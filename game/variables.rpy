# Behind The Smile - Variáveis e Configurações
# Central de Triagem da Felicidade

init python:
    import random
    import time as pytime
    
    # ==================== CONFIGURAÇÕES ====================
    class GameConfig:
        GAME_DURATION = 90          # segundos
        SPAWN_INTERVAL = 2.0        # segundos entre checks de spawn
        SPAWN_CUSTOMER_CHANCE = 0.35
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
            "name": "Funcionário Monstro",
            "description": "Um colega de trabalho comum, precisa de ajuda.",
            "line": "Ei, pode me ajudar com isso?",
            "patience": 6,
            "emoji": "🧑",
            "points": 10,
            "rarity": "common"
        },
        {
            "id": "bizarre",
            "name": "Funcionário Alien",
            "description": "Parece estranho... mas trabalha aqui.",
            "line": "As máquinas... elas falam comigo.",
            "patience": 4,
            "emoji": "🤪",
            "points": 15,
            "rarity": "common"
        },
        {
            "id": "angry",
            "name": "Funcionário He",
            "description": "Já está irritado. Melhor resolver rápido!",
            "line": "Por que tudo demora tanto aqui?!",
            "patience": 3,
            "emoji": "😠",
            "points": 20,
            "rarity": "uncommon"
        },
        {
            "id": "vip",
            "name": "Funcionária She",
            "description": "Uma supervisora da Central. Atenção máxima!",
            "line": "A Central espera eficiência total.",
            "patience": 8,
            "emoji": "🎩",
            "points": 30,
            "rarity": "rare"
        },
        {
            "id": "inspector",
            "name": "Inspetor de Felicidade",
            "description": "Avalia se todos estão sorrindo adequadamente.",
            "line": "Seu sorriso está dentro dos padrões?",
            "patience": 5,
            "emoji": "🕵️",
            "points": 40,
            "rarity": "rare"
        },
        {
            "id": "robot",
            "name": "Robô de Manutenção",
            "description": "Máquina da Central para reparos. Eficiência máxima.",
            "line": "Executando protocolo de manutenção...",
            "patience": 10,
            "emoji": "🤖",
            "points": 25,
            "rarity": "uncommon"
        },
        {
            "id": "paranoid",
            "name": "Funcionária Paranóica",
            "description": "Acha que está sendo vigiada. Muito nervosa.",
            "line": "Eles estão nos observando o tempo todo...",
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
            "id": "mail",
            "name": "Carteiro Urgente",
            "description": "Carta da Central! Precisa assinar!",
            "resolve_time": 6,
            "emoji": "📮",
            "points": 12,
            "severity": "medium"
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

# Controle de animação
default customer_entering = False
default customer_enter_time = 0.0

# Controle de tempo
default game_start_time = 0.0
default last_spawn_check = 0.0
default last_difficulty_increase = 0.0
