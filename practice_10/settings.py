# ── Screen ──────────────────────────────────────────────────────
screen_width  = 480
screen_height = 700

# ── Lane layout ─────────────────────────────────────────────────
LANE_COUNT  = 4
LANE_WIDTH  = screen_width // LANE_COUNT   # 120 px each

# ── Sprite sizes ────────────────────────────────────────────────
car_width   = 60
car_height  = 100
coin_width  = 30
coin_height = 30
obstacle_width  = 60
obstacle_height = 30
powerup_width   = 40
powerup_height  = 40

# ── Speed constants (defaults – overridden by difficulty) ────────
player_speed  = 5
enemy_speed   = 4
coin_speed    = 10   # score milestone that triggers speed‑up
road_speed    = 4    # background scroll speed

# ── Difficulty presets ───────────────────────────────────────────
DIFFICULTY = {
    "easy":   {"enemy_speed": 3, "road_speed": 3, "max_enemies": 2, "obstacle_freq": 180},
    "normal": {"enemy_speed": 5, "road_speed": 5, "max_enemies": 3, "obstacle_freq": 120},
    "hard":   {"enemy_speed": 7, "road_speed": 7, "max_enemies": 5, "obstacle_freq":  80},
}

# ── Colours ─────────────────────────────────────────────────────
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
GRAY   = (100, 100, 100)
DARK   = ( 30,  30,  30)
YELLOW = (255, 220,   0)
GREEN  = ( 50, 200,  80)
RED    = (220,  40,  40)
BLUE   = ( 40, 100, 220)
ORANGE = (255, 140,   0)
CYAN   = (  0, 200, 220)
PURPLE = (160,  60, 220)
ROAD_COLOR      = ( 50,  50,  50)
LANE_LINE_COLOR = (200, 200,   0)
GRASS_COLOR     = ( 34,  85,  34)
OIL_COLOR       = ( 20,  20,  60)
NITRO_COLOR     = (  0, 255, 180)
SHIELD_COLOR    = ( 80, 160, 255)
REPAIR_COLOR    = ( 80, 255, 100)
BARRIER_COLOR   = (220,  80,  20)
BUMP_COLOR      = (160, 160,  20)

# ── Car colour map ───────────────────────────────────────────────
CAR_COLORS = {
    "red":    RED,
    "blue":   BLUE,
    "green":  GREEN,
    "yellow": YELLOW,
    "purple": PURPLE,
}

# ── Power-up durations (ms) ──────────────────────────────────────
NITRO_DURATION  = 4000
SHIELD_DURATION = 999999   # until hit
POWERUP_TIMEOUT = 7000     # disappear if not collected

# ── Score / distance ─────────────────────────────────────────────
DIST_PER_FRAME    = 1          # metres per frame (approx)
FINISH_DISTANCE   = 5000       # metres to finish
COIN_SCORE        = 10
UNIQUE_COIN_SCORE = 25
DISTANCE_SCORE_RATE = 1        # score per 10 m