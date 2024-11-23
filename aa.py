import pygame
from constantess import *

# Inicializar
pygame.init()
pygame.display.set_caption("Appa Fans")
pygame.display.set_icon(pygame.image.load("imagenes/appa.png"))
# Ventana
ventana = pygame.display.set_mode((1600, 900))
reloj = pygame.time.Clock()

# Imagenes
letra_a = pygame.image.load("imagenes/letra_a.png")
letra_a.set_colorkey(BLANCO)

img_cor_rosa = pygame.image.load("imagenes/corazón_rosa.png")
img_cor_celeste = pygame.image.load("imagenes/corazón_azul.png").convert_alpha()
img_cor_lila = pygame.image.load("imagenes/corazón_violeta.png").convert_alpha()

fondo = pygame.image.load("imagenes/bfondo.png")

pj_imagen= pygame.image.load("imagenes/PJ1.png")
pj_imagen=pygame.transform.scale(pj_imagen, (105, 120))
# Datos

largo1 = pygame.Rect(450, 650, 80, 10)
largo2 = pygame.Rect(670, 650, 126, 10)
largo3 = pygame.Rect(936, 650, 138, 10)
largo4 = pygame.Rect(1204, 650, 126, 10)
largo5 = pygame.Rect(1470, 650, 130, 10)
punto1 = pygame.Rect(530, 600, 10, 60)
punto2 = pygame.Rect(670, 600, 10, 60)
punto3 = pygame.Rect(796, 600, 10, 60)
punto4 = pygame.Rect(936, 600, 10, 60)
punto5 = pygame.Rect(1064, 600, 10, 60)
punto6 = pygame.Rect(1204, 600, 10, 60)
punto7 = pygame.Rect(1330, 600, 10, 60)
punto8 = pygame.Rect(1470, 600, 10, 60)

paredes=[largo1,largo2,largo3,largo4,largo5,punto1,punto2,punto3,punto4,punto5,punto6,punto7,punto8]

lugar_texto = pygame.Rect(0, 0, 450, 900)
lugar_corazones = pygame.Rect(25, 755, 405, 100)


centro = pygame.Rect(1000, 450, 8, 8)

cor_celeste=img_cor_celeste.get_rect()
cor_celeste.x=LUGAR_cor_celeste[0]
cor_celeste.y=LUGAR_cor_celeste[1]

cor_rosa=img_cor_rosa.get_rect()
cor_rosa.x=LUGAR_cor_rosa[0]
cor_rosa.y=LUGAR_cor_rosa[1]
cor_lila=img_cor_lila.get_rect()

cor_lila.x=LUGAR_cor_lila[0]
cor_lila.y=LUGAR_cor_lila[1]
corazones=[cor_celeste,cor_rosa,cor_lila]



personaje = pj_imagen.get_rect()
personaje.x=1500
personaje.y=800

personaje_vel_x = 0
personaje_vel_y = 0


corazon_activo=None

# Bucle principal
jugando = True
while jugando:

    reloj.tick(60)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # que vaya al menú en vez de salir diría¿
                jugando = False
            if event.key == pygame.K_RIGHT:
                personaje_vel_x = 7
            if event.key == pygame.K_LEFT:
                personaje_vel_x = -7
            if event.key == pygame.K_DOWN:
                personaje_vel_y = 7
            if event.key == pygame.K_UP:
                personaje_vel_y = -7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                personaje_vel_x = 0
            if event.key == pygame.K_LEFT:
                personaje_vel_x = 0
            if event.key == pygame.K_DOWN:
                personaje_vel_y = 0
            if event.key == pygame.K_UP:
                personaje_vel_y = 0        
        
        """ #Arrastrar corazones
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, corazones in enumerate(corazones):
                    if corazones.collidepoint(event.pos):
                        corazon_activo = num
            if event.type == pygame.MOUSEBUTTONUP:
                corazon_activo = None """
        



    # Lógica

    personaje.x += personaje_vel_x
    personaje.y += personaje_vel_y
    

    if personaje.x > ANCHO - personaje.width:
        personaje.x = ANCHO - personaje.width
    if personaje.x < 400:
        personaje.x = 400
    if personaje.y > ALTO - personaje.height:
        personaje.y = ALTO - personaje.height
    if personaje.y < 550:
        personaje.y = 550

    for pared in paredes:
        if personaje.colliderect(pared):
            personaje.x -= personaje_vel_x
            personaje.y -= personaje_vel_y

    
    # Dibujos

    ventana.blit(fondo, (0,0))
    pygame.draw.rect(ventana,AMARILLO, lugar_texto)
    pygame.draw.rect(ventana,NARANJA, lugar_corazones)
    
    #ventana.blit(superficie, (1400,500))
    ventana.blit(pj_imagen, personaje)

    ventana.blit(letra_a, (550,490))
    ventana.blit(letra_a, (816,490))
    ventana.blit(letra_a, (1084,490))
    ventana.blit(letra_a, (1350,490))
    
    ventana.blit(img_cor_celeste, cor_celeste)
    ventana.blit(img_cor_rosa, LUGAR_cor_rosa)
    ventana.blit(img_cor_lila, LUGAR_cor_lila)

    for pared in paredes:
        #Dibujo paredes
        pygame.draw.rect(ventana, NEGRO, pared)

    
    # Actualizar
    pygame.display.update()
    

# Salir
pygame.quit()
