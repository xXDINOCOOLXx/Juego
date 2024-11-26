import pygame
from constantess import *
from Funcioones import *
import random

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
img_cor_celeste = pygame.image.load("imagenes/corazón_azul.png")
img_cor_lila = pygame.image.load("imagenes/corazón_violeta.png")
corazon_fondo=pygame.image.load("imagenes/corazón_fondo.png")

fondo = pygame.image.load("imagenes/fondo.png")

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


centro = pygame.Rect(1025, 450, 8, 8)

cor_celeste= ubicar_imagenes(img_cor_celeste, LUGAR_cor_celeste)
cor_rosa= ubicar_imagenes(img_cor_rosa, LUGAR_cor_rosa)
cor_lila= ubicar_imagenes(img_cor_lila, LUGAR_cor_lila)
corazones=[cor_celeste,cor_rosa,cor_lila]
corazon_activo=None

personaje=ubicar_imagenes(pj_imagen, (1025,800))
personaje_vel_x = 0
personaje_vel_y = 0


# Bucle principal
jugando = True
while jugando:

    reloj.tick(60)

    respuesta=lugar_respuesta(personaje)
    #respondio=False
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
        
        #Click y click corazones
        if event.type == pygame.MOUSEBUTTONDOWN:
            bandera=True
            if event.button == 1:
                for num, corazon in enumerate(corazones):
                    if corazon.collidepoint(event.pos):
                        corazon_activo = num
                        bandera=False
                        gritos[random.randint(0,2)].play()
                        print(num)
                        if respuesta!= None: #and respondio==False:
                            mover_objeto(respuesta,corazon)
                            #respondio=True
            if event.button==3:
                if personaje.collidepoint(event.pos):
                    print("p")
                    if respuesta!=None:
                        mover_objeto(respuesta,personaje)

            if bandera== True:
                CLICK_SONIDO.play()
        if event.type == pygame.MOUSEBUTTONUP:
            corazon_activo = None
        
#    if respuesta!=None and corazon_activo!=None:
#        if respuesta=="D":
#            print("a")
#            cor_celeste.x=550
#            cor_celeste.y=490
            #corazones[corazon_activo].x=550
            #corazones[corazon_activo].y=490
    #mover_corazon(corazon_activo,corazones,respuesta)


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
    #ventana.fill(BLANCO)
    ventana.blit(fondo, (0,0))
    pygame.draw.rect(ventana,AMARILLO, lugar_texto)
    pygame.draw.rect(ventana,NARANJA, lugar_corazones)
    
    
    ventana.blit(pj_imagen, personaje)

    ventana.blit(letra_a, (550,490))
    ventana.blit(letra_a, (816,490))
    ventana.blit(letra_a, (1084,490))
    ventana.blit(letra_a, (1350,490))
    
    ventana.blit(corazon_fondo, LUGAR_cor_celeste)
    ventana.blit(corazon_fondo, LUGAR_cor_rosa)
    ventana.blit(corazon_fondo, LUGAR_cor_lila)
    ventana.blit(img_cor_celeste, cor_celeste)
    ventana.blit(img_cor_rosa, cor_rosa)
    ventana.blit(img_cor_lila, cor_lila)

    for pared in paredes:
        #Dibujo paredes
        pygame.draw.rect(ventana, NEGRO, pared)

    """ aparecer= {[fondo,img_cor_celeste,img_cor_lila,img_cor_rosa,letra_a,letra_a,letra_a,letra_a,pj_imagen],
            [(0,0), LUGAR_cor_celeste,LUGAR_cor_lila, LUGAR_cor_rosa, (550,490),(816,490),(1084,490),(1350,490),personaje]} """
    
    
    # Actualizar
    pygame.display.update()

# Salir
pygame.quit()
