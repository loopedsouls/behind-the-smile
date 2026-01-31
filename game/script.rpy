# Behind The Smile - Central de Triagem da Felicidade
# Script Principal do Jogo

# ==================== PERSONAGEM NARRADOR ====================
define narrator_dystopia = Character(None, what_color="#cccccc")
define system = Character("SISTEMA", color="#f4d03f", what_color="#ffdd88")

init python:
    # Fix for renpy.error not being callable
    def error(msg):
        print("Error:", msg)
    renpy.error = error

    import random, time as pytime
    store = renpy.store

    def spawn_customer():
        client = store.get_random_customer()
        client_inst = dict(client)
        client_inst['is_looking'] = random.choice([True, False])
        store.current_customer = client_inst
        store.customer_leave_time = pytime.time() + random.uniform(4.0, 8.0)
        renpy.show_screen("customer_dialogue", customer=client_inst)
        # schedule next spawn
        store.next_customer_time = pytime.time() + random.uniform(5.0, 12.0)
        # Ativar máscara automaticamente
        store.mask_on = True

    def is_customer_looking(c):
        return c and c.get('is_looking', False)

    def on_mask_lower():
        if not store.mask_on:
            return
        store.mask_on = False
        store.mask_lower_count = getattr(store, 'mask_lower_count', 0) + 1
        if store.current_customer and is_customer_looking(store.current_customer):
            renpy.notify("CONTRATO VIOLADO.")
            renpy.notify(store.current_customer['name'] + ": Agora podemos ver.")
            store.game_state = "game_over"
        else:
            if store.mask_lower_count == 1:
                renpy.notify("SISTEMA: Sorria. Você está sendo observado.")
            elif store.mask_lower_count == 2:
                renpy.notify("Um cliente murmura: 'A máscara não é só decoração — é uma vedação.'")

    def on_mask_raise():
        store.mask_on = True

# ==================== INÍCIO DO JOGO ====================
label start:
    jump main_menu

label main_menu:
    # Resetar variáveis
    $ game_state = "menu"
    $ score = 0
    $ time_left = GameConfig.GAME_DURATION
    $ mask_on = True
    $ current_customer = None
    $ current_danger = None
    $ customers_served = 0
    $ dangers_resolved = 0
    $ difficulty_multiplier = 1.0
    
    call screen main_menu_custom()
    return

label start_game:
    # Inicializar jogo
    $ game_state = "playing"
    $ score = 0
    $ time_left = GameConfig.GAME_DURATION
    $ mask_on = True
    $ mask_lower_count = 0
    $ current_customer = None
    $ current_danger = None
    $ customers_served = 0
    $ dangers_resolved = 0
    $ difficulty_multiplier = 1.0
    $ next_customer_time = pytime.time() + 3.0
    $ customer_leave_time = None
    
    # Ocultar elementos de visual novel
    window hide
    $ renpy.block_rollback()
    $ _skipping = False
    
    # Iniciar timer
    $ start_game_timer()
    
    # Cena do jogo
    scene black with fade
    
    jump game_loop

label game_loop:
    # Mostrar HUD e aguardar interação
    show screen game_hud
    
    # Loop principal - aguarda ações do jogador
    $ renpy.pause(0.1, hard=True)
    
    # Checar spawn/saída de clientes
    $ now = pytime.time()
    if current_customer is None and now >= next_customer_time:
        $ spawn_customer()
    if current_customer is not None and customer_leave_time and now >= customer_leave_time:
        $ renpy.notify(current_customer['name'] + " saiu.")
        $ current_customer = None
    
    # Verificar estado do jogo
    if game_state == "game_over":
        jump game_over
    elif game_state == "playing":
        jump game_loop
    
    return

label pause_game:
    $ old_state = game_state
    $ game_state = "paused"
    
    call screen pause_screen()
    
    $ game_state = "playing"
    $ game_start_time = pytime.time() - (GameConfig.GAME_DURATION - time_left)
    
    jump game_loop

label game_over:
    hide screen game_hud
    window hide
    
    call screen game_over_screen()
    
    return
