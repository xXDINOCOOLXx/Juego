import pygame
pygame.init()

# Colores
BLANCO = (255,255,255)
NEGRO = (0,0,0)
VERDE=(0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VIOLETA = (134,23,219)
VIOLETA2 = (104,0,209)

# Medidas
ANCHO = 1600
ALTO = 900


# Sistema
VIDAS = 3
ACIERTO = 10
DESACIERTO= -10

#Menu
BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_PUNTUACIONES = 2


#ruido

CLICK_SONIDO = pygame.mixer.Sound("click.mp3")
