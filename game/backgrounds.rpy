# Behind The Smile - Backgrounds e Cenários
# Gera os backgrounds do jogo dinamicamente

init -1 python:
    import pygame
    
    def bg_hex_to_rgb(hex_color):
        """Converte cor hex para RGB"""
        if hex_color is None:
            return (0, 0, 0)
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

init python:
    
    class StoreBackground(renpy.Displayable):
        """Background da loja gerado proceduralmente"""
        
        def __init__(self, **kwargs):
            super(StoreBackground, self).__init__(**kwargs)
            self.cached_render = None
            self.cached_size = (0, 0)
        
        def render(self, width, height, st, at):
            # Usar tamanho fixo para 16:9
            w = 1280
            h = 720
            
            if self.cached_render is None or self.cached_size != (w, h):
                self.cached_size = (w, h)
                self.cached_render = self.create_render(w, h)
            
            return self.cached_render
        
        def create_render(self, w, h):
            """Cria o render da loja"""
            render = renpy.Render(w, h)
            canvas = render.canvas()
            
            # Cor da parede
            canvas.rect("#1a1a2e", (0, 0, w, h))
            
            # Linhas da parede (tijolos)
            for y in range(0, h, 20):
                canvas.line("#252540", (0, y), (w, y))
                offset = 50 if (y // 20) % 2 == 0 else 0
                for x in range(offset, w, 100):
                    canvas.line("#252540", (x, y), (x, y + 20))
            
            # Piso
            floor_y = int(h * 0.75)
            canvas.rect("#2d2d44", (0, floor_y, w, h - floor_y))
            
            # Linhas do piso
            for x in range(0, w, 50):
                canvas.line("#3d3d55", (x, floor_y), (x, h))
            for y in range(floor_y, h, 35):
                canvas.line("#3d3d55", (0, y), (w, y))
            
            # Prateleiras
            shelf_positions = [0.15, 0.30, 0.45]
            for shelf_pct in shelf_positions:
                shelf_y = int(h * shelf_pct)
                for x in range(0, w, 150):
                    # Prateleira
                    canvas.rect("#6d4c41", (x + 10, shelf_y, 120, 8))
                    canvas.rect("#4e342e", (x + 10, shelf_y + 6, 120, 2))
                    
                    # Itens na prateleira
                    item_colors = ["#e74c3c", "#2980b9", "#27ae60", "#f4d03f"]
                    for i in range(5):
                        item_x = x + 20 + i * 22
                        item_color = item_colors[(x // 150 + i) % len(item_colors)]
                        item_height = 15 + (i % 3) * 5
                        canvas.rect(item_color, (item_x, shelf_y - item_height, 15, item_height))
            
            # Balcão
            counter_y = int(h * 0.68)
            canvas.rect("#6d4c41", (0, counter_y, w, 25))
            canvas.rect("#8d6e63", (0, counter_y, w, 4))
            
            # Caixa registradora
            register_x = int(w * 0.08)
            register_y = int(h * 0.58)
            canvas.rect("#95a5a6", (register_x, register_y, 60, 50))
            canvas.rect("#7f8c8d", (register_x + 5, register_y + 5, 50, 25))
            canvas.rect("#f4d03f", (register_x + 10, register_y + 35, 40, 10))
            
            # Luzes do teto
            num_lights = 5
            light_spacing = w // (num_lights + 1)
            
            for i in range(1, num_lights + 1):
                light_x = light_spacing * i
                # Fio
                canvas.line("#95a5a6", (light_x, 0), (light_x, 30))
                # Luz
                canvas.rect("#95a5a6", (light_x - 20, 30, 40, 15))
                canvas.rect("#f4d03f", (light_x - 15, 40, 30, 8))
            
            return render
        
        def visit(self):
            return []
    
    class MaskOverlay(renpy.Displayable):
        """Overlay da máscara de papelão"""
        
        def __init__(self, **kwargs):
            super(MaskOverlay, self).__init__(**kwargs)
            self.cached_render = None
        
        def render(self, width, height, st, at):
            w = 1280
            h = 720
            
            if self.cached_render is None:
                self.cached_render = self.create_render(w, h)
            
            return self.cached_render
        
        def create_render(self, w, h):
            """Cria o render da máscara"""
            render = renpy.Render(w, h)
            canvas = render.canvas()
            
            border_top = int(h * 0.12)
            border_bottom = int(h * 0.15)
            border_side = int(w * 0.12)
            
            # Desenhar bordas de papelão
            canvas.rect("#c4a77d", (0, 0, w, border_top))
            canvas.rect("#c4a77d", (0, h - border_bottom, w, border_bottom))
            canvas.rect("#c4a77d", (0, 0, border_side, h))
            canvas.rect("#c4a77d", (w - border_side, 0, border_side, h))
            
            # Textura
            for i in range(30):
                x = (i * 17) % border_side
                y = (i * 31) % h
                canvas.rect("#8b6914", (x, y, 8, 3))
                canvas.rect("#8b6914", (w - border_side + x, y, 8, 3))
            
            # Sorriso (linha curva simples)
            center_x = w // 2
            for i in range(-50, 51):
                x = center_x + i * 3
                y = h - border_bottom // 2 + abs(i) // 2
                canvas.rect("#f4d03f", (x - 2, y - 2, 5, 5))
            
            return render
        
        def visit(self):
            return []

# ==================== IMAGENS DO CENÁRIO ====================
image bg store = StoreBackground()
image mask_overlay = MaskOverlay()

# Fundo sólido escuro para menus
image bg dark = Solid("#0f0f23")
image bg game_over = Solid("#1a0f0f")
