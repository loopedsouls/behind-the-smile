# Behind The Smile - Splashscreen
# Tela de abertura do jogo

# Imagem de fundo para o splash
image splash_bg = Solid("#0a0a15")
image studio_splash = im.Scale("images/splashscreen.png", 1280, 720)

# Texto com efeito de glitch
transform glitch_text:
    alpha 0.0
    linear 0.5 alpha 1.0
    pause 0.1
    xoffset 3
    pause 0.05
    xoffset -3
    pause 0.05
    xoffset 0
    pause 2.0
    linear 0.5 alpha 0.0

transform eye_blink:
    alpha 0.0
    pause 0.5
    linear 0.3 alpha 1.0
    pause 0.5
    linear 0.1 alpha 0.0
    pause 0.2
    linear 0.1 alpha 1.0
    pause 1.5
    linear 0.5 alpha 0.0

transform fade_in_out:
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 2.0
    linear 1.0 alpha 0.0

transform zoom_in:
    zoom 0.8 alpha 0.0
    linear 1.5 zoom 1.0 alpha 1.0
    pause 1.5
    linear 0.5 alpha 0.0

transform studio_fade:
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 2.5
    linear 1.0 alpha 0.0

# Tela do splash do estúdio
screen splash_studio():
    tag menu
    
    add "splash_bg"
    add "studio_splash" at studio_fade

# Tela do splashscreen
screen splash_screen():
    tag menu
    
    add "splash_bg"
    
    # Olhos de vigilância
    text "👁️" xalign 0.3 yalign 0.4 size 80 at eye_blink
    text "👁️" xalign 0.7 yalign 0.4 size 80 at eye_blink
    
    # Texto de aviso
    vbox:
        xalign 0.5
        yalign 0.7
        spacing 20
        
        text "VOCÊ ESTÁ SENDO OBSERVADO" xalign 0.5 size 28 color "#ff4444" at glitch_text
        text "Sorria." xalign 0.5 size 48 color "#f4d03f" at fade_in_out

screen splash_title():
    tag menu
    
    add "splash_bg"
    
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 15
        
        text "BEHIND THE SMILE" xalign 0.5 size 56 color "#f4d03f" outlines [(3, "#000000", 0, 0)] at zoom_in
        text "Central de Triagem da Felicidade" xalign 0.5 size 22 color "#888888" at fade_in_out

# Label do splashscreen - executa antes do menu principal
label splashscreen:
    scene black
    with fade
    
    # Splash do estúdio
    show screen splash_studio
    $ renpy.pause(4.5, hard=True)
    hide screen splash_studio
    
    # Transição para o menu
    scene black
    with fade
    
    return
