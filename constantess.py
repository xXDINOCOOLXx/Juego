import pygame

pygame.init()

# Colores
BLANCO = (255,255,255)
NEGRO = (0,0,0)
VERDE=(0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VIOLETA = (134,23,219)
VIOLETA2 = (60,20,185)
AMARILLO = (235,200,0)
NARANJA = (215,179,0)
CELESTE= (112,225,253)
# Medidas
ANCHO = 1600
ALTO = 900
PANTALLA = (ANCHO,ALTO)
TAMAÑO_BOTON = (420,70)
TAMAÑO_PREGUNTA = (350,150)
TAMAÑO_RESPUESTA = (300, 80)

# Corazones
LUGAR_cor_celeste =(36,770)
LUGAR_cor_rosa =(180,770)
LUGAR_cor_lila =(330,770)

#FPS
FPS = 60

# Sistema
VIDAS = 3
ACIERTO = 10
DESACIERTO= -10

#Menu
BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_PUNTUACIONES = 2
BOTON_SALIR = 3

#Configuración
TAMAÑO_BOTON_VOLUMEN = (120, 120)
TAMAÑO_BOTON_VOLVER = (210, 75)

#Terminado
CUADRO_TEXTO = (250,50)


# Imagenes
pasar_img=pygame.image.load("imagenes/flecha.png")
pasar_img=pygame.transform.scale(pasar_img, (60, 60))

puntos_img=pygame.image.load("imagenes/puntos.png")
puntos_img=pygame.transform.scale(puntos_img, (60, 60))
puntos_img.set_colorkey(BLANCO)

letra_a_img = pygame.image.load("imagenes/letra_a.png")
letra_a_img=pygame.transform.scale(letra_a_img, (110, 110))
letra_b_img = pygame.image.load("imagenes/letra_b.png")
letra_b_img=pygame.transform.scale(letra_b_img, (110, 110))
letra_c_img = pygame.image.load("imagenes/letra_c.png")
letra_c_img=pygame.transform.scale(letra_c_img, (110, 110))
letra_d_img = pygame.image.load("imagenes/letra_d.png")
letra_d_img=pygame.transform.scale(letra_d_img, (110, 110))

piedras_img = pygame.image.load("imagenes/piedrass.png")
#piedras_img=pygame.transform.scale(piedras_img, (140, 34))


img_cor_rosa = pygame.image.load("imagenes/corazón_rosa.png")
img_cor_celeste = pygame.image.load("imagenes/corazón_azul.png")
img_cor_lila = pygame.image.load("imagenes/corazón_violeta.png")
corazon_fondo=pygame.image.load("imagenes/corazón_fondo.png")
corazon_dx=pygame.image.load("imagenes/corazon_qepd.png")

img_cor=[img_cor_celeste,img_cor_rosa,img_cor_lila]

fondo = pygame.image.load("imagenes/fondito.png")

pj_imagen= pygame.image.load("imagenes/PJ1.png")
pj_imagen=pygame.transform.scale(pj_imagen, (105, 120))

fondo_carta_img = pygame.image.load("imagenes/CARTEL.png")
fondo_carta_img = pygame.transform.scale(fondo_carta_img, TAMAÑO_RESPUESTA)

cuadro_pregunta_img = pygame.image.load("imagenes/cuadro_pregunta.png")
cuadro_pregunta_img = pygame.transform.scale(cuadro_pregunta_img,TAMAÑO_PREGUNTA)

#ruido

CLICK_SONIDO = pygame.mixer.Sound("sonidos/click.mp3")
CLICK_SONIDO.set_volume(0.12)
click_grito1= pygame.mixer.Sound("sonidos/grito2.mp3")
click_grito1.set_volume(1)
click_grito2= pygame.mixer.Sound("sonidos/grito2.mp3")
click_grito2.set_volume(1)
click_grito3= pygame.mixer.Sound("sonidos/grito3.mp3")
click_grito3.set_volume(1)
gritos=[click_grito1,click_grito2, click_grito3]

# Datos

largo1 = pygame.Rect(450, 650, 80, 5)
largo2 = pygame.Rect(670, 650, 126, 5)
largo3 = pygame.Rect(936, 650, 138, 5)
largo4 = pygame.Rect(1204, 650, 126, 5)
largo5 = pygame.Rect(1470, 650, 130, 5)

punto1 = pygame.Rect(530, 600, 5, 60)
punto2 = pygame.Rect(670, 600, 5, 60)
punto3 = pygame.Rect(796, 600, 5, 60)
punto4 = pygame.Rect(936, 600, 5, 60)
punto5 = pygame.Rect(1064, 600, 5, 60)
punto6 = pygame.Rect(1204, 600, 5, 60)
punto7 = pygame.Rect(1330, 600, 5, 60)
punto8 = pygame.Rect(1470, 600, 5, 60)

paredes=[largo1,largo2,largo3,largo4,largo5,punto1,punto2,punto3,punto4,punto5,punto6,punto7,punto8]

lugar_texto = pygame.Rect(0, 0, 450, 900)
lugar_corazones = pygame.Rect(25, 755, 405, 100)

#Objetos

def ubicar_imagenes(imagen, posición):     
    superficie=imagen.get_rect()
    superficie.x=posición[0]
    superficie.y=posición[1]
    return superficie

centro = pygame.Rect(1025, 450, 8, 8)
letra_a=ubicar_imagenes(letra_a_img, (550,550))
letra_b=ubicar_imagenes(letra_b_img, (816,550))
letra_c=ubicar_imagenes(letra_c_img, (1084,550))
letra_d=ubicar_imagenes(letra_d_img, (1350,550))

letras=[letra_a,letra_b,letra_c,letra_d]

cor_celeste= ubicar_imagenes(img_cor_celeste, LUGAR_cor_celeste)
cor_rosa= ubicar_imagenes(img_cor_rosa, LUGAR_cor_rosa)
cor_lila= ubicar_imagenes(img_cor_lila, LUGAR_cor_lila)
corazones=[cor_celeste,cor_rosa,cor_lila]
corazon_activo=None

personaje=ubicar_imagenes(pj_imagen, (1025,800))
personaje_vel_x = 0
personaje_vel_y = 0

pasar=ubicar_imagenes(pasar_img,(130, 690))

puntos_extra=ubicar_imagenes(puntos_img, (300,685))