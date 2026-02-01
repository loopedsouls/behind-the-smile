# Behind The Smile - Central de Triagem da Felicidade
# Script Principal do Jogo

# ==================== PERSONAGEM NARRADOR ====================
define narrator_dystopia = Character(None, what_color="#cccccc")
define system = Character("SISTEMA", color="#f4d03f", what_color="#ffdd88")
define customer_char = Character(None, color="#f4d03f", what_color="#ffffff")
define narrator = Character(None, what_color="#ffffff")
define gerente = Character("GERÊNCIA", color="#ff4444", what_color="#ffaaaa")
define eu = Character("Funcionário #404", color="#44aaff", what_color="#88ddff")

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
        # Chance de olhar aumenta com o número de clientes atendidos
        look_chance = min(0.8, 0.3 + (store.customers_served * 0.05))  # Começa em 30%, até 80%
        client_inst['is_looking'] = random.random() < look_chance
        store.current_customer = client_inst
        store.customer_leave_time = pytime.time() + random.uniform(4.0, 8.0)
        renpy.call("customer_dialogue_label")
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

label customer_dialogue_label:
    $ dialogue_line = current_customer["line"]
    customer_char "[dialogue_line]"
    
    # Menu baseado no tipo de cliente para conversa profissional e fluida
    if current_customer["id"] == "normal":
        menu:
            "Certamente, vou processar seu pedido imediatamente.":
                $ serve_customer()
                $ score += 5  # Bônus por eficiência
            "Aguarde um momento enquanto verifico os detalhes.":
                $ customer_time_left = max(1, customer_time_left - 1)
                $ renpy.notify("Cliente aguardando...")
            "Desculpe, estamos com fila. Retorne em breve.":
                $ current_customer = None
                $ renpy.notify("Cliente saiu insatisfeito.")
            "Antes de prosseguir, vou preparar um café para maior eficiência.":
                $ drink_coffee()
                $ renpy.notify("Café preparado. Cliente mais calmo.")
    elif current_customer["id"] == "bizarre":
        menu:
            "Entendo sua preocupação. Vou auxiliar com eficiência.":
                $ serve_customer()
                $ arm_stability += 5  # Recupera estabilidade por empatia
            "Preciso de mais informações sobre sua solicitação.":
                $ customer_time_left = max(1, customer_time_left - 1.5)
                $ renpy.notify("Cliente explicando...")
            "Isso parece incomum. Sugiro aguardar suporte.":
                $ current_customer = None
                $ renpy.notify("Cliente confuso saiu.")
            "Vou escanear os produtos para verificar a anomalia.":
                # Simular escaneamento rápido
                if products_to_scan:
                    $ scanned_products.extend(products_to_scan)
                    $ products_to_scan = []
                    $ renpy.notify("Produtos escaneados com sucesso.")
                else:
                    $ renpy.notify("Nenhum produto para escanear.")
    elif current_customer["id"] == "angry":
        menu:
            "Calma, vou resolver isso rapidamente para você.":
                $ serve_customer()
                $ score += 10  # Bônus por acalmar
            "Entendo sua frustração. Um instante.":
                $ customer_time_left = max(1, customer_time_left - 2)
                $ renpy.notify("Cliente se acalmando...")
            "Por favor, mantenha a compostura.":
                $ current_customer = None
                $ score -= 5  # Penalidade
                $ renpy.notify("Cliente raivoso saiu furioso!")
            "Vou aplicar o carimbo de validação para acalmar.":
                $ apply_stamp()
                $ renpy.notify("Carimbo aplicado. Cliente validado.")
    elif current_customer["id"] == "vip":
        menu:
            "É um prazer atendê-la, supervisora. Tudo em ordem.":
                $ serve_customer()
                $ score += 15  # Grande bônus
            "Verificarei pessoalmente os protocolos.":
                $ customer_time_left = max(1, customer_time_left - 0.5)
                $ renpy.notify("Supervisora aprovando...")
            "A Gerência será informada.":
                $ current_customer = None
                $ renpy.notify("Supervisora saiu satisfeita.")
            "Vou preparar um café especial para a supervisora.":
                $ drink_coffee()
                $ score += 5
                $ renpy.notify("Café premium servido.")
    elif current_customer["id"] == "inspector":
        menu:
            "Meu sorriso está sempre nos padrões. Como posso ajudar?":
                $ serve_customer()
                $ arm_stability += 10  # Recupera por conformidade
            "Vou ajustar minha expressão imediatamente.":
                $ customer_time_left = max(1, customer_time_left - 1)
                $ renpy.notify("Inspetor avaliando...")
            "A máscara garante a felicidade obrigatória.":
                $ current_customer = None
                $ renpy.notify("Inspetor satisfeito.")
            "Vou escanear os produtos para verificação.":
                $ scan_product()
                $ score += 5
                $ renpy.notify("Produtos escaneados com sucesso.")
    elif current_customer["id"] == "robot":
        menu:
            "Protocolos otimizados. Processando solicitação.":
                $ serve_customer()
                $ score += 8  # Bônus por eficiência
            "Executando diagnóstico do sistema.":
                $ customer_time_left = max(1, customer_time_left - 1.2)
                $ renpy.notify("Robô processando...")
            "Humanos são ineficientes, mas vou tentar.":
                $ current_customer = None
                $ renpy.notify("Robô saiu.")
            "Vou aplicar o carimbo necessário.":
                $ apply_stamp()
                $ score += 5
                $ renpy.notify("Carimbo aplicado com precisão.")
    else:  # paranoid or default
        menu:
            "Estamos seguros aqui. Vou ajudar discretamente.":
                $ serve_customer()
                $ arm_stability += 3
            "Entendo sua paranoia. Fique tranquilo.":
                $ customer_time_left = max(1, customer_time_left - 1.8)
                $ renpy.notify("Cliente se acalmando...")
            "Não há motivo para preocupação.":
                $ current_customer = None
                $ renpy.notify("Cliente paranóico saiu desconfiado.")
            "Vou preparar um café para acalmá-lo.":
                $ drink_coffee()
                $ arm_stability += 5
                $ renpy.notify("Café servido, cliente mais calmo.")
    
    return

# ==================== INÍCIO DO JOGO ====================
label start:
    jump main_menu

label main_menu:
    # Resetar variáveis
    $ game_state = "menu"
    $ score = 0
    $ time_left = GameConfig.GAME_DURATION
    $ mask_on = True
    $ arm_stability = 100.0
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
    $ arm_stability = 100.0
    $ mask_lower_count = 0
    $ current_customer = None
    $ current_danger = None
    $ customers_served = 0
    $ dangers_resolved = 0
    $ difficulty_multiplier = 1.0
    $ next_customer_time = pytime.time() + 3.0
    $ customer_leave_time = None
    
    # Resetar sistema de produtos
    $ products_to_scan = []
    $ scanned_products = []
    $ scanning_product = None
    $ scan_start_time = 0.0
    
    # Resetar sistema de carimbos
    $ stamps_available = []
    $ current_stamp = None
    
    # Resetar sistema de café
    $ coffee_available = True
    $ coffee_cooldown = 0.0
    $ last_coffee_time = 0.0
    
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
