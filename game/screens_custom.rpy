# Behind The Smile - Telas Customizadas
# Central de Triagem da Felicidade

init python:
    # Timer para controle do jogo
    game_timer = None
    
    import math  # Para cálculos do relógio
    
    def start_game_timer():
        global game_timer
        store.game_start_time = pytime.time()
        store.last_spawn_check = store.game_start_time
        store.last_difficulty_increase = store.game_start_time
        store.last_stability_update = store.game_start_time
        store.last_announcement = store.game_start_time
    
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
            store.game_state = "day_end"
            return
        
        # Atualizar animação de entrada do cliente
        if store.customer_entering and store.current_customer:
            enter_elapsed = current_time - store.customer_enter_time
            if enter_elapsed >= 0.4:  # Duração da animação de entrada (fade 0.4s)
                store.customer_entering = False
        
        # Atualizar timers de cliente e perigo
        if store.current_customer and not store.customer_entering:
            customer_elapsed = current_time - store.current_customer.get("spawn_time", current_time) - 1.5
            store.customer_time_left = max(0, store.current_customer["patience"] - int(customer_elapsed))
            if store.customer_time_left <= 0:
                store.current_customer = None
                store.customer_entering = False
                store.mask_on = False  # Desativar máscara quando cliente vai embora
        
        # Atualizar posição do mouse
        mouse_pos = renpy.get_mouse_pos()
        store.mouse_x, store.mouse_y = mouse_pos
        
        # Atualizar estabilidade do braço
        if store.mask_on:
            stability_elapsed = current_time - store.last_stability_update
            if stability_elapsed >= 1.0:  # Atualizar a cada segundo
                # Decaimento exponencial baseado no número de clientes atendidos
                base_decay = 5.0
                exponential_factor = 1.15 ** (store.customers_served // 3)  # Aumenta a cada 3 clientes atendidos
                current_decay_rate = base_decay * exponential_factor
                store.arm_stability = max(0, store.arm_stability - current_decay_rate)
                store.last_stability_update = current_time
                if store.arm_stability <= 0:
                    store.game_state = "game_over"
                    store.game_over_reason = "exhaustion"
                    renpy.jump("game_over")
        else:
            # Recuperar estabilidade gradualmente quando máscara está baixa
            stability_elapsed = current_time - store.last_stability_update
            if stability_elapsed >= 1.0:  # Atualizar a cada segundo
                recovery_rate = 3.0  # Recupera 3 pontos por segundo
                store.arm_stability = min(100.0, store.arm_stability + recovery_rate)
                store.last_stability_update = current_time
        
        # Screenshake quando estabilidade baixa
        if store.arm_stability < 30 and random.random() < 0.1:  # 10% chance por frame
            # Note: Screenshake not implemented due to syntax issues
            pass
        
        # Spawn check
        if current_time - store.last_spawn_check >= GameConfig.SPAWN_INTERVAL:
            store.last_spawn_check = current_time
            try_spawn()
        
        # Anúncios da Gerência (fragments de lore)
        if not hasattr(store, 'last_announcement') or current_time - store.last_announcement >= 30.0:
            store.last_announcement = current_time
            fragment = random.choice(store.LORE["fragments"])
            renpy.notify("ANÚNCIO DA GERÊNCIA: " + fragment)
        
        # Atualizar escaneamento de produtos
        update_scanning()
    
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
        # Reduzir paciência baseado no número de clientes atendidos (mais rápido a cada 3 atendidos)
        speed_reduction = store.customers_served // 3
        store.current_customer["patience"] = max(1, store.current_customer["patience"] - speed_reduction)
        store.current_customer["spawn_time"] = pytime.time()
        store.customer_time_left = store.current_customer["patience"]
        store.customer_entering = True
        store.customer_enter_time = pytime.time()
        # voltar ao estado normal ao aparecer cliente
        store.player_status = "normal"
        # Spawn produtos para escanear
        spawn_products()
    
    def spawn_danger():
        """Spawna um novo perigo"""
        store.current_danger = get_random_danger()
        # Reduzir tempo de resolução baseado no número de perigos resolvidos (mais rápido a cada 2 resolvidos)
        speed_reduction = store.dangers_resolved // 2
        store.current_danger["resolve_time"] = max(1, store.current_danger["resolve_time"] - speed_reduction)
        store.current_danger["spawn_time"] = pytime.time()
        store.danger_time_left = store.current_danger["resolve_time"]
        # ajustar estado visual baseado na severidade do perigo
        if store.current_danger.get("severity") == "critical":
            store.player_status = "infected"
        else:
            store.player_status = "alert"
    
    def toggle_mask():
        """Alterna o estado da máscara"""
        store.mask_on = not store.mask_on
        
        # Se tirou a máscara com cliente presente (e não está entrando) = GAME OVER
        if not store.mask_on and store.current_customer and not store.customer_entering:
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
        
        points = store.current_customer["points"]
        store.score += points
        store.customers_served += 1
        store.current_customer = None
        # voltar ao estado visual normal
        store.player_status = "normal"
        renpy.notify("Cliente atendido! +" + str(points) + " pontos")
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
        # reset estado visual
        store.player_status = "normal"
        renpy.notify("Perigo resolvido! +" + str(points) + " pontos")
        return True
    
    def spawn_products():
        """Spawna produtos aleatórios no balcão para escanear"""
        if store.current_customer and not store.products_to_scan:
            # Escolhe 2-4 produtos aleatórios
            num_products = random.randint(2, 4)
            available_products = store.PRODUCTS.copy()
            random.shuffle(available_products)
            store.products_to_scan = available_products[:num_products]
            store.scanned_products = []
            store.scanning_product = None
            renpy.notify("Produtos no balcão! Use o scanner para bipar.")
    
    def scan_product(product_id):
        """Inicia o escaneamento de um produto"""
        if store.mask_on:
            renpy.notify("Tire a máscara para usar o scanner!")
            return
        
        if product_id in store.scanned_products:
            renpy.notify("Produto já escaneado!")
            return
        
        if store.scanning_product:
            renpy.notify("Já escaneando um produto!")
            return
        
        # Encontra o produto
        product = next((p for p in store.products_to_scan if p["id"] == product_id), None)
        if not product:
            return
        
        store.scanning_product = product
        store.scan_start_time = pytime.time()
        renpy.notify("Escaneando " + product["name"] + "...")
    
    def update_scanning():
        """Atualiza o progresso do escaneamento"""
        if not store.scanning_product:
            return
        
        elapsed = pytime.time() - store.scan_start_time
        if elapsed >= store.scanning_product["scan_time"]:
            # Escaneamento completo
            store.scanned_products.append(store.scanning_product["id"])
            renpy.notify(store.scanning_product["name"] + " escaneado!")
            store.scanning_product = None
            
            # Verifica se todos os produtos foram escaneados
            if len(store.scanned_products) >= len(store.products_to_scan):
                store.products_to_scan = []
                store.scanned_products = []
                renpy.notify("Todos os produtos escaneados! Pronto para carimbar.")
    
    def select_stamp(stamp_id):
        """Seleciona um carimbo para usar"""
        if store.mask_on:
            renpy.notify("Tire a máscara para usar os carimbos!")
            return
        
        stamp = next((s for s in store.STAMPS if s["id"] == stamp_id), None)
        if stamp:
            store.current_stamp = stamp
            renpy.notify("Carimbo '" + stamp["name"] + "' selecionado.")
    
    def apply_stamp():
        """Aplica o carimbo selecionado para validar a compra"""
        if not store.current_stamp:
            renpy.notify("Selecione um carimbo primeiro!")
            return
        
        if not store.current_customer:
            renpy.notify("Nenhum cliente para validar!")
            return
        
        if store.mask_on:
            renpy.notify("Tire a máscara para carimbar!")
            return
        
        # Verificar se todos os produtos foram escaneados
        if store.products_to_scan and len(store.scanned_products) < len(store.products_to_scan):
            renpy.notify("Escaneie todos os produtos primeiro!")
            return
        
        # Aplica o carimbo e finaliza a venda
        points = store.current_customer["points"] + 5  # Pontos extras por validação
        store.score += points
        store.customers_served += 1
        store.current_customer = None
        store.current_stamp = None
        store.products_to_scan = []
        store.scanned_products = []
        store.player_status = "normal"
        renpy.notify("Compra validada com carimbo! +" + str(points) + " pontos")
    
    def drink_coffee():
        """Bebe café para recuperar estabilidade do braço"""
        if store.mask_on:
            renpy.notify("Tire a máscara para beber café!")
            return
        
        current_time = pytime.time()
        if current_time - store.last_coffee_time < 30.0:  # Cooldown de 30 segundos
            remaining = int(30.0 - (current_time - store.last_coffee_time))
            renpy.notify("Café em cooldown! " + str(remaining) + "s restantes.")
            return
        
        # Recupera estabilidade
        recovery_amount = 40.0
        old_stability = store.arm_stability
        store.arm_stability = min(100.0, store.arm_stability + recovery_amount)
        actual_recovery = store.arm_stability - old_stability
        
        store.last_coffee_time = current_time
        renpy.notify("Café bebido! Estabilidade +" + str(int(actual_recovery)))

    # ==================== DISPLAYABLES DO RELÓGIO ====================
    
    class ClockDisplayable(renpy.Displayable):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            
        def render(self, width, height, st, at):
            # Forçar redesenho a cada frame
            renpy.redraw(self, 0)
            
            rv = renpy.Render(width, height)
            
            # Criar superfície para desenhar
            surf = renpy.display.pgrender.surface((width, height), True)
            
            # Fundo do relógio (círculo simples)
            import pygame
            pygame.draw.circle(surf, renpy.color.Color("#1a1a2e"), (width//2, height//2), width//2)
            pygame.draw.circle(surf, renpy.color.Color("#2a2a4e"), (width//2, height//2), width//2 - 2, 2)
            
            # Marcas das horas
            center_x, center_y = width // 2, height // 2
            for i in range(12):
                angle = i * 30  # 30 graus por hora
                rad = math.radians(angle - 90)
                x1 = center_x + 25 * math.cos(rad)
                y1 = center_y + 25 * math.sin(rad)
                pygame.draw.circle(surf, renpy.color.Color("#f4d03f"), (int(x1), int(y1)), 1)
            
            # Ponteiro baseado no tempo
            if hasattr(store, 'next_customer_time') and store.next_customer_time:
                current_time = pytime.time()
                time_to_next = max(0, store.next_customer_time - current_time)
                max_time = 60.0
                progress = min(1.0, time_to_next / max_time)
                
                angle = (1.0 - progress) * 360.0
                rad = math.radians(angle - 90)
                
                hand_length = 28
                x_end = center_x + hand_length * math.cos(rad)
                y_end = center_y + hand_length * math.sin(rad)
                
                # Cor do ponteiro
                if time_to_next <= 10:
                    color = "#ff4444"
                elif time_to_next <= 30:
                    color = "#ffaa44"
                else:
                    color = "#44ff44"
                
                # Desenhar linha do ponteiro
                pygame.draw.line(surf, renpy.color.Color(color), (center_x, center_y), (x_end, y_end), 3)
            
            # Centro do relógio
            pygame.draw.circle(surf, renpy.color.Color("#f4d03f"), (center_x, center_y), 3)
            
            # Converter superfície para texture e blitar no render
            tex = renpy.display.draw.load_texture(surf)
            rv.blit(tex, (0, 0))
            
            return rv
            
        def visit(self):
            return []

# Transform para texto rolando da lore removido
# transform scrolling_lore:
#     # Começa fora da tela à direita
#     xpos 1280
#     # Move para a esquerda lentamente
#     linear 30.0 xpos -2000  # Ajustar velocidade e distância baseada no comprimento do texto
#     # Repete
#     repeat

# ==================== TELA DO HUD DO JOGO ====================
screen game_hud():
    # Atualizar lógica do jogo
    timer 0.1 repeat True action Function(update_game_logic)

    # Texto da lore rolando no topo removido
    # $ lore_text = " | ".join(store.LORE["fragments"] * 3)  # Repetir 3 vezes para texto mais longo
    # text lore_text at scrolling_lore ypos 10 size 18 color "#666666"

    # Background da loja — seleciona variante por status e máscara
    if current_danger:
        $ danger_bg_map = {
            "fire": "mask/fogopratileira.jpg",
            "alarm": "mask/alarmeseguranca.jpg",
            "monster": "mask/algonassombras.jpg",
            "leak": "mask/vazamento.jpg",
            "blackout": "mask/quedadeluz.jpg",
            "rat": "mask/infestacao.jpg",
            "glitch": "mask/glitchnacamera.jpg",
            "phone": "mask/ligacaocentral.jpg"
        }
        $ danger_bg = danger_bg_map.get(current_danger["id"], "bg store_normal")
        add danger_bg size (1280, 720) at bg_crossfade
    elif player_status == "normal":
        if mask_on:
            add "bg store_normal" at bg_crossfade
        else:
            add "bg store_unmasked_normal" at bg_crossfade
    elif player_status == "alert":
        if mask_on:
            add "bg store_alert" at bg_crossfade
        else:
            add "bg store_unmasked_alert" at bg_crossfade
    elif player_status == "infected":
        if mask_on:
            add "bg store_infected" at bg_crossfade
        else:
            add "bg store_unmasked_infected" at bg_crossfade
    else:
        # fallback
        if mask_on:
            add "bg store_normal" at bg_crossfade
        else:
            add "bg store_unmasked_normal" at bg_crossfade
    
    # Porta removida (anteriormente mostrada à direita)
    
    # Jogador removido do canto esquerdo (oculto por solicitação)
    # Antes: add "player_idle" at player_breathing
    
    # Cliente com animação
    if current_customer:
        $ cust_id = current_customer.get("id", "normal")
        $ sprite_mapping = {
            "normal": "customer_monstro",
            "inspector": "customer_monstro",
            "bizarre": "customer_alien",
            "robot": "customer_alien",
            "angry": "customer_he",
            "vip": "customer_she",
            "paranoid": "customer_she"
        }
        $ cust_sprite = sprite_mapping.get(cust_id, "customer_monstro")
        if customer_entering:
            # Cliente aparece com fade no centro
            add cust_sprite at customer_fade
        else:
            # Cliente parado no centro com respiração
            add cust_sprite at customer_idle, idle_breathing
    
    # Perigo (removido - agora usa background)
    # if current_danger:
    #     $ dang_id = current_danger.get("id", "alarm")
    #     $ dang_sprite = "danger_" + dang_id
    #     add dang_sprite xpos 900 ypos 120
    
    # Olhos de vigilância nos cantos
    add "surveillance_eye" xpos 30 ypos 30
    add "surveillance_eye" xpos 1200 ypos 30
    add "surveillance_eye" xpos 1200 ypos 350
    
    # Overlay da máscara (se ativa) - segue mouse apenas quando estabilidade baixa
    if mask_on:
        if arm_stability < 50:
            # Quando estabilidade baixa, máscara segue mouse (clamp para área do rosto)
            $ mask_x = max(500, min(780, mouse_x))
            $ mask_y = max(200, min(400, mouse_y))
            # Adicionar tremor se estabilidade muito baixa
            if arm_stability < 30:
                $ mask_x += renpy.random.randint(-10, 10)
                $ mask_y += renpy.random.randint(-10, 10)
            add "mask_overlay" pos (mask_x, mask_y) anchor (0.5, 0.5)
        else:
            # Normal: overlay estático
            add "mask_overlay"
        # Texto "SORRIA!" no topo (sem emojis)
        text "SORRIA!" xalign 0.5 ypos 40 size 36 color "#f4d03f" outlines [(2, "#000000", 0, 0)]
    
    # Relógio Digital no topo direito
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -20
        yoffset 20
        xpadding 15
        ypadding 10
        background "#1a1a2eDD"
        
        vbox:
            spacing 5
            text "DIA [current_day]" size 18 color "#f4d03f" bold True
            text "[time_left]s" size 24 color "#f4d03f" bold True
    
    # Barra de Estabilidade do Braço (Vertical - Lado Esquerdo)
    frame:
        xalign 0.0
        xoffset 20
        yalign 0.5
        xpadding 15
        ypadding 20
        background "#1a1a2eDD"
        
        vbox:
            spacing 5
            text "Estabilidade do Braço" size 14 color "#ffffff" xalign 0.5
            bar value arm_stability range 100 xsize 200 ysize 25 at Transform(rotate=270)
    
    # Relógio de Spawn de Cliente (Canvas Sprite)
    frame:
        xalign 0.5
        yalign 1.0
        yoffset -100
        xpadding 15
        ypadding 10
        background "#1a1a2eDD"
        
        vbox:
            spacing 5
            text "Próximo Cliente" size 14 color "#f4d03f" xalign 0.5
            
            # Canvas com relógio circular
            fixed:
                xsize 80
                ysize 80
                align (0.5, 0.5)
                
                # Relógio completo em um displayable
                add ClockDisplayable()
            
            # Texto com tempo restante
            $ time_to_next = max(0, int(store.next_customer_time - pytime.time())) if store.next_customer_time else 0
            text "[time_to_next]s" size 16 color "#ffffff" xalign 0.5
    
    # Botões para Android (lado direito)
    frame:
        xalign 1.0
        yalign 0.5
        xoffset -10
        background None
        
        vbox:
            spacing 10
            textbutton "Máscara" action Function(toggle_mask) style "game_button"
            textbutton "Resolver" action Function(resolve_danger) style "game_button"
    # HUD removido — lógica mantida
    # frame:
    #     xalign 0.5
    #     yalign 0.0
    #     yoffset 10
    #     xpadding 20
    #     ypadding 10
    #     background "#1a1a2eDD"
    #     
    #     hbox:
    #         spacing 50
    #         
    #         # Timer
    #         hbox:
    #             spacing 5
    #             text "Tempo" size 24
    #             if time_left <= GameConfig.TIME_CRITICAL:
    #                 text "[time_left]s" size 24 color "#ff4444"
    #             elif time_left <= GameConfig.TIME_WARNING:
    #                 text "[time_left]s" size 24 color "#ffaa00"
    #             else:
    #                 text "[time_left]s" size 24 color "#44ff44"
    #         
    #         # Status da Máscara
    #         hbox:
    #             spacing 5
    #             if mask_on:
    #                 text "Máscara ON" size 20 color "#44ff44"
    #             else:
    #                 text "Máscara OFF" size 20 color "#ff4444"
    #         
    #         # Pontuação
    #         hbox:
    #             spacing 5
    #             text "Pontos" size 24
    #             text "[score]" size 24 color "#f4d03f"

    # Aviso: cliente chegando (removido)
    # if customer_entering:
    #     frame:
    #         xalign 0.5
    #         yalign 0.12
    #         background "#1a1a2eCC"
    #         xpadding 12
    #         ypadding 6
    #         text "Cliente chegando..." size 20 color "#f4d03f"

    # Status do Cliente (removido)
    # frame:
    #     xalign 0.0
    #     yalign 0.5
    #     xpadding 15
    #     ypadding 15
    #     xoffset 20
    #     background "#2a2a4eDD"
    #     
    #     vbox:
    #         spacing 5
    #         text "CLIENTE" size 18 color "#aaaaaa"
    #         if current_customer:
    #             text current_customer["emoji"] + " " + current_customer["name"] size 20
    #             text current_customer["description"] size 14 color "#888888"
    #             hbox:
    #                 spacing 5
    #                 if customer_time_left <= 2:
    #                     text "[customer_time_left]s" size 16 color "#ff4444"
    #                 else:
    #                     text "[customer_time_left]s" size 16 color "#ffaa00"
    #         else:
    #             text "Nenhum" size 18 color "#666666"
    
    # Status do Perigo (removido)
    # frame:
    #     xalign 1.0
    #     yalign 0.5
    #     xpadding 15
    #     ypadding 15
    #     xoffset -20
    #     background "#4e2a2aDD"
    #     
    #     vbox:
    #         spacing 5
    #         text "PERIGO" size 18 color "#aaaaaa"
    #         if current_danger:
    #             text current_danger["emoji"] + " " + current_danger["name"] size 20 color "#ff6666"
    #             text current_danger["description"] size 14 color "#aa6666"
    #             hbox:
    #                 spacing 5
    #                 if danger_time_left <= 3:
    #                     text "[danger_time_left]s" size 16 color "#ff4444"
    #                 else:
    #                     text "[danger_time_left]s" size 16 color "#ffaa00"
    #         else:
    #             text "Nenhum" size 18 color "#666666"
    
    # Controles removidos da tela — usar teclado
    # Exibir dica discreta indicando as teclas (ajuda completa em Options)
    
    # Atalhos de teclado
    key "K_z" action Function(toggle_mask)
    key "K_c" action Function(resolve_danger)
    key "K_ESCAPE" action Jump("pause_game")

# ==================== TELA DE MENU ====================

# Variáveis usadas para controlar o estado do menu
# Hover para itens e erro (glitch) para o background
default _menu_hover = None
default _menu_error = False

# Transforms para efeito de picote / glitch (2D)
transform glitch_jitter:
    # movimentos rápidos laterais para simular 'picote' (mais rápidos)
    xoffset 0
    linear 0.01 xoffset 16
    linear 0.01 xoffset -16
    linear 0.01 xoffset 8
    linear 0.01 xoffset -8
    linear 0.01 xoffset 0

transform glitch_flash:
    alpha 0.0
    linear 0.01 alpha 1.0
    pause 0.03
    linear 0.01 alpha 0.0

# Transform global para crossfade de background usado no HUD
transform bg_crossfade:
    alpha 0.0
    linear 0.15 alpha 1.0

screen main_menu_custom():
    tag menu
    
    # Fundo do menu: imagem do menu (escalada) - sem sobreposição
    add "menu_bg"

    # Camadas de glitch/erro (aparecem quando _menu_error é True) — durante o glitch, trocamos para menu2_bg
    if _menu_error:
        add "menu2_bg" at glitch_jitter alpha 1.0
        add Solid("#ff4444") alpha 0.16
        add Solid("#ffffff") at glitch_flash alpha 0.08

    # Timers para alternar o estado de erro (rajadas mais rápidas)
    timer 4.0 action SetVariable("_menu_error", True) repeat True
    # Timer que desativa o erro após 0.2s — definido somente enquanto _menu_error for True
    if _menu_error:
        timer 0.2 action SetVariable("_menu_error", False)

    # Menu minimalista no rodapé (botões em linha, centralizados)
    frame:
        background None
        xalign 0.5
        yalign 1.0
        yoffset -60
        xpadding 0
        ypadding 0

        hbox:
            xalign 0.5
            spacing 60

            textbutton "[_menu_hover == 'start' and '{size=40}{color=#f4d03f}Start Game{/color}{/size}' or '{size=36}{color=#ffffff}Start Game{/color}{/size}']":
                hovered SetVariable("_menu_hover", "start")
                unhovered SetVariable("_menu_hover", None)
                action Jump("start_game")
                style "menu_button"

            textbutton "[_menu_hover == 'historia' and '{size=40}{color=#f4d03f}História{/color}{/size}' or '{size=36}{color=#ffffff}História{/color}{/size}']":
                hovered SetVariable("_menu_hover", "historia")
                unhovered SetVariable("_menu_hover", None)
                action Show("lore_screen")
                style "menu_button_secondary"

            textbutton "[_menu_hover == 'exit' and '{size=40}{color=#f4d03f}Exit{/color}{/size}' or '{size=36}{color=#ffffff}Exit{/color}{/size}']":
                hovered SetVariable("_menu_hover", "exit")
                unhovered SetVariable("_menu_hover", None)
                action Quit(confirm=True)
                style "menu_button_secondary"

# ==================== TELA DE GAME OVER ====================
screen controls_help():
    tag menu
    modal True
    zorder 100
    add Solid("#00000080")
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20
        background "#1a1a1aDD"
        vbox:
            spacing 12
            xalign 0.5
            text "Ajuda de Controles" size 28 color "#f4d03f" xalign 0.5
            text "Z — Alternar Máscara (colocar/tirar)" size 18
            text "X — Atender funcionário (quando disponível)" size 18
            text "C — Resolver emergência (quando disponível)" size 18
            text "ESC — Pausar / Abrir menu" size 18
            text "Dica: Os botões na tela foram removidos. Use o teclado para maior imersão." size 16 color "#bbbbbb"
            textbutton "Fechar" action Return() xalign 0.5 style "menu_button_secondary"

screen game_over_screen():
    tag menu
    
    # Fundo vermelho escuro
    add Solid("#330000")
    
    # Overlay da máscara quebrada
    add "mask_overlay"
    
    # Filtro vermelho intenso
    add Solid("#ff000080")
    
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
            
            text "Turno [current_shift]/5" size 24 color "#ffffff" xalign 0.5
            
            # Razão do game over
            if game_over_reason == "caught":
                text "O funcionário viu seu rosto triste!" size 24 color "#ff6666" xalign 0.5
            elif game_over_reason == "danger":
                text "A emergência não foi resolvida a tempo!" size 24 color "#ff6666" xalign 0.5
            elif game_over_reason == "mask_off_spawn":
                text "Cliente apareceu sem máscara ativa!" size 24 color "#ff6666" xalign 0.5
                text "A Gerência não tolera exposição." size 18 color "#ffaaaa" xalign 0.5
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
                    text "Relatório de Desempenho" size 20 color "#f4d03f" xalign 0.5
                    
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
                            text "Funcionários" size 14 color "#888888" xalign 0.5
                            text "[customers_served]" size 32 color "#44ff44" xalign 0.5
                        
                        vbox:
                            xalign 0.5
                            text "Emergências" size 14 color "#888888" xalign 0.5
                            text "[dangers_resolved]" size 32 color "#ffaa00" xalign 0.5
            
            null height 20
            
            # Botões
            hbox:
                spacing 20
                xalign 0.5
                
                textbutton "Tentar Novamente":
                    action [SetVariable("game_state", "playing"), Jump("retry_current_day")]
                    style "menu_button"
                
                textbutton "Voltar ao Menu":
                    action Jump("main_menu")
                    style "menu_button_secondary"
            
            null height 20
            
            # Mensagem motivacional
            text "\"A felicidade é obrigatória. A tristeza é proibida.\"\n— Manual do Funcionário, Artigo 7, Parágrafo 3" size 14 color "#666666" xalign 0.5

# ==================== TELA DE PAUSA ====================
screen pause_screen():
    tag menu
    modal True
    zorder 200
    
    # Fundo: placa centralizada
    add "pause_plate" xalign 0.5 yalign 0.5
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 40
        background None
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "PAUSADO" size 36 color "#f4d03f" xalign 0.5
            
            null height 20
            
            textbutton "Continuar":
                xalign 0.5
                action Return()
                style "menu_button"
            
            textbutton "Voltar ao Menu":
                xalign 0.5
                action Jump("main_menu")
                style "menu_button_secondary"
    
    key "K_ESCAPE" action Return()

# ==================== ESTILOS ====================
style menu_button:
    # Text-only button (no background)
    background None
    hover_background None
    padding (0, 0)
    xalign 0.5

style menu_button_text:
    color "#f4d03f"
    size 36
    bold True
    outlines [(2, "#000000", 0, 0)]

style menu_button_secondary:
    # Secondary text-only buttons
    background None
    hover_background None
    padding (0, 0)
    xalign 0.5

style menu_button_secondary_text:
    color "#ffffff"
    size 28
    bold True
    outlines [(1, "#000000", 0, 0)]

style game_button:
    background "#4a4a6e"
    hover_background "#5a5a8e"
    padding (30, 15)
    
style game_button_text:
    color "#ffffff"
    size 18

style game_button_disabled:
    background "#2a2a3e"
    padding (20, 10)

style game_button_disabled_text:
    color "#666666"
    size 16

style stamp_button:
    background "#2a2a2a"
    hover_background "#3a3a3a"
    padding (10, 5)
    xsize 120

style stamp_button_text:
    color "#ffffff"
    size 14
    bold True

style product_button:
    background "#2a2a4e"
    hover_background "#3a3a5e"
    padding (10, 10)
    xsize 80
    ysize 60

style product_button_text:
    color "#ffffff"
    size 12
    text_align 0.5
    bold True
