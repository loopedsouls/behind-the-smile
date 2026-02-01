# Behind The Smile - Backgrounds e Cenários
# Substituído: agora usamos imagens estáticas para facilitar edição e substituição por assets externos.

# Backgrounds estáticos usando as imagens da pasta "mask"
image bg store_normal = im.Scale("images/mask/withoutmask.png", 1280, 720)
image bg store_alert = im.Scale("images/mask/inhandmask.png", 1280, 720)
image bg store_infected = im.Scale("images/mask/inhandmask.png", 1280, 720)
image bg store_unmasked_normal = im.Scale("images/mask/withoutmask.png", 1280, 720)
image bg store_unmasked_alert = im.Scale("images/mask/inhandmask.png", 1280, 720)
image bg store_unmasked_infected = im.Scale("images/mask/inhandmask.png", 1280, 720)

# Background do quarto do protagonista
image bg meu_quarto = im.Scale("images/mask/meuquarto.jpg", 1280, 720)

# Overlay de máscara (usa a versão com máscara para sobrepor)
image mask_overlay = im.Scale("images/mask/withmask.png", 1280, 720)

# Fundo do menu (stretched igual splashscreen)
image menu_bg = im.Scale("images/menu.png", 1280, 720)
# Variante do menu usada durante glitches (troca temporária)
image menu2_bg = im.Scale("images/menu2.png", 1280, 720)
# Placa usada como fundo da tela de pausa
image pause_plate = im.Scale("images/plate.png", 800, 480)

# Fundo sólido escuro para menus
image bg dark = Solid("#0f0f23")
image bg game_over = Solid("#1a0f0f")

