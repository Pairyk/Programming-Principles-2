import pygame
import random

# colors
WHITE   = (255, 255, 255)
BLACK   = (0,   0,   0)
GRAY    = (100, 100, 100)
LGRAY   = (160, 160, 160)
RED     = (220, 50,  50)
GREEN   = (50,  200, 80)
BLUE    = (50,  120, 220)
YELLOW  = (240, 200, 30)
ORANGE  = (240, 130, 30)
CYAN    = (0,   200, 220)
DGREEN  = (0,   160, 60)
PURPLE  = (160, 50,  220)
ROAD_C  = (40,  40,  40)
GRASS_C = (30,  90,  30)

# car color mapping from settings
CAR_COLOR_MAP = {
    'blue': pygame.image.load("sprites/dauren_car_blue.png"),
    'red': pygame.image.load("sprites/enemy_dauren_car.png"),
    # 'green': pygame.image.load("sprites/dauren_car_green.png"),
    # 'yellow': pygame.image.load("sprites/dauren_car_yellow.png"),
}

WIDTH  = 400
HEIGHT = 600

# When loading in racer.py
ROAD_IMAGE = pygame.image.load("sprites/road.png").convert_alpha()
# Force it to the screen width and height exactly
ROAD_IMAGE = pygame.transform.smoothscale(ROAD_IMAGE, (400, 600))
# ---- road drawing helpers ----

# In racer.py
def draw_road(screen, stripe_offset, nitro_active):
    # Get the exact height of the image you loaded
    img_height = ROAD_IMAGE.get_height()
    
    # Draw the main image
    screen.blit(ROAD_IMAGE, (0, int(stripe_offset)))
    
    # Draw the second image exactly one 'img_height' above the first
    # Subtract 1 to create a 1-pixel overlap (hiding the gap)
    screen.blit(ROAD_IMAGE, (0, int(stripe_offset - img_height + 1)))


def get_lane_x(lane, num_lanes=3):
    # returns center x of lane (0-indexed)
    road_start = 40
    road_w = WIDTH - 80
    lane_w = road_w // num_lanes
    return road_start + lane * lane_w + lane_w // 2


# ---- player car ----

class Player(pygame.sprite.Sprite):
    def __init__(self, car_color='blue'):
        super().__init__()
        # 1. Keep a MASTER copy that never changes
        raw_img = CAR_COLOR_MAP.get(car_color)
        self.master_image = pygame.transform.scale(raw_img, (36, 60))
        
        # 2. Set the active image
        self.image = self.master_image.copy()
        
        self.base_speed = 5
        self.speed = self.base_speed

        self.shield_active = False  
        self.nitro_active = False
        self.nitro_timer = 0   
        self.shield_used = False  

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20

    def refresh_image(self):
        # ALWAYS start from the clean master_image
        new_surf = self.master_image.copy()

        if self.shield_active:
            # Drawing on the fresh copy
            pygame.draw.ellipse(new_surf, (0, 200, 255, 150), new_surf.get_rect(), 3)
        
        # If you add nitro visuals later:
        # if self.nitro_active:
        #     draw_flames(new_surf)
            
        self.image = new_surf

    def update_powerups(self):
        if self.nitro_active:
            self.nitro_timer -= 1
            if self.nitro_timer <= 0:
                self.nitro_active = False
                self.speed = self.base_speed
                self.refresh_image() # This now correctly clears effects

    # ... move, apply_nitro, apply_shield, absorb_hit look great!

    def move(self):
        keys = pygame.key.get_pressed()
        spd  = self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.move_ip(spd, 0)
        if keys[pygame.K_LEFT]  or keys[pygame.K_a]:
            self.rect.move_ip(-spd, 0)
        # clamp to road
        if self.rect.left < 42: self.rect.left = 42
        if self.rect.right > WIDTH - 42: self.rect.right = WIDTH - 42

    def update_powerups(self):
        # count down nitro timer
        if self.nitro_active:
            self.nitro_timer -= 1
            if self.nitro_timer <= 0:
                self.nitro_active = False
                self.speed = self.base_speed
                self.refresh_image()

    def apply_nitro(self, duration_ticks=240):
        self.nitro_active = True
        self.nitro_timer = duration_ticks
        self.speed = self.base_speed + 5

    def apply_shield(self):
        self.shield_active = True
        self.shield_used = False
        self.refresh_image()

    def absorb_hit(self):
        # returns True if shield absorbed the hit
        if self.shield_active:
            self.shield_active = False
            self.refresh_image()
            return True
        return False


# ---- enemy traffic car ----

class EnemyCar(pygame.sprite.Sprite):
    def __init__(self, speed=6, player_rect=None):
        super().__init__()
        self.raw_image = pygame.image.load("sprites/enemy_dauren_car.png").convert_alpha()
        self.master_image = pygame.transform.scale(self.raw_image, (36, 60))
        self.image = self.master_image.copy()

        self.rect = self.image.get_rect()
        self.speed = speed
        self._spawn_safe(player_rect)

    def _spawn_safe(self, player_rect):
        # pick a random lane, make sure not on top of player
        for _ in range(20):
            lane = random.randint(0, 2)
            self.rect.centerx = get_lane_x(lane)
            self.rect.bottom = random.randint(-200, -60)
            if player_rect is None:
                break
            if not self.rect.inflate(0, 60).colliderect(player_rect):
                break

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT + 10:
            self._spawn_safe(None)


# ---- road obstacle: oil spill / pothole / barrier ----

class Obstacle(pygame.sprite.Sprite):
    TYPES = ['oil', 'pothole', 'barrier']

    def __init__(self, speed=5, player_rect=None):
        super().__init__()
        self.kind = random.choice(self.TYPES)
        self.speed = speed
        self.image = self._make_image()
        self.rect = self.image.get_rect()
        self._spawn_safe(player_rect)

    def _make_image(self):
        if self.kind == 'oil':
            surf = pygame.Surface((44, 22), pygame.SRCALPHA)
            pygame.draw.ellipse(surf, (20, 20, 80, 200), (0, 0, 44, 22))
            pygame.draw.ellipse(surf, (60, 60, 180, 120),(4, 4, 36, 14))
            return surf
        elif self.kind == 'pothole':
            surf = pygame.Surface((30, 20), pygame.SRCALPHA)
            pygame.draw.ellipse(surf, (20, 20, 20), (0, 0, 30, 20))
            pygame.draw.ellipse(surf, (60, 60, 60), (4, 4, 22, 12))
            return surf
        else:  # barrier
            surf = pygame.Surface((50, 20), pygame.SRCALPHA)
            pygame.draw.rect(surf, ORANGE, (0, 4, 50, 12), border_radius=4)
            for i in range(0, 50, 10):
                c = RED if (i // 10) % 2 == 0 else WHITE
                pygame.draw.rect(surf, c, (i, 4, 10, 12))
            return surf

    def _spawn_safe(self, player_rect):
        for _ in range(20):
            lane = random.randint(0, 2)
            self.rect.centerx = get_lane_x(lane)
            self.rect.bottom = random.randint(-300, -80)
            if player_rect is None:
                break
            if not self.rect.inflate(0, 80).colliderect(player_rect):
                break

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT + 10:
            self._spawn_safe(None)


# ---- nitro strip on road ----

class NitroStrip(pygame.sprite.Sprite):
    def __init__(self, speed=5):
        super().__init__()
        self.speed = speed
        self.image = self._make_image()
        self.rect = self.image.get_rect()
        lane = random.randint(0, 2)
        self.rect.centerx = get_lane_x(lane)
        self.rect.bottom = -20

    def _make_image(self):
        surf = pygame.Surface((60, 18), pygame.SRCALPHA)
        pygame.draw.rect(surf, CYAN, (0, 0, 60, 18), border_radius=4)
        arrow = [(10, 9), (30, 2), (50, 9), (30, 16)]
        pygame.draw.polygon(surf, WHITE, arrow)
        return surf

    def move(self):
        self.rect.move_ip(0, self.speed)


# ---- coin (carries over logic from base, adds weight) ----

class Coin(pygame.sprite.Sprite):
    WEIGHT_COLORS = {1: YELLOW, 3: ORANGE, 5: RED, 10: CYAN}

    def __init__(self, speed=6):
        super().__init__()
        self.speed = speed
        self.weight = random.choice((1, 3, 5, 10))
        self.image = self._make_image()
        self.rect = self.image.get_rect()
        lane = random.randint(0, 2)
        self.rect.centerx = get_lane_x(lane)
        self.rect.bottom = random.randint(-400, -40)

    def _make_image(self):
        c = self.WEIGHT_COLORS.get(self.weight, YELLOW)
        surf = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(surf, c, (10, 10), 10)
        pygame.draw.circle(surf, BLACK, (10, 10), 10, 2)
        label = pygame.font.SysFont('consolas', 9, bold=True).render(str(self.weight), True, BLACK)
        surf.blit(label, label.get_rect(center=(10, 10)))
        return surf

    def respawn(self):
        self.weight = random.choice((1, 3, 5, 10))
        self.image = self._make_image()
        lane = random.randint(0, 2)
        self.rect.centerx = get_lane_x(lane)
        self.rect.bottom = random.randint(-400, -40)

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT + 10:
            self.respawn()


# ---- power-up item ----

class PowerUp(pygame.sprite.Sprite):
    TYPES = ['nitro', 'shield', 'repair']
    LIFETIME = 300  # frames before it disappears if not collected

    def __init__(self, speed=5):
        super().__init__()
        self.kind = random.choice(self.TYPES)
        self.speed = speed
        self.timer = self.LIFETIME
        self.image = self._make_image()
        self.rect = self.image.get_rect()
        lane = random.randint(0, 2)
        self.rect.centerx = get_lane_x(lane)
        self.rect.bottom  = -30

    def _make_image(self):
        surf = pygame.Surface((28, 28), pygame.SRCALPHA)
        colors = {'nitro': CYAN, 'shield': BLUE, 'repair': GREEN}
        labels = {'nitro': 'N', 'shield': 'S', 'repair': 'R'}
        c = colors.get(self.kind, WHITE)
        # pulsing size not possible per frame easily, just draw static box
        pygame.draw.rect(surf, c, (0, 0, 28, 28), border_radius=6)
        pygame.draw.rect(surf, WHITE, (0, 0, 28, 28), 2, border_radius=6)
        lbl = pygame.font.SysFont('consolas', 16, bold=True).render(labels[self.kind], True, BLACK)
        surf.blit(lbl, lbl.get_rect(center=(14, 14)))
        return surf

    def move(self):
        self.rect.move_ip(0, self.speed)
        self.timer -= 1

    def is_expired(self):
        return self.timer <= 0 or self.rect.top > HEIGHT + 10


# ---- hud drawing ----

def draw_hud(screen, score, distance, coins_collected, player,
             active_powerup, powerup_timer, fonts):
    # semi transparent top bar
    bar = pygame.Surface((WIDTH, 40), pygame.SRCALPHA)
    bar.fill((0, 0, 0, 160))
    screen.blit(bar, (0, 0))

    sc_txt = fonts['small'].render(f'score: {score}', True, YELLOW)
    ds_txt = fonts['small'].render(f'dist: {distance}m', True, WHITE)
    cn_txt = fonts['small'].render(f'coins: {coins_collected}', True, ORANGE)
    screen.blit(sc_txt, (8, 10))
    screen.blit(ds_txt, (WIDTH // 2 - ds_txt.get_width() // 2, 10))
    screen.blit(cn_txt, (WIDTH - cn_txt.get_width() - 8, 10))

    # powerup indicator
    if active_powerup:
        pu_colors = {'nitro': CYAN, 'shield': BLUE, 'repair': GREEN}
        c = pu_colors.get(active_powerup, WHITE)
        secs = max(0, powerup_timer // 60)
        pu_txt = fonts['tiny'].render(
            f'{active_powerup.upper()} {"active" if active_powerup == "shield" else f"{secs}s"}',
            True, c
        )
        screen.blit(pu_txt, (WIDTH // 2 - pu_txt.get_width() // 2, 44))

    # shield indicator icon
    if player.shield_active:
        pygame.draw.rect(screen, BLUE, (WIDTH - 36, 44, 28, 18), border_radius=4)
        lbl = fonts['tiny'].render('SHD', True, WHITE)
        screen.blit(lbl, (WIDTH - 34, 46))

    # nitro indicator
    if player.nitro_active:
        pygame.draw.rect(screen, CYAN, (8, 44, 28, 18), border_radius=4)
        lbl = fonts['tiny'].render('NIT', True, BLACK)
        screen.blit(lbl, (10, 46))
