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
AMARILLO = (235,200,0)
NARANJA = (215,179,0)
# Medidas
ANCHO = 1600
ALTO = 900

# Corazones
LUGAR_cor_celeste =(36,770)
LUGAR_cor_rosa =(180,770)
LUGAR_cor_lila =(330,770)


# Sistema
VIDAS = 3
ACIERTO = 10
DESACIERTO= -10

#Menu
BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_PUNTUACIONES = 2


#ruido

CLICK_SONIDO = pygame.mixer.Sound("sonidos/click.mp3")
CLICK_SONIDO.set_volume(0.12)
click2= pygame.mixer.Sound("sonidos/sus.mp3")
click2.set_volume(0.1)

