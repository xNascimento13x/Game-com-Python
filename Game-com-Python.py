import pygame
pygame.init ()

janela = pygame.display.set_mode((800,600))
pygame.display.pygame.display.set_caption("game rodando")
janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

pygame.drw.pygame.draw.circle(janela,(0,255,0) , (400,300) , 50)

pygame.display.update()

pygame.quit
