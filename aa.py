import pygame
from constantess import *

# Inicializar
pygame.init()


# Ventana
ventana = pygame.display.set_mode((1600, 900))
reloj = pygame.time.Clock()

# Imagenes
letra_a = pygame.image.load("letra_a.png")
letra_a.set_colorkey(BLANCO)
cor_rosa = pygame.image.load("rosa.png")
cor_rosa.set_colorkey(BLANCO)
cor_celeste = pygame.image.load("celeste.png").convert()
cor_celeste.set_colorkey(BLANCO)
cor_lila = pygame.image.load("lila.png")
cor_lila.set_colorkey(BLANCO)
fondo = pygame.image.load("bfondo.png")

corazones=[cor_lila,cor_celeste,cor_rosa]
# Datos

largo1 = pygame.Rect(400, 650, 150, 10)
largo2 = pygame.Rect(650, 650, 166, 10)
largo3 = pygame.Rect(916, 650, 170, 10)
largo4 = pygame.Rect(1184, 650, 166, 10)
largo5 = pygame.Rect(1450, 650, 150, 10)
punto1 = pygame.Rect(550, 600, 10, 60)
punto2 = pygame.Rect(650, 600, 10, 60)
punto3 = pygame.Rect(816, 600, 10, 60)
punto4 = pygame.Rect(916, 600, 10, 60)
punto5 = pygame.Rect(1084, 600, 10, 60)
punto6 = pygame.Rect(1184, 600, 10, 60)
punto7 = pygame.Rect(1350, 600, 10, 60)
punto8 = pygame.Rect(1450, 600, 10, 60)

paredes=[largo1,largo2,largo3,largo4,largo5,punto1,punto2,punto3,punto4,punto5,punto6,punto7,punto8]

lugar_texto = pygame.Rect(0, 0, 400, 900)


centro = pygame.Rect(1000, 450, 8, 8)



personaje = pygame.Rect(1500, 800, 50, 50)
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
            if event.key == pygame.K_ESCAPE:
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
        
        #Arrastrar corazones
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, corazones in enumerate(corazones):
                    if corazones.collidepoint(event.pos):
                        corazon_activo = num
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                corazon_activo = None
        if event.type == pygame.MOUSEMOTION:
            if corazon_activo != None:
                corazones[corazon_activo].move_ip(event.rel)



    # Lógica


    personaje.x += personaje_vel_x
    personaje.y += personaje_vel_y


    if personaje.x > ANCHO - personaje.width:
        personaje.x = ANCHO - personaje.width
    if personaje.x < 400:
        personaje.x = 400
    if personaje.y > ALTO - personaje.height:
        personaje.y = ALTO - personaje.height
    if personaje.y < 600:
        personaje.y = 600

    for pared in paredes:
        if personaje.colliderect(pared):
            personaje.x -= personaje_vel_x
            personaje.y -= personaje_vel_y
        #Dibujo paredes
        #pygame.draw.rect(ventana, NEGRO, pared)

    
    # Dibujos


    #ventana.fill((2,170,210))
    ventana.blit(fondo, (0,0))
    pygame.draw.rect(ventana, VIOLETA, lugar_texto)
    

    pygame.draw.rect(ventana, AZUL, personaje)


    ventana.blit(letra_a, (550,490))
    ventana.blit(letra_a, (816,490))
    ventana.blit(letra_a, (1084,490))
    ventana.blit(letra_a, (1350,490))
    
    ventana.blit(cor_celeste, (60,790))
    ventana.blit(cor_rosa, (160,790))
    ventana.blit(cor_lila, (260,790))

    for pared in paredes:
        #Dibujo paredes
        pygame.draw.rect(ventana, NEGRO, pared)



    # Actualizar
    pygame.display.update()

# Salir
pygame.quit()
