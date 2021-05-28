import pygame
pygame.init ()
x = 400
y = 300

velocidade = 5
janela = pygame.display.set_mode((800,600))
pygame.display.pygame.display.set_caption("game rodando")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

            comandos = pygame.key.get_pressed()
            if comandos [pygame.k_up] :
                y-= velocidade
            if comandos [pygame.k_DOWN] :
                y+= velocidade
            if comandos [pygame.k_RIGHT] :
                X-= velocidade
            if comandos [pygame.k_left] :
                X+= velocidade
    pygame.draw.circle(janela, (0,255,0) ,(x,y), (400,300) , 50)
    pygame.display.update()

pygame.quit
