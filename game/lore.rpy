# Behind The Smile - Lore e História do Mundo
# A história por trás da Central de Triagem da Felicidade

init python:
    # ==================== LORE DO JOGO ====================
    
    LORE = {
        "title": "A Crise do Sorriso",
        
        "background": """
O mundo como conhecíamos acabou em 2031.

Não foi com um estrondo. Foi com um sorriso.

A Grande Crise Burocrática já havia esgotado os recursos de todas as nações. 
Filas intermináveis, documentos perdidos, sistemas que nunca funcionavam. 
O povo estava à beira do colapso - e os governos sabiam disso.

Então veio a guerra. Silenciosa. Covarde. Perfeita.
        """,
        
        "the_weapon": """
═══════════════════════════════════════════════════
    ARQUIVO CONFIDENCIAL - NÍVEL ÔMEGA
    PROJETO: CORDYCEPS-7 (CODINOME: "SORRISO")
═══════════════════════════════════════════════════

Um país - ninguém sabe mais qual, os registros foram apagados - liberou algo.

Não era uma bomba. Não era um vírus comum.

Era um FUNGO.

Engenheirado em laboratórios secretos, o Cordyceps-7 foi projetado para ser 
a arma perfeita: invisível, silenciosa, e absolutamente devastadora.

O fungo se aloja no sistema nervoso central. Cresce lentamente, 
estendendo seus filamentos pelo cérebro, tomando controle motor 
enquanto mantém a consciência... parcialmente intacta.

A vítima não percebe. Não no começo.

Apenas alguns sinais: um sorriso involuntário, movimentos sutilmente 
descoordenados, uma fome inexplicável...
        """,
        
        "the_infected": """
═══════════════════════════════════════════════════
    OS INFECTADOS - RELATÓRIO MÉDICO #7749
═══════════════════════════════════════════════════

Os estágios da infecção são insidiosos:

ESTÁGIO 1 - INFILTRAÇÃO (1-7 dias)
- Nenhum sintoma visível
- Esporos se alojam nos pulmões e migram para o cérebro
- A pessoa continua sua vida normal

ESTÁGIO 2 - INTEGRAÇÃO (1-4 semanas)  
- Sorrisos involuntários em momentos inapropriados
- Leve descoordenação motora
- Aumento do apetite
- A pessoa ainda é "ela mesma"... mais ou menos

ESTÁGIO 3 - DOMINAÇÃO (1-2 meses)
- O fungo assume controle parcial
- Impulsos violentos surgem sem explicação
- A fome se torna... específica
- A consciência original ainda está lá, gritando, presa

ESTÁGIO 4 - CONSUMAÇÃO (Irreversível)
- Controle total do hospedeiro
- Única motivação: ALIMENTAR-SE
- Não há lógica. Não há razão. Não há misericórdia.
- O monstro não quer conquistar. Não quer dominar.
- Ele quer COMER. Apenas isso. Sem explicação. Sem satisfação.
- Uma fome eterna que nunca pode ser saciada.
        """,
        
        "the_masks": """
═══════════════════════════════════════════════════
    A SOLUÇÃO - DECRETO FEDERAL #001-SORRISO
═══════════════════════════════════════════════════

O governo encontrou uma "solução".

Não uma cura. Uma MÁSCARA.

A teoria era simples: se todos usassem máscaras sorridentes, 
ninguém poderia identificar os infectados pelo sorriso involuntário.
A sociedade poderia "funcionar" novamente.

Mas havia um efeito colateral conveniente:

Com todos sorrindo o tempo todo, ninguém poderia expressar 
descontentamento. Medo. Raiva. Tristeza.

A burocracia finalmente tinha sua utopia:
CIDADÃOS PERMANENTEMENTE FELIZES.

(Ou pelo menos, permanentemente parecendo felizes.)

É proibido tirar a máscara em público.
É proibido mostrar emoções negativas.
É proibido questionar o sistema.

Sorria. Sempre.
Porque se você não sorrir... como vamos saber que você não é um deles?
        """,
        
        "your_role": """
═══════════════════════════════════════════════════
    SUA FUNÇÃO - AGENTE DE TRIAGEM
═══════════════════════════════════════════════════

Você é um Agente de Triagem da Felicidade.

Seu trabalho é simples:
1. MANTENHA A MÁSCARA ao atender os cidadãos
2. PROCESSE seus pedidos com eficiência e um sorriso
3. REMOVA A MÁSCARA apenas para lidar com "anomalias"

As anomalias podem ser qualquer coisa: um incêndio, um vazamento, 
um alarme... ou algo pior. Coisas que exigem que você veja claramente.
Coisas que exigem que você aja sem o sorriso falso atrapalhando.

Mas cuidado: se um cidadão ver você sem a máscara, é GAME OVER.

Por quê? Porque se você pode tirar a máscara...
...talvez você não tenha nada a esconder.
...talvez você não esteja sorrindo por baixo.
...talvez você seja um DELES.

E no mundo pós-Cordyceps, a dúvida é uma sentença de morte.

Boa sorte, Agente.
Mantenha o sorriso.
        """,
        
        "fragments": [
            "Os arquivos dizem que a guerra durou 3 dias. Ninguém acredita.",
            "Dizem que os primeiros infectados foram políticos. Irônico.",
            "O fungo não mata. Ele... substitui.",
            "Algumas pessoas tiram a máscara de propósito. Querem ser livres. Por um segundo.",
            "Os olhos são a última coisa a mudar. É assim que você sabe.",
            "A cura existe. Está trancada. 'Muito cara para produzir em massa.'",
            "O sorriso da máscara foi desenhado por um infectado. Ninguém percebeu.",
            "Alguns infectados mantêm suas memórias. Assistem enquanto seus corpos...",
            "A fome nunca para. Nunca. Mesmo depois de comer.",
            "O fungo não pensa. Não sente. Só... consome."
        ],
        "clients": [
            {"id": "vizinha", "name": "Vizinha Solícita", "line": "Boa noite, querida. Sorria, sempre sorria — deixa tudo mais fácil.", "emoji": "👩"},
            {"id": "corporativo", "name": "Funcionário Corporativo", "line": "A Gerência lembra tudo. Cumpre o contrato: sorriso, produtividade, silêncio.", "emoji": "👔"},
            {"id": "crianca", "name": "Criança de Olhos Fundos", "line": "Quando você mostra seu rosto, eles... se lembram do que comem.", "emoji": "👶"},
            {"id": "velho", "name": "Velho Que Não Sorri", "line": "Antes do contrato, a loja era diferente. A máscara mantém as coisas... calmas.", "emoji": "👴"},
            {"id": "sorriso_esticado", "name": "O Sorriso Esticado", "line": "Eles querem o real. A casca é distração. Caia a casca, e nós lembramos.", "emoji": "😀"}
        ]
    }

# ==================== TELA DE LORE ====================
screen lore_screen():
    tag menu
    modal True
    
    add Solid("#0a0a15")
    
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
                        text LORE["the_weapon"] size 16 color "#aaaaaa" font "DejaVuSansMono.ttf"
                
                # Os Infectados
                frame:
                    background Solid("#0a1a0a88")
                    padding (20, 20)
                    xfill True
                    
                    vbox:
                        text "// OS INFECTADOS //" size 24 color "#44ff44"
                        null height 10
                        text LORE["the_infected"] size 16 color "#aaaaaa" font "DejaVuSansMono.ttf"
                
                # As Máscaras
                frame:
                    background Solid("#1a1a0a88")
                    padding (20, 20)
                    xfill True
                    
                    vbox:
                        text "// AS MÁSCARAS //" size 24 color "#ffff44"
                        null height 10
                        text LORE["the_masks"] size 16 color "#aaaaaa" font "DejaVuSansMono.ttf"
                
                # Sua Função
                frame:
                    background Solid("#0a0a1a88")
                    padding (20, 20)
                    xfill True
                    
                    vbox:
                        text "// SUA MISSÃO //" size 24 color "#4444ff"
                        null height 10
                        text LORE["your_role"] size 16 color "#aaaaaa" font "DejaVuSansMono.ttf"
                
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
    
    narrator_dystopia "O mundo como conhecíamos acabou em 2031."
    narrator_dystopia "Não foi com um estrondo."
    narrator_dystopia "Foi com um sorriso."
    
    scene black with dissolve
    pause 0.5
    
    narrator_dystopia "A Grande Crise Burocrática já havia esgotado tudo."
    narrator_dystopia "Filas. Documentos. Sistemas quebrados."
    narrator_dystopia "O povo estava à beira do colapso."
    
    scene black with dissolve
    pause 0.5
    
    system "ALERTA DE SEGURANÇA NÍVEL ÔMEGA"
    narrator_dystopia "Então veio a guerra. Silenciosa. Covarde."
    narrator_dystopia "Um país liberou algo. Ninguém sabe mais qual."
    
    scene black with dissolve
    pause 0.3
    
    narrator_dystopia "Não era uma bomba."
    narrator_dystopia "Era um FUNGO."
    
    scene black with dissolve
    pause 0.5
    
    narrator_dystopia "Cordyceps-7. Codinome: 'Sorriso'."
    narrator_dystopia "Ele se aloja no cérebro. Cresce. Toma controle."
    narrator_dystopia "A vítima não percebe. Não no começo."
    
    narrator_dystopia "Apenas alguns sinais..."
    narrator_dystopia "Um sorriso involuntário."
    narrator_dystopia "Uma fome inexplicável."
    
    scene black with dissolve
    pause 0.5
    
    narrator_dystopia "Os infectados não querem conquistar."
    narrator_dystopia "Não querem dominar."
    narrator_dystopia "Eles querem COMER."
    narrator_dystopia "Sem razão. Sem satisfação. Apenas... fome."
    
    scene black with dissolve
    pause 0.5
    
    system "DECRETO FEDERAL #001-SORRISO"
    narrator_dystopia "A solução do governo foi simples:"
    narrator_dystopia "MÁSCARAS. Para todos. Sempre."
    
    narrator_dystopia "Se todos sorriem, ninguém pode identificar os infectados."
    narrator_dystopia "Se todos sorriem, ninguém pode expressar descontentamento."
    narrator_dystopia "A burocracia finalmente tinha sua utopia."
    
    scene black with dissolve
    pause 0.5
    
    system "DESIGNAÇÃO: AGENTE DE TRIAGEM"
    narrator_dystopia "Você é um Agente de Triagem da Felicidade."
    narrator_dystopia "Seu trabalho: manter o sorriso. Processar cidadãos."
    narrator_dystopia "Só tire a máscara para lidar com 'anomalias'."
    
    narrator_dystopia "Mas se um cidadão ver você sem máscara..."
    narrator_dystopia "...a dúvida é uma sentença de morte."
    
    scene black with dissolve
    pause 0.3
    
    system "BOA SORTE, AGENTE"
    system "MANTENHA O SORRISO"
    
    window hide
    
    jump main_menu
