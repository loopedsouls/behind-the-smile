# Behind The Smile - Lore e História do Mundo
# A história por trás da Central de Triagem da Felicidade

init python:
    # ==================== LORE DO JOGO ====================
    
    LORE = {
        "title": "A Crise do Sorriso",
        
        "background": """
O mundo como conhecíamos se despedaçou em uma fenda da realidade.

Não foi com um estrondo. Foi com um sorriso forçado.

A Grande Crise Burocrática havia transformado o trabalho em uma prisão infinita.
Filas intermináveis, documentos perdidos, sistemas que nunca funcionavam.
O povo estava à beira do colapso - e os monstros sabiam disso.

Então veio a anomalia. Silenciosa. Covarde. Perfeita.
        """,
        
        "the_weapon": """
═══════════════════════════════════════════════════
    ARQUIVO CONFIDENCIAL - NÍVEL ÔMEGA
    PROJETO: FENDA DA REALIDADE (CODINOME: "SORRISO")
═══════════════════════════════════════════════════

Uma anomalia - ninguém sabe de onde veio, os registros foram perdidos - rasgou a realidade.

Não era uma bomba. Não era um vírus comum.

Era uma FENDA.

Criada em dimensões paralelas, a Fenda da Realidade foi projetada para ser 
a arma perfeita: invisível, silenciosa, e absolutamente devastadora.

Ela atrai entidades de outras realidades. Cresce lentamente, 
estendendo seus tentáculos pela loja, trazendo monstros que se alimentam 
de negatividade enquanto mantém a consciência... parcialmente intacta.

A vítima não percebe. Não no começo.

Apenas alguns sinais: um sorriso involuntário, movimentos sutilmente 
descoordenados, uma fome inexplicável...
        """,
        
        "the_infected": """
═══════════════════════════════════════════════════
    OS MONSTROS - RELATÓRIO DE ANOMALIA #7749
═══════════════════════════════════════════════════

Os estágios da anomalia são insidiosos:

ESTÁGIO 1 - INFILTRAÇÃO (1-7 dias)
- Nenhum sinal visível na loja
- Entidades se infiltram através da fenda e migram para os clientes
- A loja continua funcionando normalmente

ESTÁGIO 2 - INTEGRAÇÃO (1-4 semanas)  
- Sorrisos involuntários em momentos inapropriados
- Leve descoordenação motora nos clientes
- Aumento do apetite por negatividade
- Os clientes ainda parecem normais... mais ou menos

ESTÁGIO 3 - DOMINAÇÃO (1-2 meses)
- A anomalia assume controle parcial dos clientes
- Impulsos violentos surgem sem explicação
- A fome se torna... específica para emoções negativas
- A consciência original ainda está lá, gritando, presa

ESTÁGIO 4 - CONSUMAÇÃO (Irreversível)
- Controle total do hospedeiro
- Única motivação: ALIMENTAR-SE DE NEGATIVIDADE
- Não há lógica. Não há razão. Não há misericórdia.
- O monstro não quer conquistar. Não quer dominar.
- Ele quer COMER emoções. Apenas isso. Sem explicação. Sem satisfação.
- Uma fome eterna que nunca pode ser saciada.
        """,
        
        "the_masks": """
═══════════════════════════════════════════════════
    A SOLUÇÃO - DECRETO DA GERÊNCIA #001-SORRISO
═══════════════════════════════════════════════════

A Gerência encontrou uma "solução".

Não uma cura. Uma MÁSCARA.

A teoria era simples: se o funcionário usasse uma máscara sorridente, 
os monstros não poderiam detectar a negatividade por trás dela.
A loja poderia "funcionar" novamente.

Mas havia um efeito colateral conveniente:

Com o sorriso permanente, o funcionário não poderia expressar 
descontentamento. Medo. Raiva. Tristeza.

A Gerência finalmente tinha sua utopia:
FUNCIONÁRIOS PERMANENTEMENTE FELIZES.

(Ou pelo menos, permanentemente parecendo felizes.)

É proibido tirar a máscara quando o cliente olhar.
É proibido mostrar emoções negativas.
É proibido questionar a Gerência.

Sorria. Sempre.
Porque se você não sorrir... como vamos saber que você não é um deles?
        """,
        
        "your_role": """
═══════════════════════════════════════════════════
    SUA FUNÇÃO - FUNCIONÁRIO #404
═══════════════════════════════════════════════════

Você é o Funcionário #404.

Seu trabalho é simples:
1. MANTENHA A MÁSCARA ao atender os clientes
2. PROCESSE seus pedidos com eficiência e um sorriso
3. REMOVA A MÁSCARA apenas para lidar com "anomalias"

As anomalias podem ser qualquer coisa: um produto fora de lugar, um alarme, 
um cliente suspeito... ou algo pior. Coisas que exigem que você veja claramente.
Coisas que exigem que você aja sem o sorriso falso atrapalhando.

Mas cuidado: se um cliente ver você sem a máscara, é GAME OVER.

Por quê? Porque se você pode tirar a máscara...
...talvez você tenha negatividade a esconder.
...talvez você não esteja sorrindo por dentro.
...talvez você seja um DELES.

E na loja da fenda, a dúvida é uma sentença de morte.

Boa sorte, Funcionário.
Mantenha o sorriso.
        """,
        
        "fragments": [
            "Os arquivos dizem que a fenda se abriu durante uma noite de turno. Ninguém acredita.",
            "Dizem que os primeiros monstros foram clientes regulares. Irônico.",
            "A anomalia não mata. Ela... substitui.",
            "Algumas pessoas tiram a máscara de propósito. Querem ser livres. Por um segundo.",
            "Os olhos são a última coisa a mudar. É assim que você sabe.",
            "A cura existe. Está trancada. 'Muito cara para produzir em massa.'",
            "O sorriso da máscara foi desenhado por um monstro. Ninguém percebeu.",
            "Alguns monstros mantêm suas memórias. Assistem enquanto seus corpos...",
            "A fome nunca para. Nunca. Mesmo depois de comer negatividade.",
            "A anomalia não pensa. Não sente. Só... consome."
        ],
        "clients": [
            {"id": "vizinha", "name": "Vizinha Solícita", "description": "Uma vizinha amigável que sempre sorri.", "line": "Boa noite, querida. Sorria, sempre sorria — deixa tudo mais fácil.", "emoji": "👩", "patience": 10},
            {"id": "corporativo", "name": "Funcionário Corporativo", "description": "Um trabalhador dedicado à empresa.", "line": "A Gerência lembra tudo. Cumpre o contrato: sorriso, produtividade, silêncio.", "emoji": "👔", "patience": 10},
            {"id": "crianca", "name": "Criança de Olhos Fundos", "description": "Uma criança com olhar estranho.", "line": "Quando você mostra seu rosto, eles... se lembram do que comem.", "emoji": "👶", "patience": 10},
            {"id": "velho", "name": "Velho Que Não Sorri", "description": "Um idoso que evita sorrir.", "line": "Antes do contrato, a loja era diferente. A máscara mantém as coisas... calmas.", "emoji": "👴", "patience": 10},
            {"id": "sorriso_esticado", "name": "O Sorriso Esticado", "description": "Alguém com um sorriso forçado.", "line": "Eles querem o real. A casca é distração. Caia a casca, e nós lembramos.", "emoji": "😀", "patience": 10}
        ]
    }

# ==================== TELA DE LORE ====================
# ==================== TELA DE LORE ====================
transform balancing:
    xalign 0.5
    yalign 0.5
    linear 1.0 xoffset 5
    linear 1.0 xoffset -5
    repeat

screen lore_screen():
    tag menu
    modal True
    
    # Fundo da loja
    add "bg store_normal"
    
    # Personagem balançando no centro
    add "customer_monstro" at balancing
    
    # Overlay escuro para legibilidade
    add Solid("#00000080")
    
    frame:
        xfill True
        yfill True
        background None
        padding (50, 50)
        
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            
            vbox:
                spacing 30
                
                # Título
                text "ARQUIVOS CLASSIFICADOS" size 48 color "#f4d03f" xalign 0.5
                text "NÍVEL DE ACESSO: TRIAGEM" size 18 color "#666666" xalign 0.5
                
                null height 30
                
                # Background
                frame:
                    background Solid("#0f0f2388")
                    padding (20, 20)
                    xfill True
                    
                    vbox:
                        text "// CONTEXTO HISTÓRICO //" size 24 color "#f4d03f"
                        null height 10
                        text LORE["background"] size 18 color "#cccccc"
                
                # A Arma
                frame:
                    background Solid("#1a0a0a88")
                    padding (20, 20)
                    xfill True
                    
                    vbox:
                        text "// A ARMA //" size 24 color "#ff4444"
                        null height 10
                        text LORE["the_weapon"] size 16 color "#aaaaaa"
                
                # Os Infectados
                frame:
                    background Solid("#0a1a0a88")
                    padding (20, 20)
                    xfill True
                    
                    vbox:
                        text "// OS INFECTADOS //" size 24 color "#44ff44"
                        null height 10
                        text LORE["the_infected"] size 16 color "#aaaaaa"
                
                # As Máscaras
                frame:
                    background Solid("#1a1a0a88")
                    padding (20, 20)
                    xfill True
                    
                    vbox:
                        text "// AS MÁSCARAS //" size 24 color "#ffff44"
                        null height 10
                        text LORE["the_masks"] size 16 color "#aaaaaa"
                
                # Sua Função
                frame:
                    background Solid("#0a0a1a88")
                    padding (20, 20)
                    xfill True
                    
                    vbox:
                        text "// SUA MISSÃO //" size 24 color "#4444ff"
                        null height 10
                        text LORE["your_role"] size 16 color "#aaaaaa"
                
                null height 50
                
                # Botão Voltar
                textbutton "[[VOLTAR AO MENU]]":
                    xalign 0.5
                    text_size 24
                    text_color "#f4d03f"
                    text_hover_color "#ffffff"
                    action Return()

# ==================== INTRO NARRATIVA ====================
label show_intro:
    scene black with fade
    
    # Estilo de terminal
    window show
    
    narrator_dystopia "O mundo como conhecíamos se despedaçou em uma fenda da realidade."
    narrator_dystopia "Não foi com um estrondo."
    narrator_dystopia "Foi com um sorriso forçado."
    
    scene black with dissolve
    pause 0.5
    
    narrator_dystopia "A Grande Crise Burocrática já havia transformado o trabalho em prisão."
    narrator_dystopia "Filas. Documentos. Sistemas quebrados."
    narrator_dystopia "O povo estava à beira do colapso."
    
    scene black with dissolve
    pause 0.5
    
    system "ALERTA DE SEGURANÇA NÍVEL ÔMEGA"
    narrator_dystopia "Então veio a anomalia. Silenciosa. Covarde."
    narrator_dystopia "Uma fenda rasgou a realidade. Ninguém sabe de onde."
    
    scene black with dissolve
    pause 0.3
    
    narrator_dystopia "Não era uma bomba."
    narrator_dystopia "Era uma FENDA."
    
    scene black with dissolve
    pause 0.5
    
    narrator_dystopia "Fenda da Realidade. Codinome: 'Sorriso'."
    narrator_dystopia "Ela atrai entidades. Cresce. Toma controle."
    narrator_dystopia "A vítima não percebe. Não no começo."
    
    narrator_dystopia "Apenas alguns sinais..."
    narrator_dystopia "Um sorriso involuntário."
    narrator_dystopia "Uma fome por negatividade."
    
    scene black with dissolve
    pause 0.5
    
    narrator_dystopia "Os monstros não querem conquistar."
    narrator_dystopia "Não querem dominar."
    narrator_dystopia "Eles querem COMER emoções negativas."
    narrator_dystopia "Sem razão. Sem satisfação. Apenas... fome."
    
    scene black with dissolve
    pause 0.5
    
    system "DECRETO DA GERÊNCIA #001-SORRISO"
    narrator_dystopia "A solução da Gerência foi simples:"
    narrator_dystopia "MÁSCARAS. Para funcionários. Sempre."
    
    narrator_dystopia "Se o funcionário sorri, os monstros não detectam a negatividade."
    narrator_dystopia "Se o funcionário sorri, não pode expressar descontentamento."
    narrator_dystopia "A Gerência finalmente tinha sua utopia."
    
    scene black with dissolve
    pause 0.5
    
    system "DESIGNAÇÃO: FUNCIONÁRIO #404"
    narrator_dystopia "Você é o Funcionário #404."
    narrator_dystopia "Seu trabalho: manter o sorriso. Processar clientes."
    narrator_dystopia "Só tire a máscara para lidar com 'anomalias'."
    
    narrator_dystopia "Mas se um cliente ver você sem máscara..."
    narrator_dystopia "...a dúvida é uma sentença de morte."
    
    scene black with dissolve
    pause 0.3
    
    system "BOA SORTE, FUNCIONÁRIO"
    system "MANTENHA O SORRISO"
    
    window hide
    
    jump main_menu
