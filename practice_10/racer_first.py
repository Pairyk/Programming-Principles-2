import sys, pygame, random
from pygame.locals import *
from racer_settings import *

pygame.init()

# just basic stuff yk
pygame.display.set_caption("Racer game")
screen = pygame.display.set_mode((screen_width, screen_height))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()
running = True

# score, ignore for now
score = 0
# ---------------------- Enemy class ----------------------------

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # car looksmaxing
        self.image_raw = pygame.image.load("sprites/enemy_dauren_car.png").convert_alpha()
        self.image = pygame.transform.scale(self.image_raw, (car_width, car_height))
        
        # positioning car to random x
        self.rect = self.image.get_rect(x=random.randint(0, screen_width-car_width), y = -car_height)

    def update(self):
        self.rect.move_ip(0, enemy_speed)
        # if top of the images lefts the borders, then we send it back to start 
        if self.rect.top >= screen_height:
            self.rect.x = random.randint(0, screen_width - car_width)
            self.rect.y = -car_height      

    # we have to appear on screen
    def draw(self, surface):
        surface.blit(self.image, self.rect)

# ---------------------- Players class ----------------------------

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # car looksmaxing
        self.image_raw = pygame.image.load("sprites/dauren_car.png").convert_alpha()
        self.image = pygame.transform.scale(self.image_raw, (car_width, car_height))
        
        # positioning car
        self.starting_pos = ((screen_width/2)-(car_width/2), (screen_height - (car_height*1.2)))
        self.rect = self.image.get_rect(centerx=(screen_width/2))
        self.rect.bottom = (screen_height - car_height)

    def update(self):
        # if specific key is pressed then it moves
        pressed = pygame.key.get_pressed()
        if pressed[K_w]:
            self.rect.move_ip(0, -player_speed)
        if pressed[K_s]:
            self.rect.move_ip(0, player_speed)
        if pressed[K_a]:
            self.rect.move_ip(-player_speed, 0)
        if pressed[K_d]:
            self.rect.move_ip(player_speed, 0)
        
        # don't leave the screen!
        self.rect.clamp_ip(screen_rect)

    # we have to appear on screen
    def draw(self, surface):
        surface.blit(self.image, self.rect)

# ---------------------- Coin class ----------------------------
COIN_TYPES = {
    "basic": {"value": 1, "path": "sprites/coin.png", "chance": 70},
    "unique": {"value": 2, "path": "sprites/unique_coin.png", "chance": 30}
}


COIN_IMAGES = {
    "basic": pygame.image.load("sprites/coin.png").convert_alpha(),
    "unique": pygame.image.load("sprites/unique_coin.png").convert_alpha()
}

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.is_active = True
        self.timer = 0
        self.cooldown = 1200
        self.spawn()

    def spawn(self):
        types = list(COIN_TYPES.keys())
        weights = [COIN_TYPES[t]["chance"] for t in types]
        self.type = random.choices(types, weights=weights)[0]

        self.value = COIN_TYPES[self.type]["value"]
        raw_image = COIN_IMAGES[self.type]

        self.image = pygame.transform.scale(raw_image, (coin_width, coin_height))

        self.rect = self.image.get_rect(
            x=random.randint(0, screen_width - coin_width),
            y=random.randint(0, screen_height - coin_height)
        )
        self.is_active = True

    def collided(self):
        global score
        score += self.value
        self.is_active = False
        self.timer = pygame.time.get_ticks()

    def update(self):
        if not self.is_active:
            current_time = pygame.time.get_ticks()
            if current_time - self.timer >= self.cooldown:
                self.spawn()

    def draw(self, surface):
        if self.is_active:
            surface.blit(self.image, self.rect)

# Game objects
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Grouping for mass action
road_objects = pygame.sprite.Group()
road_objects.add(C1)

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(E1, P1, C1)

# font
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 30)
game_over = font.render("Game Over", True, (255, 255, 255))

# ---------------------- Main loop ----------------------------

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.blit(bg, (0, 0))
    scores = font_small.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(scores, (10, 10))

    # displaying and moving everything
    for entity in all_sprites:
        entity.update()
        entity.draw(screen)

    if C1.is_active and pygame.sprite.collide_rect(P1, C1):
        old_score = score 
        C1.collided()

        if score // coin_speed > old_score // coin_speed:
            enemy_speed += 2

    # checking for collision
    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()

        screen.fill((0, 0, 0))
        screen.blit(game_over, (150, 400))
        pygame.display.flip()

        for entity in all_sprites:
            entity.kill()
        
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(60)

        pygame.time.delay(1000) 
        
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(60)
