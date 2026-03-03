import pygame
import sys
import random

pygame.init()

LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Colisão de Objetos")

PRETO = (0, 0, 0)
FONTE = pygame.font.SysFont(None, 50)

clock = pygame.time.Clock()


class Texto:
    def __init__(self, mensagem, x, y):
        self.mensagem = mensagem
        self.cor = self.cor_aleatoria()
        self.surface = FONTE.render(self.mensagem, True, self.cor)
        self.rect = self.surface.get_rect(topleft=(x, y))
        self.vel_x = random.choice([-3, 3])
        self.vel_y = random.choice([-3, 3])

    def cor_aleatoria(self):
        return (
            random.randint(1, 255),
            random.randint(1, 255),
            random.randint(1, 255),
        )

    def mudar_cor(self):
        self.cor = self.cor_aleatoria()
        self.surface = FONTE.render(self.mensagem, True, self.cor)

    def mover(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def verificar_parede(self):
        if self.rect.right >= LARGURA or self.rect.left <= 0:
            self.vel_x *= -1
            self.mudar_cor()

        if self.rect.bottom >= ALTURA or self.rect.top <= 0:
            self.vel_y *= -1
            self.mudar_cor()

    def desenhar(self, tela):
        tela.blit(self.surface, self.rect)


texto1 = Texto("VAMO", 100, 100)
texto2 = Texto("GREMIO", 500, 400)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    TELA.fill(PRETO)

    texto1.mover()
    texto2.mover()

    texto1.verificar_parede()
    texto2.verificar_parede()

    if texto1.rect.colliderect(texto2.rect):
        texto1.vel_x, texto2.vel_x = texto2.vel_x, texto1.vel_x
        texto1.vel_y, texto2.vel_y = texto2.vel_y, texto1.vel_y
        texto1.mudar_cor()
        texto2.mudar_cor()

    texto1.desenhar(TELA)
    texto2.desenhar(TELA)

    pygame.display.flip()
    clock.tick(512)

pygame.quit()
sys.exit()