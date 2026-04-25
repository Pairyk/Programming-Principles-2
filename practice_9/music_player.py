import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("UFOTUNES")
clock = pygame.time.Clock()
running = True

music = ["musics/bitbreaker - You Make Me Sick (Evil)(1).mp3", "musics/Серік Ибрагимов & Октем Алтаев - Ақ сәулем.mp3"]
index = 0

def play_current():
    pygame.mixer.music.load(music[index])
    pygame.mixer.music.play()

def next_song():
    global index
    index = (index+1) % len(music)
    play_current()

def previous_song():
    global index
    index = (index-1) % len(music)
    play_current()
    
def pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

play_current()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                previous_song()
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_SPACE:
                pause_music()
    
    screen.fill((50, 60, 185))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()