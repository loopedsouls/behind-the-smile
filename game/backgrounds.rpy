# Behind The Smile - Backgrounds e Cenários
# Substituído: agora usamos imagens estáticas para facilitar edição e substituição por assets externos.

# Backgrounds estáticos usando as imagens da pasta "mask"
image bg store_normal = im.Scale("images/mask/withoutmask.jpg", 1280, 720)
image bg store_alert = im.Scale("images/mask/inhandmask.png", 1280, 720)
image bg store_infected = im.Scale("images/mask/inhandmask.png", 1280, 720)
image bg store_unmasked_normal = im.Scale("images/mask/withoutmask.jpg", 1280, 720)
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

# ==================== UI ELEMENTS ====================
image ui_coffee_cup = im.Scale("images/store/coffee_cup.jpg", 200, 200)

# ==================== PLACEHOLDERS - Dia 1 ====================
# Cenas narrativas do Dia 1
image bg uniform_hanging = im.Scale("images/quarto/uniforme_pendurado_mascara.jpg", 1280, 720)
image bg mirror_putting_mask = Solid("#1a1a1a")  # add img mirror_putting_mask.jpg
image bg behind_counter_masked = im.Scale("images/store/behind_counter_masked.jpg", 1280, 720)
image bg street_neon_dystopia = im.Scale("images/street/street_neon_dystopia.jpg", 1280, 720)
image bg store_neon_sign = im.Scale("images/store/store_neon_sign.jpg", 1280, 720)
image bg store_entrance = im.Scale("images/store/store_entrance.jpg", 1280, 720)

# ==================== PLACEHOLDERS - Monstros ====================
image bg spider_monster = Solid("#0a0a0a")  # add img spider_monster.jpg
image monster_spider_legs = Solid("#0a0a0a")  # add img spider_monster.jpg (alias)

# ==================== PLACEHOLDERS - Dias Seguintes ====================
image bg bedroom_day2 = Solid("#1a1a1a")  # add img bedroom_more_deteriorated.jpg
image bg performance_report = Solid("#1a1a1a")  # add img performance_report_bg.jpg
image bg creepy_customer = Solid("#1a1a1a")  # add img creepy_looking_customer.jpg
image bg mysterious_note = Solid("#1a1a1a")  # add img mysterious_note.jpg
image bg corrupted_coffee = Solid("#1a1a1a")  # add img corrupted_coffee.jpg
image bg city_chaos = Solid("#1a1a1a")  # add img city_chaos.jpg
image bg fallen_masks = Solid("#1a1a1a")  # add img fallen_masks_street.jpg
image bg nightmare_surreal = Solid("#1a1a1a")  # add img nightmare_surreal.jpg
image bg waking_in_pain = Solid("#1a1a1a")  # add img waking_in_pain.jpg
image bg day4_deteriorated = Solid("#1a1a1a")  # add img day4_deteriorated_mask.jpg
image bg mask_on_nightstand = Solid("#1a1a1a")  # add img mask_on_nightstand.jpg

