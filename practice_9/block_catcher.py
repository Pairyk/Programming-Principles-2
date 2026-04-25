import pygame
import random
import settings as stt
from pygame.locals import *

# -- INITIALIZATION
pygame.init()
screen = pygame.display.set_mode(stt.SCREEN_SCALE)
pygame.display.set_caption("GREEN BLOCK CATCHER")
screen_rect = screen.get_rect()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

# -- GAME OBJECTS
paddle = pygame.Rect(400, 550, 80, 10)
block = pygame.Rect(random.randint(0, stt.SCREEN_SCALE[0]-20), 0, 20, 20)
block_speed = stt.BLOCK_SPEED
running = True

score = 0

# -- MAIN LOOP
while running:
    # -- EVENTS
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # -- INPUT & MOVEMENT
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        paddle.x -= stt.PADDLE_SPEED
    if keys[K_RIGHT]:
        paddle.x += stt.PADDLE_SPEED

    block.y += block_speed

    # -- LOGIC
    if block.colliderect(paddle):
        block.y = 0
        block.x = random.randint(0, stt.SCREEN_SCALE[0]-20)
        block_speed += 0.5
        score += 1

    if block.y > stt.SCREEN_SCALE[1]:
        screen.fill(stt.BLACK)
        game_over = font.render(f"GAME OVER!\nSCORE: {score}", True, stt.RED)
        game_over_rect = game_over.get_rect(center=screen_rect.center)
        screen.blit(game_over, game_over_rect)
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    # -- BOUNDARIES (Keep paddle on screen)
    paddle.clamp_ip(screen_rect)
    
    # -- DRAWING OBJECTS
    screen.fill(stt.BLACK)
    pygame.draw.rect(screen, (stt.WHITE), paddle)
    pygame.draw.rect(screen, (stt.GREEN), block)
    
    score_text = font.render(f"Score: {score}", True, stt.WHITE)
    screen.blit(score_text, (10,10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()