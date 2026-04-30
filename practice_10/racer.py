"""racer.py – sprites, groups, and the main game-loop function."""

import pygame, random, math
from pygame.locals import *
from settings import *


# ═══════════════════════════════════════════════════════════════
#  Utility helpers
# ═══════════════════════════════════════════════════════════════

def lane_x(lane: int) -> int:
    """Return left-edge pixel x for a lane index 0‥LANE_COUNT-1."""
    return lane * LANE_WIDTH + (LANE_WIDTH - car_width) // 2


def safe_spawn_x(player_rect, margin=80) -> int:
    """Pick a random lane that is not directly above the player."""
    options = list(range(LANE_COUNT))
    player_lane = player_rect.centerx // LANE_WIDTH
    safe = [l for l in options if abs(l - player_lane) >= 1]
    lane = random.choice(safe if safe else options)
    return lane_x(lane)


# ═══════════════════════════════════════════════════════════════
#  Road background (scrolling stripes)
# ═══════════════════════════════════════════════════════════════

class Road:
    """Draws a tiled road with lane markings."""

    def __init__(self):
        self.offset = 0
        self.tile_h = 60        # height of each dashed segment

    def update(self, speed):
        self.offset = (self.offset + speed) % self.tile_h

    def draw(self, surface):
        # grass sides
        pygame.draw.rect(surface, GRASS_COLOR, (0, 0, screen_width, screen_height))
        # road body
        road_rect = pygame.Rect(0, 0, screen_width, screen_height)
        pygame.draw.rect(surface, ROAD_COLOR, road_rect)

        # lane dashes
        for lane in range(1, LANE_COUNT):
            x = lane * LANE_WIDTH
            y = -self.tile_h + self.offset
            while y < screen_height:
                pygame.draw.rect(surface, LANE_LINE_COLOR, (x - 2, y, 4, self.tile_h // 2))
                y += self.tile_h

        # road edges
        pygame.draw.rect(surface, WHITE, (0, 0, 6, screen_height))
        pygame.draw.rect(surface, WHITE, (screen_width - 6, 0, 6, screen_height))


# ═══════════════════════════════════════════════════════════════
#  Player
# ═══════════════════════════════════════════════════════════════

class Player(pygame.sprite.Sprite):
    def __init__(self, car_color="red"):
        super().__init__()
        self.base_speed = player_speed
        self.speed = player_speed
        self.car_color = car_color
        self.image = self._make_image()
        self.rect = self.image.get_rect(
            centerx=screen_width // 2,
            bottom=screen_height - 20
        )
        self.shield_active = False
        self.nitro_active = False
        self.nitro_end = 0
        self.shield_hits = 0
        self.distance = 0
        self.coins_collected = 0

    def _make_image(self):
        color = CAR_COLORS.get(self.car_color, RED)
        surf = pygame.Surface((car_width, car_height), SRCALPHA)
        # body
        pygame.draw.rect(surf, color, (5, 10, car_width-10, car_height-20), border_radius=8)
        # windshield
        pygame.draw.rect(surf, (160, 220, 255, 180), (10, 18, car_width-20, 22), border_radius=4)
        # headlights
        pygame.draw.rect(surf, YELLOW, (8, 12, 14, 8), border_radius=3)
        pygame.draw.rect(surf, YELLOW, (car_width-22, 12, 14, 8), border_radius=3)
        # tail lights
        pygame.draw.rect(surf, RED, (8, car_height-22, 14, 8), border_radius=3)
        pygame.draw.rect(surf, RED, (car_width-22, car_height-22, 14, 8), border_radius=3)
        # wheels
        for wx, wy in [(0,15),(car_width-10,15),(0,car_height-35),(car_width-10,car_height-35)]:
            pygame.draw.rect(surf, DARK, (wx, wy, 10, 20), border_radius=3)
        return surf

    def activate_nitro(self):
        self.nitro_active = True
        self.speed = self.base_speed * 2
        self.nitro_end = pygame.time.get_ticks() + NITRO_DURATION

    def activate_shield(self):
        self.shield_active = True
        self.shield_hits = 1

    def repair(self):
        # Repair clears any slow effect and resets speed
        self.speed = self.base_speed
        self.nitro_active = False

    def update(self, screen_rect):
        now = pygame.time.get_ticks()
        if self.nitro_active and now >= self.nitro_end:
            self.nitro_active = False
            self.speed = self.base_speed

        pressed = pygame.key.get_pressed()
        dx, dy = 0, 0
        if pressed[K_w] or pressed[K_UP]:    dy = -self.speed
        if pressed[K_s] or pressed[K_DOWN]:  dy =  self.speed
        if pressed[K_a] or pressed[K_LEFT]:  dx = -self.speed
        if pressed[K_d] or pressed[K_RIGHT]: dx =  self.speed
        self.rect.move_ip(dx, dy)
        self.rect.clamp_ip(screen_rect)
        self.distance += DIST_PER_FRAME

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.shield_active:
            r = self.rect.inflate(12, 12)
            pygame.draw.ellipse(surface, SHIELD_COLOR, r, 3)
        if self.nitro_active:
            # draw flame under car
            fx = self.rect.centerx
            fy = self.rect.bottom
            for i in range(5):
                off = random.randint(-8, 8)
                h = random.randint(8, 20)
                pygame.draw.polygon(surface, ORANGE,
                    [(fx+off-6, fy), (fx+off+6, fy), (fx+off, fy+h)])


# ═══════════════════════════════════════════════════════════════
#  Enemy car
# ═══════════════════════════════════════════════════════════════

ENEMY_COLORS = [
    (180, 60,  60),
    ( 60, 60, 180),
    ( 60,180,  60),
    (180,180,  60),
    (160, 60, 180),
    (180,120,  40),
]

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed, player_rect):
        super().__init__()
        self.speed = speed
        self.image = self._make_image()
        lx = safe_spawn_x(player_rect)
        self.rect = self.image.get_rect(x=lx, y=-car_height - random.randint(0, 200))

    def _make_image(self):
        color = random.choice(ENEMY_COLORS)
        surf = pygame.Surface((car_width, car_height), SRCALPHA)
        pygame.draw.rect(surf, color, (5, 10, car_width-10, car_height-20), border_radius=8)
        pygame.draw.rect(surf, (160, 220, 255, 160), (10, 40, car_width-20, 20), border_radius=4)
        pygame.draw.rect(surf, YELLOW, (8, car_height-22, 14, 8), border_radius=3)
        pygame.draw.rect(surf, YELLOW, (car_width-22, car_height-22, 14, 8), border_radius=3)
        for wx, wy in [(0,15),(car_width-10,15),(0,car_height-35),(car_width-10,car_height-35)]:
            pygame.draw.rect(surf, DARK, (wx, wy, 10, 20), border_radius=3)
        return surf

    def update(self, player_rect=None):
        self.rect.move_ip(0, self.speed)
        if self.rect.top >= screen_height:
            if player_rect:
                lx = safe_spawn_x(player_rect)
            else:
                lx = lane_x(random.randint(0, LANE_COUNT-1))
            self.rect.x = lx
            self.rect.y = -car_height - random.randint(0, 150)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# ═══════════════════════════════════════════════════════════════
#  Coins
# ═══════════════════════════════════════════════════════════════

class Coin(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.speed = speed
        self.value = random.choices([COIN_SCORE, UNIQUE_COIN_SCORE], weights=[70, 30])[0]
        color = YELLOW if self.value == COIN_SCORE else CYAN
        self.image = self._make_image(color)
        lane = random.randint(0, LANE_COUNT-1)
        self.rect = self.image.get_rect(
            x=lane * LANE_WIDTH + (LANE_WIDTH - coin_width) // 2,
            y=-coin_height
        )

    def _make_image(self, color):
        surf = pygame.Surface((coin_width, coin_height), SRCALPHA)
        pygame.draw.circle(surf, color, (coin_width//2, coin_height//2), coin_width//2)
        pygame.draw.circle(surf, WHITE, (coin_width//2, coin_height//2), coin_width//4)
        return surf

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top >= screen_height:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# ═══════════════════════════════════════════════════════════════
#  Obstacles  (oil spill, barrier, speed bump, pothole)
# ═══════════════════════════════════════════════════════════════

OBS_TYPES = ["oil", "barrier", "bump", "pothole"]

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, speed, player_rect):
        super().__init__()
        self.otype = random.choice(OBS_TYPES)
        self.speed = speed
        self.image = self._make_image()
        lx = safe_spawn_x(player_rect)
        self.rect = self.image.get_rect(x=lx, y=-obstacle_height - random.randint(0,100))

    def _make_image(self):
        w, h = obstacle_width, obstacle_height
        surf = pygame.Surface((w, h), SRCALPHA)
        if self.otype == "oil":
            pygame.draw.ellipse(surf, OIL_COLOR, (0, 0, w, h))
            pygame.draw.ellipse(surf, (40, 40, 120, 180), (4, 4, w-8, h-8))
        elif self.otype == "barrier":
            pygame.draw.rect(surf, BARRIER_COLOR, (0, 8, w, h-16), border_radius=4)
            for i in range(0, w, 16):
                pygame.draw.rect(surf, WHITE, (i, 8, 8, h-16))
        elif self.otype == "bump":
            pygame.draw.rect(surf, BUMP_COLOR, (0, h//3, w, h//3), border_radius=6)
            pygame.draw.rect(surf, GRAY, (0, h//3+2, w, 4))
        else:  # pothole
            pygame.draw.ellipse(surf, (20, 15, 10), (5, 2, w-10, h-4))
            pygame.draw.ellipse(surf, (50, 40, 30), (10, 5, w-20, h-10))
        return surf

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top >= screen_height:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def apply_effect(self, player):
        if self.otype == "oil":
            player.speed = max(1, player.speed - 2)
        elif self.otype == "bump":
            player.speed = max(1, player.speed - 1)
        # barrier and pothole cause damage (handled by caller)


# ═══════════════════════════════════════════════════════════════
#  Power-ups
# ═══════════════════════════════════════════════════════════════

PU_TYPES = ["nitro", "shield", "repair"]

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.ptype = random.choice(PU_TYPES)
        self.speed = speed
        self.spawn_time = pygame.time.get_ticks()
        self.image = self._make_image()
        lane = random.randint(0, LANE_COUNT-1)
        self.rect = self.image.get_rect(
            x=lane * LANE_WIDTH + (LANE_WIDTH - powerup_width) // 2,
            y=-powerup_height
        )
        self.pulse = 0

    def _make_image(self):
        w, h = powerup_width, powerup_height
        surf = pygame.Surface((w, h), SRCALPHA)
        colors = {"nitro": NITRO_COLOR, "shield": SHIELD_COLOR, "repair": REPAIR_COLOR}
        labels = {"nitro": "N", "shield": "S", "repair": "R"}
        color = colors[self.ptype]
        pygame.draw.rect(surf, color, (0, 0, w, h), border_radius=8)
        pygame.draw.rect(surf, WHITE, (2, 2, w-4, h-4), 2, border_radius=7)
        font = pygame.font.SysFont("Arial", 22, bold=True)
        txt = font.render(labels[self.ptype], True, WHITE)
        surf.blit(txt, txt.get_rect(center=(w//2, h//2)))
        return surf

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top >= screen_height:
            self.kill()
            return
        if pygame.time.get_ticks() - self.spawn_time > POWERUP_TIMEOUT:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def apply(self, player):
        if self.ptype == "nitro":
            player.activate_nitro()
        elif self.ptype == "shield":
            player.activate_shield()
        elif self.ptype == "repair":
            player.repair()


# ═══════════════════════════════════════════════════════════════
#  Nitro strip  (road event)
# ═══════════════════════════════════════════════════════════════

class NitroStrip(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.speed = speed
        w = LANE_WIDTH
        h = 20
        surf = pygame.Surface((w, h), SRCALPHA)
        pygame.draw.rect(surf, NITRO_COLOR, (0, 0, w, h), border_radius=4)
        for i in range(0, w, 12):
            pygame.draw.rect(surf, WHITE, (i, 0, 6, h))
        self.image = surf
        lane = random.randint(0, LANE_COUNT-1)
        self.rect = self.image.get_rect(x=lane * LANE_WIDTH, y=-h)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top >= screen_height:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# ═══════════════════════════════════════════════════════════════
#  HUD drawing helpers
# ═══════════════════════════════════════════════════════════════

def draw_hud(surface, player, score, distance, finish_distance, active_pu, pu_end, font_sm):
    # Score
    txt = font_sm.render(f"Score: {score}", True, WHITE)
    surface.blit(txt, (10, 10))

    # Distance
    remaining = max(0, finish_distance - distance)
    txt2 = font_sm.render(f"Dist: {distance}m  Rem: {remaining}m", True, WHITE)
    surface.blit(txt2, (10, 38))

    # Shield indicator
    if player.shield_active:
        stxt = font_sm.render("🛡 SHIELD", True, SHIELD_COLOR)
        surface.blit(stxt, (screen_width - 130, 10))

    # Active power-up
    if active_pu:
        now = pygame.time.get_ticks()
        colors = {"nitro": NITRO_COLOR, "shield": SHIELD_COLOR, "repair": REPAIR_COLOR}
        color = colors.get(active_pu, WHITE)
        if active_pu == "nitro":
            rem_s = max(0, (pu_end - now) / 1000)
            label = f"NITRO {rem_s:.1f}s"
        elif active_pu == "shield":
            label = "SHIELD active"
        else:
            label = ""
        if label:
            pu_surf = font_sm.render(label, True, color)
            surface.blit(pu_surf, (screen_width//2 - pu_surf.get_width()//2, 10))

    # Progress bar
    bar_w = screen_width - 20
    bar_h = 8
    bar_x, bar_y = 10, screen_height - 14
    pygame.draw.rect(surface, GRAY, (bar_x, bar_y, bar_w, bar_h), border_radius=4)
    progress = min(1.0, distance / finish_distance)
    pygame.draw.rect(surface, GREEN, (bar_x, bar_y, int(bar_w * progress), bar_h), border_radius=4)


# ═══════════════════════════════════════════════════════════════
#  Main game loop
# ═══════════════════════════════════════════════════════════════

def run_game(settings: dict) -> dict:
    """
    Run one game session. Returns a result dict:
    {"score": int, "distance": int, "coins": int, "finished": bool}
    """
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Racer")
    clock = pygame.time.Clock()
    screen_rect = screen.get_rect()

    diff_name = settings.get("difficulty", "normal")
    diff = DIFFICULTY[diff_name]
    base_enemy_speed = diff["enemy_speed"]
    base_road_speed  = diff["road_speed"]
    max_enemies      = diff["max_enemies"]
    obs_freq         = diff["obstacle_freq"]

    sound_on = settings.get("sound", True)

    # ── font
    font_sm  = pygame.font.SysFont("Verdana", 22, bold=True)
    font_med = pygame.font.SysFont("Verdana", 36, bold=True)

    # ── road
    road = Road()
    cur_road_speed = base_road_speed
    cur_enemy_speed = base_enemy_speed

    # ── player
    player = Player(car_color=settings.get("car_color", "red"))

    # ── sprite groups
    enemies   = pygame.sprite.Group()
    coins_grp = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    powerups  = pygame.sprite.Group()
    strips    = pygame.sprite.Group()

    # spawn initial enemies
    for _ in range(max_enemies):
        e = Enemy(cur_enemy_speed, player.rect)
        enemies.add(e)

    # ── game state
    score          = 0
    distance       = 0
    coins_collected = 0
    active_pu      = None      # "nitro" | "shield" | "repair" | None
    pu_end_time    = 0
    crashed        = False
    finished       = False

    # ── timers / counters
    coin_timer   = 0
    obs_timer    = 0
    pu_timer     = 0
    strip_timer  = 0
    frame        = 0

    running = True
    while running:
        dt = clock.tick(60)
        frame += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                import sys; sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False  # back to menu

        # ── difficulty scaling every 500m
        tier = distance // 500
        cur_enemy_speed = base_enemy_speed + tier * 0.5
        cur_road_speed  = base_road_speed  + tier * 0.3
        cur_obs_freq    = max(40, obs_freq - tier * 10)

        # ── update road scroll
        road.update(cur_road_speed)

        # ── player update
        player.update(screen_rect)
        distance = player.distance

        # ── spawn coins
        coin_timer += 1
        if coin_timer >= 60:
            coin_timer = 0
            if len(coins_grp) < 4:
                c = Coin(cur_road_speed)
                coins_grp.add(c)

        # ── spawn obstacles
        obs_timer += 1
        if obs_timer >= cur_obs_freq:
            obs_timer = 0
            ob = Obstacle(cur_road_speed + 1, player.rect)
            obstacles.add(ob)

        # ── spawn power-ups (every ~15 s randomly)
        pu_timer += 1
        if pu_timer >= 900 and active_pu is None:
            pu_timer = 0
            if len(powerups) == 0:
                pu = PowerUp(cur_road_speed)
                powerups.add(pu)

        # ── spawn nitro strips (every ~20 s)
        strip_timer += 1
        if strip_timer >= 1200:
            strip_timer = 0
            strips.add(NitroStrip(cur_road_speed + 2))

        # ── update enemies
        for e in enemies:
            e.speed = cur_enemy_speed
            e.update(player.rect)

        # keep correct number of enemies
        while len(enemies) < max_enemies + tier:
            ne = Enemy(cur_enemy_speed, player.rect)
            enemies.add(ne)

        coins_grp.update()
        obstacles.update()
        powerups.update()
        strips.update()

        # ── collisions: coins
        hit_coins = pygame.sprite.spritecollide(player, coins_grp, True)
        for c in hit_coins:
            score += c.value
            coins_collected += 1
            player.coins_collected += 1

        # ── collisions: power-ups (only one at a time)
        hit_pu = pygame.sprite.spritecollide(player, powerups, True)
        for pu in hit_pu:
            if active_pu is None or pu.ptype == "repair":
                pu.apply(player)
                active_pu = pu.ptype
                if pu.ptype == "nitro":
                    pu_end_time = player.nitro_end
                elif pu.ptype == "repair":
                    active_pu = None  # instant

        # clear expired nitro
        if active_pu == "nitro" and pygame.time.get_ticks() >= pu_end_time:
            active_pu = None

        # ── collisions: obstacles
        hit_obs = pygame.sprite.spritecollide(player, obstacles, True)
        for ob in hit_obs:
            if player.shield_active:
                player.shield_active = False
                active_pu = None
            elif ob.otype in ("barrier", "pothole"):
                crashed = True
                running = False
            else:
                ob.apply_effect(player)  # slow-down but no crash

        # ── collisions: nitro strips
        hit_strips = pygame.sprite.spritecollide(player, strips, True)
        for _ in hit_strips:
            player.activate_nitro()
            active_pu = "nitro"
            pu_end_time = player.nitro_end

        # ── collisions: enemy cars
        if pygame.sprite.spritecollideany(player, enemies):
            if player.shield_active:
                player.shield_active = False
                active_pu = None
                # push enemies away
                for e in enemies:
                    if e.rect.colliderect(player.rect):
                        e.rect.y = -car_height
            else:
                crashed = True
                running = False

        # ── distance score bonus
        score += distance // 10 * DISTANCE_SCORE_RATE

        # ── finish check
        if distance >= FINISH_DISTANCE:
            finished = True
            score += 500
            running = False

        # ══ DRAW ═════════════════════════════════════════════
        road.draw(screen)
        strips.draw(screen)
        obstacles.draw(screen)
        coins_grp.draw(screen)
        powerups.draw(screen)
        for e in enemies:
            e.draw(screen)
        player.draw(screen)

        draw_hud(screen, player, score, distance, FINISH_DISTANCE,
                 active_pu, pu_end_time, font_sm)

        # ── Nitro shield HUD on side
        if player.shield_active:
            pygame.draw.rect(screen, SHIELD_COLOR, screen_rect, 4)

        pygame.display.flip()

    return {
        "score":    score,
        "distance": distance,
        "coins":    coins_collected,
        "finished": finished,
        "crashed":  crashed,
    }