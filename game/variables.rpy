# Behind The Smile - Variáveis e Configurações
# Central de Triagem da Felicidade

init python:
    import random
    import time as pytime
    
    # ==================== CONFIGURAÇÕES ====================
    class GameConfig:
        GAME_DURATION = 60          # segundos (1 minuto)
        SPAWN_INTERVAL = 8.0        # segundos entre checks de spawn (aumentado para dar mais tempo)
        SPAWN_CUSTOMER_CHANCE = 0.15  # reduzido para spawns menos frequentes
        SPAWN_DANGER_CHANCE = 0.25
        
        POINTS_PER_DANGER = 15
        POINTS_PER_CUSTOMER = 10
        POINTS_CUSTOMER_SERVED = 25
        
        DIFFICULTY_INCREASE_INTERVAL = 20  # segundos
        DIFFICULTY_MULTIPLIER = 1.1
        
        TIME_WARNING = 30
        TIME_CRITICAL = 10
    
    # ==================== TIPOS DE FUNCIONÁRIOS ====================
    CUSTOMER_TYPES = [
        {
            "id": "normal",
            "name": "Monstro",
            "description": "Um ex-colega que enlouqueceu após demissão.",
            "line": "A crise burocrática nos quebrou... agora somos monstros famintos por negatividade. Ajude-me antes que eu perca o controle!",
            "patience": 6,
            "emoji": "🧑",
            "points": 10,
            "rarity": "common"
        },
        {
            "id": "bizarre",
            "name": "Alien",
            "description": "Parece estranho... mas trabalha aqui.",
            "line": "A fenda da realidade trouxe coisas... entidades. Elas falam através das máquinas. Você ouve os sussurros?",
            "patience": 4,
            "emoji": "🤪",
            "points": 15,
            "rarity": "common"
        },
        {
            "id": "angry",
            "name": "Raivoso",
            "description": "Já está irritado. Melhor resolver rápido!",
            "line": "Este lugar... a loja da fenda... ela nos transforma. A negatividade cresce, e nós... comemos.",
            "patience": 3,
            "emoji": "😠",
            "points": 20,
            "rarity": "uncommon"
        },
        {
            "id": "vip",
            "name": "She",
            "description": "Uma supervisora da Central. Atenção máxima!",
            "line": "A Gerência criou as máscaras para nos proteger... ou para nos controlar? Eficiência total, funcionário. Sempre sorrindo.",
            "patience": 8,
            "emoji": "🎩",
            "points": 30,
            "rarity": "rare"
        },
        {
            "id": "inspector",
            "name": "Inspetor de Felicidade",
            "description": "Avalia se todos estão sorrindo adequadamente.",
            "line": "O sorriso é obrigatório. A tristeza é proibida. Mas por trás da máscara... o que você realmente sente?",
            "patience": 5,
            "emoji": "🕵️",
            "points": 40,
            "rarity": "rare"
        },
        {
            "id": "robot",
            "name": "Robô de Manutenção",
            "description": "Máquina da Central para reparos. Eficiência máxima.",
            "line": "Protocolo de manutenção: humanos são ineficientes. A anomalia se espalha... otimize ou seja consumido.",
            "patience": 10,
            "emoji": "🤖",
            "points": 25,
            "rarity": "uncommon"
        },
        {
            "id": "paranoid",
            "name": "Paranóica",
            "description": "Acha que está sendo vigiada. Muito nervosa.",
            "line": "A Gerência nos observa. Sempre. A fenda trouxe monstros... e eles se alimentam de nossas emoções. Não confie em ninguém.",
            "patience": 2,
            "emoji": "😰",
            "points": 35,
            "rarity": "rare"
        }
    ]
    
    # ==================== TIPOS DE PERIGOS ====================
    DANGER_TYPES = [
        {
            "id": "fire",
            "name": "Incêndio",
            "description": "Fogo começando nas prateleiras!",
            "resolve_time": 8,
            "emoji": "🔥",
            "points": 15,
            "severity": "high"
        },
        {
            "id": "alarm",
            "name": "Alarme",
            "description": "O alarme de segurança disparou!",
            "resolve_time": 5,
            "emoji": "🚨",
            "points": 10,
            "severity": "medium"
        },
        {
            "id": "monster",
            "name": "Criatura",
            "description": "Algo se aproxima das sombras...",
            "resolve_time": 12,
            "emoji": "👹",
            "points": 25,
            "severity": "critical"
        },
        {
            "id": "leak",
            "name": "Vazamento",
            "description": "Líquido estranho vazando do teto!",
            "resolve_time": 7,
            "emoji": "💧",
            "points": 12,
            "severity": "medium"
        },
        {
            "id": "blackout",
            "name": "Queda de Luz",
            "description": "As luzes estão piscando!",
            "resolve_time": 4,
            "emoji": "💡",
            "points": 8,
            "severity": "low"
        },
        {
            "id": "rat",
            "name": "Infestação",
            "description": "Algo se move entre as caixas...",
            "resolve_time": 9,
            "emoji": "🐀",
            "points": 18,
            "severity": "high"
        },
        {
            "id": "glitch",
            "name": "Glitch na Câmera",
            "description": "A câmera de vigilância está com defeito!",
            "resolve_time": 3,
            "emoji": "📹",
            "points": 20,
            "severity": "critical"
        },
        {
            "id": "phone",
            "name": "Telefone",
            "description": "Ligação da Central! Atenda!",
            "resolve_time": 5,
            "emoji": "☎️",
            "points": 15,
            "severity": "high"
        }
    ]
    
    # ==================== FUNÇÕES AUXILIARES ====================
    def get_random_customer():
        """Retorna um cliente aleatório baseado em raridade"""
        roll = random.random() * 100
        
        if roll < 10:
            target_rarity = "rare"
        elif roll < 40:
            target_rarity = "uncommon"
        else:
            target_rarity = "common"
        
        filtered = [c for c in CUSTOMER_TYPES if c["rarity"] == target_rarity]
        return random.choice(filtered).copy()
    
    def get_random_danger():
        """Retorna um perigo aleatório baseado em severidade"""
        roll = random.random() * 100
        
        if roll < 10:
            target_severity = "critical"
        elif roll < 30:
            target_severity = "high"
        elif roll < 70:
            target_severity = "medium"
        else:
            target_severity = "low"
        
        filtered = [d for d in DANGER_TYPES if d["severity"] == target_severity]
        return random.choice(filtered).copy()

    # ==================== PRODUTOS PARA ESCANEAR ====================
    PRODUCTS = [
        {"id": "bread", "name": "Pão", "emoji": "🍞", "scan_time": 2.0},
        {"id": "milk", "name": "Leite", "emoji": "🥛", "scan_time": 1.5},
        {"id": "eggs", "name": "Ovos", "emoji": "🥚", "scan_time": 2.5},
        {"id": "cheese", "name": "Queijo", "emoji": "🧀", "scan_time": 1.8},
        {"id": "apples", "name": "Maçãs", "emoji": "🍎", "scan_time": 3.0},
        {"id": "coffee_beans", "name": "Grãos de Café", "emoji": "☕", "scan_time": 2.2},
    ]

    # ==================== CARIMBOS ====================
    STAMPS = [
        {"id": "approved", "name": "APROVADO", "color": "#44ff44"},
        {"id": "validated", "name": "VALIDADO", "color": "#f4d03f"},
        {"id": "processed", "name": "PROCESSADO", "color": "#4444ff"},
    ]

# ==================== VARIÁVEIS DE ESTADO ====================
default game_state = "menu"  # menu, playing, paused, game_over
default time_left = 90
default score = 0
default mask_on = True
# Estado visual do jogador: normal, alert, infected
default player_status = "normal"
default difficulty_multiplier = 1.0

default current_customer = None
default current_danger = None
default customer_time_left = 0
default danger_time_left = 0

default customers_served = 0
default dangers_resolved = 0
default game_over_reason = ""

default current_shift = 1  # Turno atual (1-5)

# Controle de animação
default customer_entering = False
default customer_enter_time = 0.0

# Controle de mouse para máscara
default mouse_x = 640
default mouse_y = 360
default arm_stability = 100.0  # 0-100
default stability_decay_rate = 5.0  # por segundo
default last_stability_update = 0.0

# Sistema de produtos para escanear
default products_to_scan = []  # Lista de produtos que aparecem no balcão
default scanned_products = []  # Produtos já escaneados
default scanning_product = None  # Produto sendo escaneado atualmente
default scan_start_time = 0.0  # Quando começou a escanear

# Sistema de carimbos
default stamps_available = []  # Carimbos disponíveis para usar
default current_stamp = None  # Carimbo selecionado

# Sistema de café
default coffee_available = True  # Se café está disponível para beber
default coffee_cooldown = 0.0  # Tempo até poder beber café novamente
default last_coffee_time = 0.0  # Última vez que bebeu café
