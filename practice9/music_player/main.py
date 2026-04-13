import pygame
from player import MusicPlayer
pygame.init()
pygame.mixer.init()
WIDTH, HEIGHT=700,200
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")
font=pygame.font.Font(None, 40)
clock=pygame.time.Clock()

playlist=[
    "music/track1.mp3",
    "music/track2.mp3"
]
player=MusicPlayer(playlist)
running=True
while running:
    screen.fill((255,255,255))
    text=font.render(
        f"Now Playing: {player.get_current_track_name()}",
        True,
        (0,0,0)
    )
    screen.blit(text, (50,80))
    instructions=font.render("P Play | S Stop | N Next | B Back | Q Quit |", True, (0,0,0))
    screen.blit(instructions, (50,130))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_p:
                player.play()

            elif event.key==pygame.K_s:
                player.stop()

            elif event.key==pygame.K_n:
                player.next_track()
            
            elif event.key==pygame.K_b:
                player.previous_track()

            elif event.key==pygame.K_q:
                running=False
            
    clock.tick()
pygame.quit()


