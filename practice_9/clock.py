import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((600, 600))
center_screen =  (300, 300)

clock = pygame.time.Clock()
running = True

# sprites
raw_sec_hand = pygame.image.load("imgs/4-2-pen-png-hd.png")
sec_hand  = pygame.transform.scale(raw_sec_hand, (200, 100))

raw_mint_hand = pygame.image.load("imgs/pngimg.com - spoon_PNG3043.png")
mint_hand = pygame.transform.scale(raw_mint_hand, (100, 200))

mint_extended = pygame.Surface((100, 400), pygame.SRCALPHA)
clock_extended = pygame.Surface((400, 100), pygame.SRCALPHA) 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 50, 255))

    # getting time
    time = datetime.datetime.now()
    sec = time.second
    mint = time.minute
    sec_rotation = (-6 * sec) - 90
    mint_rotation = (-0.1 * mint) 

    clock_extended_rotated = pygame.transform.rotate(clock_extended, sec_rotation)
    clock_extended_rect = clock_extended_rotated.get_rect(center=center_screen)

    mint_extended_rotated = pygame.transform.rotate(mint_extended, mint_rotation)
    mint_extended_rect = mint_extended_rotated.get_rect(center=center_screen)

    clock_extended.blit(sec_hand, (0, 0))
    mint_extended.blit(mint_hand, (0, 0))

    screen.blit(clock_extended_rotated, clock_extended_rect)
    screen.blit(mint_extended_rotated, mint_extended_rect)

    print(time)

    pygame.display.flip()
    clock.tick(60)

pygame.quit() 