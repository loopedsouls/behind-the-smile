# Behind The Smile - Telas Customizadas
# Central de Triagem da Felicidade

init python:
    # Timer para controle do jogo
    game_timer = None
    
    def start_game_timer():
        global game_timer
        store.game_start_time = pytime.time()
        store.last_spawn_check = store.game_start_time
        store.last_difficulty_increase = store.game_start_time
    
    def update_game_logic():
        """Atualiza a lógica do jogo a cada frame"""
        if store.game_state != "playing":
            return
            
        current_time = pytime.time()
        elapsed = current_time - store.game_start_time
        
        # Atualizar tempo restante
        store.time_left = max(0, int(GameConfig.GAME_DURATION - elapsed))
        
        # Verificar fim do jogo por tempo
        if store.time_left <= 0:
            store.game_state = "game_over"
            store.game_over_reason = "time"
            renpy.jump("game_over")
            return
        
        # Atualizar timers de cliente e perigo
        if store.current_customer:
            customer_elapsed = current_time - store.current_customer.get("spawn_time", current_time)
            store.customer_time_left = max(0, store.current_customer["patience"] - int(customer_elapsed))
            if store.customer_time_left <= 0:
                store.current_customer = None
        
        if store.current_danger:
            danger_elapsed = current_time - store.current_danger.get("spawn_time", current_time)
            store.danger_time_left = max(0, store.current_danger["resolve_time"] - int(danger_elapsed))
            if store.danger_time_left <= 0:
                store.game_state = "game_over"
                store.game_over_reason = "danger"
                renpy.jump("game_over")
                return
        
        # Spawn check
        if current_time - store.last_spawn_check >= GameConfig.SPAWN_INTERVAL:
            store.last_spawn_check = current_time
            try_spawn()
        
        # Dificuldade progressiva
        if current_time - store.last_difficulty_increase >= GameConfig.DIFFICULTY_INCREASE_INTERVAL:
            store.last_difficulty_increase = current_time
            store.difficulty_multiplier *= GameConfig.DIFFICULTY_MULTIPLIER
    
    def try_spawn():
        """Tenta spawnar cliente ou perigo"""
        customer_chance = GameConfig.SPAWN_CUSTOMER_CHANCE * store.difficulty_multiplier
        danger_chance = GameConfig.SPAWN_DANGER_CHANCE * store.difficulty_multiplier
        
        if not store.current_customer and random.random() < customer_chance:
            spawn_customer()
        
        if not store.current_danger and random.random() < danger_chance:
            spawn_danger()
    
    def spawn_customer():
        """Spawna um novo cliente"""
        store.current_customer = get_random_customer()
        store.current_customer["spawn_time"] = pytime.time()
        store.customer_time_left = store.current_customer["patience"]
    
    def spawn_danger():
        """Spawna um novo perigo"""
        store.current_danger = get_random_danger()
        store.current_danger["spawn_time"] = pytime.time()
        store.danger_time_left = store.current_danger["resolve_time"]
    
    def toggle_mask():
        """Alterna o estado da máscara"""
        store.mask_on = not store.mask_on
        
        # Se tirou a máscara com cliente presente = GAME OVER
        if not store.mask_on and store.current_customer:
            store.game_state = "game_over"
            store.game_over_reason = "caught"
            renpy.jump("game_over")
    
    def serve_customer():
        """Tenta atender o cliente"""
        if not store.current_customer:
            return False
        
        if not store.mask_on:
            renpy.notify("Coloque a máscara para atender!")
            return False
        
        store.score += store.current_customer["points"]
        store.customers_served += 1
        store.current_customer = None
        renpy.notify("Cliente atendido! +" + str(store.current_customer["points"] if store.current_customer else 0) + " pontos")
        return True
    
    def resolve_danger():
        """Tenta resolver o perigo"""
        if not store.current_danger:
            return False
        
        if store.mask_on:
            renpy.notify("Tire a máscara para resolver o perigo!")
            return False
        
        points = store.current_danger["points"]
        store.score += points
        store.dangers_resolved += 1
        store.current_danger = None
        renpy.notify("Perigo resolvido! +" + str(points) + " pontos")
        return True

# ==================== TELA DO HUD DO JOGO ====================
screen game_hud():
    # Atualizar lógica do jogo
    timer 0.1 repeat True action Function(update_game_logic)
    
    # Background da loja
    add "bg store"
    
    # Jogador (lado esquerdo, atrás do balcão)
    if mask_on:
        add "player_mask" xpos 150 ypos 450
    else:
        add "player_idle" xpos 150 ypos 450
    
    # Cliente (centro da tela)
    if current_customer:
        $ cust_id = current_customer.get("id", "normal")
        if cust_id == "normal":
            add "customer_normal" xpos 700 ypos 470
        elif cust_id == "bizarre":
            add "customer_bizarre" xpos 700 ypos 470
        elif cust_id == "angry":
            add "customer_angry" xpos 700 ypos 470
        elif cust_id == "vip":
            add "customer_vip" xpos 700 ypos 470
        elif cust_id == "inspector":
            add "customer_inspector" xpos 700 ypos 470
        elif cust_id == "robot":
            add "customer_robot" xpos 700 ypos 470
        elif cust_id == "child":
            add "customer_child" xpos 700 ypos 490
        elif cust_id == "paranoid":
            add "customer_paranoid" xpos 700 ypos 470
    
    # Perigo (canto superior direito)
    if current_danger:
        $ dang_id = current_danger.get("id", "alarm")
        if dang_id == "fire":
            add "danger_fire" xpos 1100 ypos 150
        elif dang_id == "alarm":
            add "danger_alarm" xpos 1100 ypos 150
        elif dang_id == "monster":
            add "danger_monster" xpos 1100 ypos 150
        elif dang_id == "mail":
            add "danger_mail" xpos 1100 ypos 150
        elif dang_id == "leak":
            add "danger_leak" xpos 1100 ypos 150
        elif dang_id == "blackout":
            add "danger_blackout" xpos 1100 ypos 150
        elif dang_id == "rat":
            add "danger_rat" xpos 1100 ypos 150
        elif dang_id == "glitch":
            add "danger_glitch" xpos 1100 ypos 150
        elif dang_id == "phone":
            add "danger_phone" xpos 1100 ypos 150
    
    # Olhos de vigilância nos cantos
    add "surveillance_eye" xpos 30 ypos 30
    add "surveillance_eye" xpos 1200 ypos 30
    add "surveillance_eye" xpos 1200 ypos 350
    
    # Overlay da máscara (se ativa)
    if mask_on:
        add "mask_overlay"
        # Texto "SORRIA!" no topo
        text "☺ SORRIA! ☺" xalign 0.5 ypos 40 size 36 color "#f4d03f" outlines [(2, "#000000", 0, 0)]
    
    # HUD Superior
    frame:
        xalign 0.5
        yalign 0.0
        yoffset 10
        xpadding 20
        ypadding 10
        background "#1a1a2eDD"
        
        hbox:
            spacing 50
            
            # Timer
            hbox:
                spacing 5
                text "⏱️" size 24
                if time_left <= GameConfig.TIME_CRITICAL:
                    text "[time_left]s" size 24 color "#ff4444"
                elif time_left <= GameConfig.TIME_WARNING:
                    text "[time_left]s" size 24 color "#ffaa00"
                else:
                    text "[time_left]s" size 24 color "#44ff44"
            
            # Status da Máscara
            hbox:
                spacing 5
                if mask_on:
                    text "😊" size 24
                    text "Máscara ON" size 20 color "#44ff44"
                else:
                    text "😐" size 24
                    text "Máscara OFF" size 20 color "#ff4444"
            
            # Pontuação
            hbox:
                spacing 5
                text "⭐" size 24
                text "[score]" size 24 color "#f4d03f"
    
    # Status do Cliente (lado esquerdo)
    frame:
        xalign 0.0
        yalign 0.5
        xpadding 15
        ypadding 15
        xoffset 20
        background "#2a2a4eDD"
        
        vbox:
            spacing 5
            text "👤 CLIENTE" size 18 color "#aaaaaa"
            if current_customer:
                text current_customer["emoji"] + " " + current_customer["name"] size 20
                text current_customer["description"] size 14 color "#888888"
                hbox:
                    spacing 5
                    text "⏳" size 16
                    if customer_time_left <= 2:
                        text "[customer_time_left]s" size 16 color "#ff4444"
                    else:
                        text "[customer_time_left]s" size 16 color "#ffaa00"
            else:
                text "Nenhum" size 18 color "#666666"
    
    # Status do Perigo (lado direito)
    frame:
        xalign 1.0
        yalign 0.5
        xpadding 15
        ypadding 15
        xoffset -20
        background "#4e2a2aDD"
        
        vbox:
            spacing 5
            text "⚠️ PERIGO" size 18 color "#aaaaaa"
            if current_danger:
                text current_danger["emoji"] + " " + current_danger["name"] size 20 color "#ff6666"
                text current_danger["description"] size 14 color "#aa6666"
                hbox:
                    spacing 5
                    text "⏳" size 16
                    if danger_time_left <= 3:
                        text "[danger_time_left]s" size 16 color "#ff4444"
                    else:
                        text "[danger_time_left]s" size 16 color "#ffaa00"
            else:
                text "Nenhum" size 18 color "#666666"
    
    # Controles (parte inferior)
    frame:
        xalign 0.5
        yalign 1.0
        yoffset -20
        xpadding 20
        ypadding 15
        background "#1a1a2eDD"
        
        hbox:
            spacing 30
            
            # Botão Máscara
            textbutton ("😐 Tirar Máscara [[ESPAÇO]]" if mask_on else "😊 Colocar Máscara [[ESPAÇO]]"):
                action Function(toggle_mask)
                style "game_button"
            
            # Botão Atender
            if current_customer:
                textbutton "🤝 Atender [[E]]":
                    action Function(serve_customer)
                    style "game_button"
            else:
                textbutton "🤝 Atender [[E]]":
                    style "game_button_disabled"
            
            # Botão Resolver
            if current_danger:
                textbutton "🔧 Resolver [[R]]":
                    action Function(resolve_danger)
                    style "game_button"
            else:
                textbutton "🔧 Resolver [[R]]":
                    style "game_button_disabled"
    
    # Atalhos de teclado
    key "K_SPACE" action Function(toggle_mask)
    key "K_e" action Function(serve_customer)
    key "K_r" action Function(resolve_danger)
    key "K_ESCAPE" action Jump("pause_game")

# ==================== TELA DE MENU ====================
screen main_menu_custom():
    tag menu
    
    add "bg dark"
    
    # Olhos decorativos (posições relativas para 16:9)
    text "👁️" xpos 0.05 ypos 0.15 size 30 color "#ffffff4D"
    text "👁️" xpos 0.85 ypos 0.25 size 30 color "#ffffff4D"
    text "👁️" xpos 0.08 ypos 0.6 size 30 color "#ffffff4D"
    text "👁️" xpos 0.9 ypos 0.7 size 30 color "#ffffff4D"
    
    # Container principal centralizado
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 15
        
        # Logo
        text "BEHIND THE SMILE" size 42 color "#f4d03f" xalign 0.5 outlines [(2, "#000000", 0, 0)]
        text "Central de Triagem da Felicidade" size 20 color "#888888" xalign 0.5
        
        null height 10
        
        # ID do Funcionário
        frame:
            background "#2a2a4e"
            xpadding 20
            ypadding 8
            xalign 0.5
            text "FUNCIONÁRIO #402" size 16 color "#f4d03f" xalign 0.5
        
        # Conteúdo em duas colunas
        hbox:
            xalign 0.5
            spacing 20
            
            # Coluna esquerda - Briefing
            frame:
                background "#1a1a2eDD"
                xpadding 20
                ypadding 15
                xsize 400
                
                vbox:
                    spacing 8
                    text "📋 Briefing Diário" size 18 color "#f4d03f"
                    text "{b}Sorria, você está sendo observado!{/b}" size 14 color "#ffffff"
                    null height 5
                    text "O mundo acabou em um colapso burocrático. Você trabalha na única instituição que sobreviveu: a {i}Central de Triagem da Felicidade{/i}." size 13 color "#cccccc"
                    null height 5
                    text "Sua missão: manter a máscara sorridente ao atender clientes, mas lembre-se — enquanto sorri, você não enxerga os perigos." size 13 color "#cccccc"
                    null height 5
                    text "⚠️ Se um cliente ver seu rosto triste, é GAME OVER." size 14 color "#ff4444"
            
            # Coluna direita - Controles
            frame:
                background "#1a1a2eDD"
                xpadding 20
                ypadding 15
                xsize 280
                
                vbox:
                    spacing 8
                    text "🎮 Controles" size 18 color "#f4d03f"
                    null height 5
                    hbox:
                        spacing 10
                        text "[[ESPAÇO]]" size 14 color "#f4d03f" min_width 80
                        text "Alternar máscara" size 14 color "#cccccc"
                    hbox:
                        spacing 10
                        text "[[E]]" size 14 color "#f4d03f" min_width 80
                        text "Atender cliente" size 14 color "#cccccc"
                    hbox:
                        spacing 10
                        text "[[R]]" size 14 color "#f4d03f" min_width 80
                        text "Resolver perigo" size 14 color "#cccccc"
                    hbox:
                        spacing 10
                        text "[[ESC]]" size 14 color "#f4d03f" min_width 80
                        text "Pausar" size 14 color "#cccccc"
        
        null height 15
        
        # Botão Iniciar
        textbutton "▶ INICIAR TURNO":
            xalign 0.5
            action Jump("start_game")
            style "menu_button"
    
    # Aviso de vigilância (parte inferior)
    frame:
        xalign 0.5
        yalign 1.0
        yoffset -15
        background "#ff444433"
        xpadding 15
        ypadding 8
        
        text "📹 Câmeras Ativas - Sorria Sempre" size 14 color "#ff4444"

# ==================== TELA DE GAME OVER ====================
screen game_over_screen():
    tag menu
    
    add "bg game_over"
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 40
        background "#2a1a1aCC"
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "GAME OVER" size 48 color "#ff4444" xalign 0.5
            
            # Razão do game over
            if game_over_reason == "caught":
                text "O cliente viu seu rosto triste!" size 24 color "#ff6666" xalign 0.5
            elif game_over_reason == "danger":
                text "O perigo não foi resolvido a tempo!" size 24 color "#ff6666" xalign 0.5
            else:
                text "Turno encerrado!" size 24 color "#ffaa00" xalign 0.5
            
            null height 20
            
            # Estatísticas
            frame:
                background "#1a1a2e"
                xpadding 30
                ypadding 20
                xalign 0.5
                
                vbox:
                    spacing 10
                    text "📊 Relatório de Desempenho" size 20 color "#f4d03f" xalign 0.5
                    
                    null height 10
                    
                    hbox:
                        spacing 50
                        xalign 0.5
                        
                        vbox:
                            xalign 0.5
                            text "Pontuação" size 14 color "#888888" xalign 0.5
                            text "[score]" size 32 color "#f4d03f" xalign 0.5
                        
                        vbox:
                            xalign 0.5
                            text "Clientes" size 14 color "#888888" xalign 0.5
                            text "[customers_served]" size 32 color "#44ff44" xalign 0.5
                        
                        vbox:
                            xalign 0.5
                            text "Perigos" size 14 color "#888888" xalign 0.5
                            text "[dangers_resolved]" size 32 color "#ffaa00" xalign 0.5
            
            null height 20
            
            # Botões
            hbox:
                spacing 20
                xalign 0.5
                
                textbutton "🔄 Tentar Novamente":
                    action Jump("start_game")
                    style "menu_button"
                
                textbutton "◀ Voltar ao Menu":
                    action Jump("main_menu")
                    style "menu_button_secondary"
            
            null height 20
            
            # Mensagem motivacional
            text "\"A felicidade é obrigatória. A tristeza é proibida.\"\n— Manual do Funcionário, Artigo 7, Parágrafo 3" size 14 color "#666666" xalign 0.5

# ==================== TELA DE PAUSA ====================
screen pause_screen():
    tag menu
    modal True
    
    add "#00000099"
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 40
        background "#1a1a2eEE"
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "⏸️ PAUSADO" size 36 color "#f4d03f" xalign 0.5
            
            null height 20
            
            textbutton "▶ Continuar":
                xalign 0.5
                action Return()
                style "menu_button"
            
            textbutton "◀ Voltar ao Menu":
                xalign 0.5
                action Jump("main_menu")
                style "menu_button_secondary"
    
    key "K_ESCAPE" action Return()

# ==================== ESTILOS ====================
style menu_button:
    background "#f4d03f"
    hover_background "#ffdd55"
    padding (30, 15)
    
style menu_button_text:
    color "#1a1a2e"
    size 20
    
style menu_button_secondary:
    background "#4a4a6e"
    hover_background "#5a5a8e"
    padding (30, 15)
    
style menu_button_secondary_text:
    color "#ffffff"
    size 20

style game_button:
    background "#4a4a6e"
    hover_background "#5a5a8e"
    padding (20, 10)
    
style game_button_text:
    color "#ffffff"
    size 16

style game_button_disabled:
    background "#2a2a3e"
    padding (20, 10)
    
style game_button_disabled_text:
    color "#666666"
    size 16
