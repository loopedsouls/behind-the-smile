# Behind The Smile - Central de Triagem da Felicidade
# Script Principal do Jogo

# ==================== PERSONAGEM NARRADOR ====================
define narrator_dystopia = Character(None, what_color="#cccccc")
define system = Character("SISTEMA", color="#f4d03f", what_color="#ffdd88")

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
    $ current_customer = None
    $ current_danger = None
    $ customers_served = 0
    $ dangers_resolved = 0
    $ difficulty_multiplier = 1.0
    
    # Iniciar timer
    $ start_game_timer()
    
    # Cena do jogo
    scene black with fade
    
    system "Turno iniciado. Boa sorte, Funcionário #402."
    system "Lembre-se: {color=#ff4444}SORRIA SEMPRE{/color}."
    
    jump game_loop

label game_loop:
    # Mostrar HUD e aguardar interação
    show screen game_hud
    
    # Loop principal - aguarda ações do jogador
    $ renpy.pause(0.1, hard=True)
    
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
    
    call screen game_over_screen()
    
    return
