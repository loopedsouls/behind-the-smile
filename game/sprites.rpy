# Behind The Smile - Sistema de Sprites Pixel Art
# Renderiza sprites usando código Python no Ren'Py

init python: 
    import pygame
    from renpy.display.displayable import Displayable
    
    # ==================== PALETA DE CORES ====================
    PALETTE = {
        "transparent": None,
        "black": "#0d1117",
        "darkGray": "#21262d",
        "gray": "#484f58",
        "lightGray": "#8b949e",
        "white": "#e6edf3",
        
        "yellow": "#f4d03f",
        "yellowDark": "#d4ac0d",
        "yellowLight": "#f9e79f",
        
        "skin": "#e8beac",
        "skinDark": "#c4a484",
        "skinLight": "#f5d5c8",
        
        "hairBrown": "#5d4037",
        "hairBlack": "#1a1a1a",
        
        "shirtBlue": "#2980b9",
        "shirtRed": "#c0392b",
        "shirtGreen": "#27ae60",
        
        "uniform": "#34495e",
        "uniformLight": "#5d6d7e",
        
        "cardboard": "#c4a77d",
        "cardboardDark": "#8b6914",
        
        "fire": "#e74c3c",
        "fireOrange": "#e67e22",
        "fireYellow": "#f1c40f",
        
        "wood": "#6d4c41",
        "woodDark": "#4e342e",
        "woodLight": "#8d6e63",
        
        "metal": "#95a5a6",
        "metalDark": "#7f8c8d",
        
        "neon": "#00ff88",
    }
    
    # Mapa de caracteres para cores
    CHAR_TO_COLOR = {
        '.': None,
        ' ': None,
        'X': PALETTE["black"],
        'D': PALETTE["darkGray"],
        'G': PALETTE["gray"],
        'L': PALETTE["lightGray"],
        'W': PALETTE["white"],
        'Y': PALETTE["yellow"],
        'y': PALETTE["yellowDark"],
        'S': PALETTE["skin"],
        's': PALETTE["skinDark"],
        'H': PALETTE["hairBrown"],
        'h': PALETTE["hairBlack"],
        'U': PALETTE["uniform"],
        'u': PALETTE["uniformLight"],
        'C': PALETTE["cardboard"],
        'c': PALETTE["cardboardDark"],
        'B': PALETTE["shirtBlue"],
        'R': PALETTE["fire"],
        'O': PALETTE["fireOrange"],
        'F': PALETTE["fireYellow"],
        'M': PALETTE["metal"],
        'm': PALETTE["metalDark"],
        'K': PALETTE["wood"],
        'k': PALETTE["woodDark"],
        'N': PALETTE["neon"],
    }
    
    # ==================== SPRITES DO JOGADOR ====================
    SPRITE_PLAYER_IDLE = [
        "....HHHH....",
        "...HHHHHH...",
        "...HHHHHH...",
        "..HSSSSSSH..",
        "..SSSSSSS...",
        "..S.SS.SS...",
        "...SSSSSS...",
        "....SSSS....",
        "....UUUU....",
        "...UUUUUU...",
        "..UUUUUUUU..",
        "..UU.UU.UU..",
        "..SS....SS..",
        "..SS....SS..",
        "..SS....SS..",
        "..kk....kk..",
    ]
    
    SPRITE_PLAYER_MASK = [
        "....HHHH....",
        "...HHHHHH...",
        "...HHHHHH...",
        "..CCCCCCCC..",
        "..CcCCCCcC..",
        "..C.CC.CC...",
        "..CCCCCCCC..",
        "..CcYYYYcC..",
        "....UUUU....",
        "...UUUUUU...",
        "..UUUUUUUU..",
        "..UU.UU.UU..",
        "..SS....SS..",
        "..SS....SS..",
        "..SS....SS..",
        "..kk....kk..",
    ]
    
    # ==================== SPRITES DE CLIENTES ====================
    SPRITE_CUSTOMERS = {
        "normal": [
            "....hhhh....",
            "...hhhhhh...",
            "...hhhhhh...",
            "..hSSSSSS...",
            "..SSSSSSSS..",
            "..S.SS.SS...",
            "...SSSSSS...",
            "....SSSS....",
            "....BBBB....",
            "...BBBBBB...",
            "..BBBBBBBB..",
            "..BB.BB.BB..",
            "..SS....SS..",
            "..SS....SS..",
            "..kk....kk..",
        ],
        "bizarre": [
            "...NNNNNN...",
            "..NNNNNNNN..",
            "..NNNNNNNN..",
            "..NSSSSSSN..",
            "..SSSSSSSS..",
            "..S.SS.SS...",
            "...S..S.S...",
            "....SSSS....",
            "...RRRRRR...",
            "..RRRRRRRR..",
            "..RR.RR.RR..",
            "..SS....SS..",
            "..SS....SS..",
            "..NN....NN..",
        ],
        "angry": [
            "....hhhh....",
            "...hhhhhh...",
            "..hhhhhhh...",
            "..hSSSSSS...",
            "..SSSSSSSS..",
            ".XS.SS.SSX..",
            "...SSSSSS...",
            "....S..S....",
            "....RRRR....",
            "...RRRRRR...",
            "..RRRRRRRR..",
            "..RR.RR.RR..",
            "..SS....SS..",
            "..SS....SS..",
            "..kk....kk..",
        ],
        "vip": [
            "....YYYY....",
            "...YYYYYY...",
            "..YYYYYYYY..",
            "..YSSSSSSY..",
            "..SSSSSSSS..",
            "..S.SS.SS...",
            "...SSSSSS...",
            "....SMMS....",
            "...DDDDDD...",
            "..DDDDDDDD..",
            "..DDYDDYDD..",
            "..DD.DD.DD..",
            "..SS....SS..",
            "..SS....SS..",
            "..XX....XX..",
        ],
        "inspector": [
            "....XXXX....",
            "...XXXXXX...",
            "..XXXXXXXX..",
            "..XSSSSSSX..",
            "..XMSSMSSX..",
            "..S.SS.SS...",
            "...SSSSSS...",
            "....SSSS....",
            "...XXXXXX...",
            "..XXXXXXXX..",
            "..XX.XX.XX..",
            "..XX.XX.XX..",
            "..SS....SS..",
            "..SS....SS..",
            "..XX....XX..",
        ],
        "robot": [
            "...MMMMMM...",
            "..MMMMMMMM..",
            "..MMMMMMMM..",
            "..MNMMMNMM..",
            "..MMMMMMMM..",
            "..M.MM.MM...",
            "...MMMMMM...",
            "....MMMM....",
            "...MMMMMM...",
            "..MMMMMMMM..",
            "..MM.MM.MM..",
            "..MMMMMMMM..",
            "..MM....MM..",
            "..MM....MM..",
            "..MM....MM..",
        ],
        "child": [
            "............",
            "....yyyy....",
            "...yyyyyy...",
            "...ySSSSSy..",
            "...SSSSSS...",
            "...S.S.SS...",
            "....SSSS....",
            "....SSSS....",
            "....BBBB....",
            "...BBBBBB...",
            "...BB.BB.B..",
            "...SS..SS...",
            "...SS..SS...",
            "...kk..kk...",
        ],
        "paranoid": [
            "....hhhh....",
            "...hhhhhh...",
            "..hhhhhhhh..",
            "..hSSSSSS...",
            "..SSSSSSSS..",
            ".WSSWSSWSS..",
            "...SSSSSS...",
            "....SSSS....",
            "....GGGG....",
            "...GGGGGG...",
            "..GGGGGGGG..",
            "..GG.GG.GG..",
            "..SS....SS..",
            "..SS....SS..",
            "..kk....kk..",
        ],
    }
    
    # ==================== SPRITES DE PERIGOS ====================
    SPRITE_DANGERS = {
        "fire": [
            "......F.....",
            ".....FFF....",
            "....FFFFF...",
            "...OOOOOOO..",
            "..OOOOOOOOO.",
            "..OROOOORO..",
            ".ORROOOORR..",
            ".RRRRRRRRR..",
            ".RRRRRRRRRR.",
            "..RRRRRRRR..",
            "...RRRRRR...",
        ],
        "alarm": [
            "....RRRR....",
            "...RRRRRR...",
            "..RRRRRRRR..",
            "..RR.RR.RR..",
            "..RRRRRRRR..",
            "..RRRRRRRR..",
            "..MMMMMMMM..",
            "...MMMMMM...",
            "....MMMM....",
            ".....MM.....",
        ],
        "monster": [
            "..XX....XX..",
            ".XXXX..XXXX.",
            ".XNNX..XNNX.",
            ".XXXX..XXXX.",
            "..XXXXXXXX..",
            ".XXXXXXXXXX.",
            ".XX.XXXX.XX.",
            ".XWXXXXXXWX.",
            ".XXXXXXXXXX.",
            "..XXXXXXXX..",
            "...XX..XX...",
            "..XX....XX..",
        ],
        "mail": [
            "....BBBB....",
            "...BBBBBB...",
            "..BBBBBBBB..",
            "..BSSSSSBB..",
            "..SSSSSSSS..",
            "..S.SS.SS...",
            "...SSSSSS...",
            "..WWWWWWWW..",
            "..WYYYYYYW..",
            "..WYYYYYYW..",
            "..WWWWWWWW..",
            "..SS....SS..",
            "..SS....SS..",
            "..BB....BB..",
        ],
        "leak": [
            "....BBBB....",
            "...B....B...",
            "..B......B..",
            "..B......B..",
            "...B....B...",
            "....BBBB....",
            ".....BB.....",
            "....BBBB....",
            "...B....B...",
            "..B......B..",
            ".B........B.",
        ],
        "blackout": [
            "....YYYY....",
            "...YYYYYY...",
            "..YYYYYYYY..",
            "..YY.YY.YY..",
            "..YYYYYYYY..",
            "...YYYYYY...",
            "....YYYY....",
            ".....YY.....",
            ".....YY.....",
            ".....XX.....",
            "....X..X....",
        ],
        "rat": [
            "............",
            "..GG....GG..",
            ".GGGG..GGGG.",
            ".GGGGGGGGGG.",
            ".GGGGGGGGGG.",
            ".GG.GGGG.GG.",
            ".GGGGGGGGGG.",
            "..GGGGGGGG..",
            "...GGGGGG...",
            "..GG....GG..",
            ".GG......GG.",
        ],
        "glitch": [
            ".NNNNNNNNNN.",
            ".N........N.",
            ".N.NNNNNN.N.",
            ".N.N....N.N.",
            ".N.N.NN.N.N.",
            ".N.N....N.N.",
            ".N.NNNNNN.N.",
            ".N........N.",
            ".NNNNNNNNNN.",
            "....NNNN....",
            "...NN..NN...",
        ],
        "phone": [
            "..MMMMMMMM..",
            ".MMMMMMMMMM.",
            ".MM......MM.",
            ".M.MMMMMM.M.",
            ".M.M....M.M.",
            ".M.M.YY.M.M.",
            ".M.M....M.M.",
            ".M.MMMMMM.M.",
            ".MM......MM.",
            ".MMMMMMMMMM.",
            "..MMMMMMMM..",
        ],
    }
    
    # Sprite do olho de vigilância
    SPRITE_EYE = [
        "..WWWW..",
        ".WWWWWW.",
        "WWWXXWWW",
        "WWXXXXWW",
        "WWWXXWWW",
        ".WWWWWW.",
        "..WWWW..",
    ]
    
    # ==================== SPRITE DA PORTA ====================
    SPRITE_DOOR_CLOSED = [
        "KKKKKKKKKKKKKKKKKKKK",
        "KkkkkkkkkkkkkkkkkkKK",
        "Kk................kK",
        "Kk................kK",
        "Kk................kK",
        "Kk................kK",
        "Kk......YYYY......kK",
        "Kk......YYYY......kK",
        "Kk................kK",
        "Kk................kK",
        "Kk................kK",
        "Kk..........MM....kK",
        "Kk..........MM....kK",
        "Kk................kK",
        "Kk................kK",
        "Kk................kK",
        "Kk................kK",
        "Kk................kK",
        "KkkkkkkkkkkkkkkkkkKK",
        "KKKKKKKKKKKKKKKKKKKK",
    ]
    
    SPRITE_DOOR_OPEN = [
        "KKKKKK...............",
        "Kkkkk................",
        "Kk...................",
        "Kk...................",
        "Kk...................",
        "Kk...................",
        "Kk.YYYY..............",
        "Kk.YYYY..............",
        "Kk...................",
        "Kk...................",
        "Kk...................",
        "Kk.MM................",
        "Kk.MM................",
        "Kk...................",
        "Kk...................",
        "Kk...................",
        "Kk...................",
        "Kk...................",
        "Kkkkk................",
        "KKKKKK...............",
    ]
    
    # ==================== FUNÇÕES DE RENDERIZAÇÃO ====================
    def hex_to_rgb(hex_color):
        """Converte cor hex para RGB"""
        if hex_color is None:
            return None
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def create_sprite_surface(sprite_data, pixel_size=4):
        """Cria uma superfície Pygame a partir de dados de sprite"""
        height = len(sprite_data)
        width = max(len(row) for row in sprite_data)
        
        surface = pygame.Surface((width * pixel_size, height * pixel_size), pygame.SRCALPHA)
        surface.fill((0, 0, 0, 0))
        
        for y, row in enumerate(sprite_data):
            for x, char in enumerate(row):
                color = CHAR_TO_COLOR.get(char)
                if color:
                    rgb = hex_to_rgb(color)
                    if rgb:
                        pygame.draw.rect(surface, rgb + (255,), 
                                       (x * pixel_size, y * pixel_size, pixel_size, pixel_size))
        
        return surface
    
    class PixelSprite(Displayable):
        """Displayable customizado para sprites pixel art"""
        
        def __init__(self, sprite_data, pixel_size=4, **kwargs):
            super(PixelSprite, self).__init__(**kwargs)
            self.sprite_data = sprite_data
            self.pixel_size = pixel_size
            self.surface = None
        
        def render(self, width, height, st, at):
            if self.surface is None:
                self.surface = create_sprite_surface(self.sprite_data, self.pixel_size)
            
            render = renpy.Render(self.surface.get_width(), self.surface.get_height())
            render.blit(self.surface, (0, 0))
            return render
        
        def visit(self):
            return []
    
    def get_player_sprite(with_mask=True, pixel_size=6):
        """Retorna o sprite do jogador"""
        sprite_data = SPRITE_PLAYER_MASK if with_mask else SPRITE_PLAYER_IDLE
        return PixelSprite(sprite_data, pixel_size)
    
    def get_customer_sprite(customer_id, pixel_size=6):
        """Retorna o sprite de um cliente"""
        sprite_data = SPRITE_CUSTOMERS.get(customer_id, SPRITE_CUSTOMERS["normal"])
        return PixelSprite(sprite_data, pixel_size)
    
    def get_danger_sprite(danger_id, pixel_size=6):
        """Retorna o sprite de um perigo"""
        sprite_data = SPRITE_DANGERS.get(danger_id, SPRITE_DANGERS["alarm"])
        return PixelSprite(sprite_data, pixel_size)
    
    def get_eye_sprite(pixel_size=4):
        """Retorna o sprite do olho de vigilância"""
        return PixelSprite(SPRITE_EYE, pixel_size)

# ==================== IMAGENS DINÂMICAS ====================
image player_idle = PixelSprite(SPRITE_PLAYER_IDLE, 6)
# image player_mask removed (canvas-based masked sprite eliminated)

# Customer images replaced by client PNGs (1.png is the main asset)

# Imagens dos clientes atualizadas conforme arquivos reais
image customer_monstro = "images/client/monstro.png"
image customer_alien = "images/client/alien.png"
image customer_he = "images/client/he.png"
image customer_she = "images/client/she.png"

# Fallbacks para tipos não mapeados
image customer_normal = "images/client/monstro.png"
image customer_bizarre = "images/client/alien.png"
image customer_angry = "images/client/he.png"
image customer_vip = "images/client/she.png"
image customer_inspector = "images/client/monstro.png"
image customer_robot = "images/client/alien.png"
image customer_child = "images/client/he.png"
image customer_paranoid = "images/client/she.png"

image danger_fire = PixelSprite(SPRITE_DANGERS["fire"], 6)
image danger_alarm = PixelSprite(SPRITE_DANGERS["alarm"], 6)
image danger_monster = PixelSprite(SPRITE_DANGERS["monster"], 6)
image danger_mail = PixelSprite(SPRITE_DANGERS["mail"], 6)
image danger_leak = PixelSprite(SPRITE_DANGERS["leak"], 6)
image danger_blackout = PixelSprite(SPRITE_DANGERS["blackout"], 6)
image danger_rat = PixelSprite(SPRITE_DANGERS["rat"], 6)
image danger_glitch = PixelSprite(SPRITE_DANGERS["glitch"], 6)
image danger_phone = PixelSprite(SPRITE_DANGERS["phone"], 6)

image surveillance_eye = PixelSprite(SPRITE_EYE, 4)

# Porta removida — displayables `door_*` eliminados

# ==================== ANIMAÇÕES ====================

# Posição da porta
# transform door_idle removed (porta eliminada)

# Entrada do cliente: agora aparece com fade no centro (sem animação linear)
transform customer_fade:
    anchor (0.5, 1.0)
    xpos 540 ypos 640
    zoom 0.5
    alpha 0.0
    linear 0.4 alpha 1.0

# Cliente parado no centro
transform customer_idle:
    anchor (0.5, 1.0)
    xpos 540 ypos 640
    zoom 0.5
    
# Cliente saindo
transform customer_leave:
    anchor (0.5, 1.0)
    ypos 570
    xpos 640
    linear 1.0 xpos 1100
    linear 0.2 alpha 0.0

# Animação de andar (balanço das pernas)
transform walking:
    block:
        linear 0.12 yoffset -4 rotate 2
        linear 0.12 yoffset 0 rotate 0
        linear 0.12 yoffset -4 rotate -2
        linear 0.12 yoffset 0 rotate 0
        repeat

# Respiração sutil quando parado
transform idle_breathing:
    block:
        linear 1.0 yoffset -2
        linear 1.0 yoffset 0
        repeat

# transform player_breathing removed — jogador oculto no HUD

# player_center_fade removed (player não deve ficar translúcido)
