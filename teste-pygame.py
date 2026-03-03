import pygame
import sys
import random

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Colisão de Objetos')

PRETO = (0, 0, 0)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto1 = fonte.render("VAMO", True, (255, 0, 0))
texto1_rect = texto1.get_rect(x=100, y=100)
vel_x1 = random.choice([-1, 1])
vel_y1 = random.choice([-1, 1])

texto2 = fonte.render("GREMIO", True, (0, 255, 0))
texto2_rect = texto2.get_rect(x=500, y=400)
vel_x2 = random.choice([-1, 1])
vel_y2 = random.choice([-1, 1])

clock = pygame.time.Clock()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(PRETO)

    tela.blit(texto1, texto1_rect)
    texto1_rect.x += vel_x1
    texto1_rect.y += vel_y1

    if texto1_rect.right >= largura:
        vel_x1 = -1
        texto1 = fonte.render("VAMO", True, (random.randint(1,255), random.randint(1,255), random.randint(1,255)))
    if texto1_rect.left <= 0:
        vel_x1 = 1
        texto1 = fonte.render("VAMO", True, (random.randint(1,255), random.randint(1,255), random.randint(1,255)))
    if texto1_rect.bottom >= altura:
        vel_y1 = -1
        texto1 = fonte.render("VAMO", True, (random.randint(1,255), random.randint(1,255), random.randint(1,255)))
    if texto1_rect.top <= 0:
        vel_y1 = 1
        texto1 = fonte.render("VAMO", True, (random.randint(1,255), random.randint(1,255), random.randint(1,255)))

    tela.blit(texto2, texto2_rect)
    texto2_rect.x += vel_x2
    texto2_rect.y += vel_y2

    if texto2_rect.right >= largura:
        vel_x2 = -1
        texto2 = fonte.render("GREMIO", True, (random.randint(1,255), random.randint(1,255), random.randint(1,255)))
    if texto2_rect.left <= 0:
        vel_x2 = 1
        texto2 = fonte.render("GREMIO", True, (random.randint(1,255), random.randint(1,255), random.randint(1,255)))
    if texto2_rect.bottom >= altura:
        vel_y2 = -1
        texto2 = fonte.render("GREMIO", True, (random.randint(1,255), random.randint(1,255), random.randint(1,255)))
    if texto2_rect.top <= 0:
        vel_y2 = 1
        texto2 = fonte.render("GREMIO", True, (random.randint(1,255), random.randint(1,255), random.randint(1,255)))

    if texto1_rect.colliderect(texto2_rect):
        vel_x1, vel_x2 = vel_x2, vel_x1
        vel_y1, vel_y2 = vel_y2, vel_y1
        texto1 = fonte.render("VAMO", True, (random.randint(1,255), random.randint(1,255), random.randint(1,255)))
        texto2 = fonte.render("GREMIO", True, (random.randint(1,255), random.randint(1,255), random.randint(1,255)))

    clock.tick(512)
    pygame.display.flip()

pygame.quit()
sys.exit()