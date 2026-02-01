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
        # VERIFICAÇÃO CRÍTICA: Máscara deve estar ativa para spawn de cliente
        if not store.mask_on:
            store.game_state = "game_over"
            store.game_over_reason = "mask_off_spawn"
            renpy.notify("CONTRATO VIOLADO - Cliente apareceu sem máscara ativa!")
            renpy.notify("A Gerência não tolera exposição.")
            renpy.jump("game_over")
            return
        
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
        # Manter máscara ativa (já está ativa da verificação acima)

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
    $ current_day = 1
    
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
    
    # Começar narrativa do Dia 1
    jump day_1_intro

label game_loop:
    # Mostrar HUD e aguardar interação
    show screen game_hud
    
    # Loop principal - aguarda ações do jogador
    $ renpy.pause(0.1, hard=True)
    
    # Checar spawn/saída de clientes
    $ now = pytime.time()
    if current_customer is None and now >= next_customer_time:
        # Adicionar delay extra para evitar spawns muito próximos
        $ time_since_last_spawn = now - getattr(store, 'last_spawn_time', 0)
        if time_since_last_spawn >= 8.0:  # Mínimo 8 segundos entre spawns
            $ spawn_customer()
            $ store.last_spawn_time = now
        else:
            # Reagendar para daqui a pouco
            $ store.next_customer_time = now + (8.0 - time_since_last_spawn)
    if current_customer is not None and customer_leave_time and now >= customer_leave_time:
        $ renpy.notify(current_customer['name'] + " saiu.")
        $ current_customer = None
    
    # Verificar estado do jogo
    if game_state == "game_over":
        jump game_over
    elif game_state == "day_end":
        # Dia terminou - retornar para continuar a narrativa
        return
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

# ==================== CAPÍTULOS NARRATIVOS ====================

label day_1_intro:
    $ current_day = 1
    window show
    scene bg meu_quarto
    
    "O alarme toca às 6:00 da manhã. Meu apartamento é um cubículo mínimo, com paredes de concreto cinza e uma única janela que dá para um beco escuro."
    
    "Levanto-me da cama estreita, sentindo o peso da noite anterior. Os olhos queimam, as mãos tremem ligeiramente. É o meu primeiro dia como Funcionário #404."
    
    "A Gerência me recrutou há uma semana. Disseram que eu era 'perfeito para o cargo' - alguém que já estava quebrado o suficiente para não questionar as regras."
    
    "Visto o uniforme: calças pretas, camisa branca engomada, gravata fina. E a máscara. Aquela máscara de sorriso amarelo brilhante que nunca sai do meu rosto durante o expediente."
    
    "O espelho reflete um estranho. Olheiras profundas, pele pálida, olhos vazios. Mas a máscara... a máscara sorri eternamente."
    
    gerente "Funcionário #404. Relatório matinal."
    
    gerente "Eficiência: 0%%. Felicidade: 0%%. Conformidade: 0%%."
    
    gerente "Hoje começa seu treinamento. Mantenha o sorriso. Atenda os clientes. Não falhe."
    
    "Saio para a rua. A cidade é um labirinto de prédios altos e ruas iluminadas por neon distorcido. Pessoas caminham como autômatos, todas com suas máscaras sorridentes."
    
    "Chego à loja de conveniência. A placa pisca: 'SORRIA - VOCÊ ESTÁ SENDO OBSERVADO'."
    
    "Entro. O ar condicionado zumbe como um inseto gigante. As prateleiras estão impecavelmente arrumadas. O balcão brilha sob as luzes fluorescentes."
    
    "É hora de começar o turno."
    
    window hide
    jump day_1_gameplay

label day_1_gameplay:
    # Gameplay do Dia 1 - clientes normais, dificuldade baixa
    scene bg store_normal
    $ difficulty_multiplier = 1.0
    $ time_left = GameConfig.GAME_DURATION
    $ game_state = "playing"
    
    call game_loop()
    
    # Após o turno
    window show
    scene bg store_normal
    
    gerente "Funcionário #404. Relatório do turno."
    
    gerente "Clientes atendidos: [customers_served]. Pontuação: [score]."
    
    if score >= 50:
        gerente "Desempenho aceitável. Continue assim."
    else:
        gerente "Desempenho insuficiente. Melhore ou enfrente as consequências."
    
    "Volto para casa exausto. A máscara pesa no meu rosto como chumbo. Meus braços doem de segurá-la por tanto tempo."
    
    "Mas... algo estranho aconteceu hoje. Um cliente olhou para mim de um jeito diferente. Não com raiva ou impaciência. Com... reconhecimento?"
    
    "Durmo inquieto, sonhando com sorrisos que se transformam em gritos."
    
    window hide
    jump day_2_intro

label day_2_intro:
    $ current_day = 2
    window show
    scene bg meu_quarto
    
    "Dia 2. O alarme toca novamente. Meu corpo dói como se tivesse corrido uma maratona ontem."
    
    "Olho no espelho. As olheiras estão piores. A máscara sorri, mas meus olhos... eles traem tudo."
    
    "A Gerência deixou uma mensagem no meu terminal: 'Aumente sua eficiência. Clientes reportaram lentidão.'"
    
    "No caminho para o trabalho, vejo mais pessoas nas ruas. Todas mascaradas, todas sorrindo. É como se a cidade inteira estivesse participando de uma piada cósmica."
    
    "Chego à loja. Hoje parece mais movimentada. Os clientes chegam em ondas, cada um com sua própria máscara de sorriso."
    
    "Um pensamento me ocorre: quantos deles são reais? Quantos são... outra coisa?"
    
    gerente "Funcionário #404. Comece o turno. Eficiência esperada: 15%% acima do dia anterior."
    
    window hide
    jump day_2_gameplay

label day_2_gameplay:
    # Gameplay do Dia 2 - dificuldade média, mais clientes
    scene bg store_normal
    $ difficulty_multiplier = 1.2
    $ time_left = GameConfig.GAME_DURATION
    $ game_state = "playing"
    
    call game_loop()
    
    window show
    
    gerente "Relatório do Dia 2."
    
    gerente "Melhoria detectada. Continue o progresso."
    
    "Hoje foi mais intenso. Os clientes pareciam mais impacientes, mais... observadores. Um deles mencionou algo sobre 'protocolos' e 'conformidade'."
    
    "Minhas mãos tremem mais agora. A máscara pesa como uma âncora. Mas não posso tirá-la. Nunca durante o expediente."
    
    "À noite, recebo uma ligação anônima. Uma voz distorcida sussurra: 'Eles sabem quem você é. Fuja enquanto pode.'"
    
    "Desligo o telefone. Paranóia? Ou aviso legítimo?"
    
    "Durmo com a máscara ao lado da cama, sorrindo para mim no escuro."
    
    window hide
    jump day_3_intro

label day_3_intro:
    $ current_day = 3
    window show
    scene bg meu_quarto
    
    "Dia 3. Acordo suando frio. O telefone tocou a noite toda com chamadas silenciosas."
    
    "A mensagem da Gerência hoje é mais direta: 'Não questione. Apenas obedeça.'"
    
    "No caminho para o trabalho, noto que algumas pessoas nas ruas não estão mais sorrindo. Suas máscaras pendem frouxas, revelando olhares vazios."
    
    "Será que estou imaginando coisas? Ou a cidade está... mudando?"
    
    "Na loja, o ar parece mais pesado hoje. As luzes fluorescentes piscam ocasionalmente, lançando sombras estranhas."
    
    "Um cliente chega primeiro - uma mulher com uniforme de supervisora. Ela me olha de um jeito que me faz arrepiar."
    
    gerente "Funcionário #404. Hoje testaremos sua lealdade. Não decepcione."
    
    window hide
    jump day_3_gameplay

label day_3_gameplay:
    # Gameplay do Dia 3 - dificuldade alta, clientes especiais aparecem
    scene bg store_normal
    $ difficulty_multiplier = 1.5
    $ time_left = GameConfig.GAME_DURATION
    $ game_state = "playing"
    
    call game_loop()
    
    window show
    
    gerente "Dia 3 concluído. Lealdade confirmada."
    
    "Hoje foi... diferente. A supervisora me deu instruções específicas. 'Mantenha a fachada', ela disse. 'A verdade é relativa.'"
    
    "Os clientes pareciam mais agressivos, mais exigentes. Um deles tentou arrancar minha máscara. Graças aos céus consegui mantê-la no lugar."
    
    "À noite, encontro um bilhete na minha porta: 'A Gerência não é o que parece. Procure a verdade nos arquivos.'"
    
    "Que arquivos? Onde?"
    
    "Durmo com um olho aberto, a máscara sempre por perto."
    
    window hide
    jump day_4_intro

label day_4_intro:
    $ current_day = 4
    window show
    scene bg meu_quarto
    
    "Dia 4. O mundo parece mais frágil agora. Como se uma rachadura invisível estivesse se abrindo na realidade."
    
    "A Gerência mandou uma atualização: 'Protocolo de Emergência ativado. Aumente vigilância.'"
    
    "Nas ruas, vejo pessoas discutindo em voz baixa. Máscaras caídas revelam expressões de medo e confusão."
    
    "Será que estou causando isso? Ou sou apenas uma peça no quebra-cabeça?"
    
    "Na loja, o scanner de produtos começa a falhar. Os carimbos aparecem borrados. O café tem gosto de metal."
    
    "Um inspetor chega primeiro hoje. Seus olhos perfuram através da máscara."
    
    gerente "Funcionário #404. Hoje revelaremos segredos. Esteja preparado."
    
    window hide
    jump day_4_gameplay

label day_4_gameplay:
    # Gameplay do Dia 4 - dificuldade muito alta, anomalias
    scene bg store_normal
    $ difficulty_multiplier = 1.8
    $ time_left = GameConfig.GAME_DURATION
    $ game_state = "playing"
    
    call game_loop()
    
    window show
    
    gerente "Dia 4. Segredos revelados."
    
    "O inspetor me contou coisas... coisas que não deveriam ser ditas. Sobre a 'verdadeira natureza' da Gerência."
    
    "Clientes chegam em hordas agora. Alguns parecem... errados. Suas formas mudam quando não estou olhando diretamente."
    
    "Minhas mãos tremem incontrolavelmente. A máscara escorrega. Mas não posso tirá-la. Não agora."
    
    "À noite, os sonhos vêm. Sonhos com rostos sem olhos, sorrisos eternos, e uma voz que sussurra meu nome verdadeiro."
    
    "Preciso descobrir a verdade. Antes que seja tarde demais."
    
    window hide
    jump day_5_intro

label day_5_intro:
    $ current_day = 5
    window show
    scene bg meu_quarto
    
    "Dia 5. O último dia. Ou o primeiro do fim."
    
    "A cidade está em caos. Máscaras caídas nas ruas, pessoas gritando, luzes piscando erraticamente."
    
    "A Gerência não mandou mensagem hoje. Talvez saibam que descobri tudo."
    
    "Entro na loja pela última vez. O ar está carregado de eletricidade estática. Os produtos nas prateleiras... se movem sozinhos?"
    
    "Um robô chega primeiro. Seus olhos vermelhos piscam com dados que não quero ver."
    
    gerente "Funcionário #404. Hoje termina tudo. Escolha seu lado."
    
    window hide
    jump day_5_gameplay

label day_5_gameplay:
    # Gameplay do Dia 5 - dificuldade máxima, clímax
    $ difficulty_multiplier = 2.0
    $ time_left = GameConfig.GAME_DURATION
    $ game_state = "playing"
    
    call game_loop()
    
    window show
    
    "O turno termina. Mas nada acabou."
    
    "Os clientes... eles eram todos parte disso. Parte da ilusão."
    
    "A Gerência... não é humana. Nunca foi."
    
    "E eu? O que sou agora?"
    
    "A máscara cai do meu rosto. Pela primeira vez em dias, vejo meu reflexo verdadeiro."
    
    "Não há sorriso. Apenas determinação."
    
    "É hora de acabar com isso."
    
    window hide
    jump ending

label ending:
    window show
    scene black
    
    "Você completou os 5 dias como Funcionário #404."
    
    "Mas a história não termina aqui..."
    
    "A Gerência sempre precisa de novos funcionários."
    
    "E você... você aprendeu a sorrir de verdade?"
    
    window hide
    jump main_menu

# ==================== SISTEMA DE RETRY ====================

label retry_current_day:
    # Reinicia apenas o dia atual, mantendo progresso
    $ game_state = "playing"
    $ time_left = GameConfig.GAME_DURATION
    $ mask_on = True
    $ arm_stability = 100.0
    $ mask_lower_count = 0
    
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
    
    # Manter current_day e dificuldade
    # Pular para o gameplay do dia atual
    if current_day == 1:
        jump day_1_gameplay
    elif current_day == 2:
        jump day_2_gameplay
    elif current_day == 3:
        jump day_3_gameplay
    elif current_day == 4:
        jump day_4_gameplay
    elif current_day == 5:
        jump day_5_gameplay
    else:
        # Fallback para dia 1 se algo der errado
        $ current_day = 1
        jump day_1_gameplay

label game_over:
    hide screen game_hud
    window hide
    
    call screen game_over_screen()
    
    return
