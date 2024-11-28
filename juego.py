import pygame
from constantess import *
from Funcioones import *
from terminado import *
import random


lista_preguntas = []
if leer_csv_preguntas("preguntas.csv", lista_preguntas):
    mezclar_lista(lista_preguntas)

# Inicializar
pygame.init()
pygame.display.set_caption("Appa Fans")
pygame.display.set_icon(pygame.image.load("imagenes/appa.png"))

cuadro_pregunta = {}
cuadro_pregunta["superficie"] = pygame.Surface(TAMAÑO_PREGUNTA)
cuadro_pregunta["rectangulo"] = cuadro_pregunta["superficie"].get_rect()

cartas_respuestas = []
for i in range(4):
    cuadro_respuesta = {}
    cuadro_respuesta["superficie"] = pygame.Surface(TAMAÑO_RESPUESTA)
    cuadro_respuesta["rectangulo"] = cuadro_respuesta["superficie"].get_rect()
    cartas_respuestas.append(cuadro_respuesta)

fuente_pregunta = pygame.font.Font("fuentes/VCR_OSD_MONO_1.001.ttf", 32)
fuente_respuesta = pygame.font.Font("fuentes/VCR_OSD_MONO_1.001.ttf", 32)
fuente_respuesta.set_bold(True)
indice = 0
#bandera_respuesta = False
personaje_vel_x = 0
personaje_vel_y = 0
bandera_tiempo=True
empieza=0
##################################################
def mostrar_juego(ventana:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global indice
    #global bandera_respuesta
    global personaje_vel_x
    global personaje_vel_y
    global bandera_tiempo
    global empieza
    retorno = "juego"
    respuesta_usuario=None
    corazon_activo=None
    if bandera_tiempo:
        empieza=pygame.time.get_ticks() 
        bandera_tiempo=False    
    segundos=(pygame.time.get_ticks()-empieza)/1000 #calculate how many seconds
    if segundos>16:
            datos_juego["vidas"] -= 1
            lol.play
            indice+=1
            empieza=pygame.time.get_ticks() 
    
    if datos_juego["vidas"] <= 0:
        #if not bandera_respuesta:         ##esto parece borrable
            retorno = "terminado"  
            #bandera_respuesta = True  
            return retorno

    cuadro_pregunta["superficie"].fill(AMARILLO)
    for carta in cartas_respuestas:
        carta["superficie"].fill(VIOLETA)

    """ if bandera_respuesta:
        pygame.time.delay(500)
        bandera_respuesta = False """

    pregunta_actual = lista_preguntas[indice]
    #respuesta=lugar_respuesta(personaje)
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        if evento.type == pygame.MOUSEBUTTONDOWN:
            bandera_sonido_click=True
            if pasar.collidepoint(evento.pos):
                indice+=1
                empieza=pygame.time.get_ticks()
                estratosferar_objeto(pasar)
            if puntos_extra.collidepoint(evento.pos):
                chance=True
                estratosferar_objeto(puntos_extra)
            for num, corazon in enumerate(corazones):
                if corazon.collidepoint(evento.pos):
                    corazon_activo = num
                    bandera_sonido_click=False
                    gritos[random.randint(0,2)].play()
                    print(f"{num}")
                    respuesta_usuario=mover_objeto(personaje,corazon)
                    print(respuesta_usuario)
            if bandera_sonido_click== True:
                CLICK_SONIDO.play()
        if evento.type == pygame.MOUSEBUTTONUP:
            corazon_activo = None
        #Movimiento
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE: 
                retorno = "menu"
            if evento.key == pygame.K_RIGHT:
                personaje_vel_x = 10
            if evento.key == pygame.K_LEFT:
                personaje_vel_x = -10
            if evento.key == pygame.K_DOWN:
                personaje_vel_y = 10
            if evento.key == pygame.K_UP:
                personaje_vel_y = -10
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                personaje_vel_x = 0
            if evento.key == pygame.K_LEFT:
                personaje_vel_x = 0
            if evento.key == pygame.K_DOWN:
                personaje_vel_y = 0
            if evento.key == pygame.K_UP:
                personaje_vel_y = 0        

    # Límites
    chocar (personaje, personaje_vel_x,personaje_vel_y)
    

    ventana.blit(fondo, (0,0))
    pygame.draw.rect(ventana,AMARILLO, lugar_texto)
    pygame.draw.rect(ventana,NARANJA, lugar_corazones)
    mostrar_texto(cuadro_pregunta["superficie"], f"{pregunta_actual['pregunta']}", (20, 20), fuente_pregunta, NEGRO)

    mostrar_texto(cartas_respuestas[0]["superficie"], f"{pregunta_actual['respuesta_1']}", (20, 10), fuente_respuesta, BLANCO)
    mostrar_texto(cartas_respuestas[1]["superficie"], f"{pregunta_actual['respuesta_2']}", (20, 10), fuente_respuesta, BLANCO)
    mostrar_texto(cartas_respuestas[2]["superficie"], f"{pregunta_actual['respuesta_3']}", (20, 10), fuente_respuesta, BLANCO)
    mostrar_texto(cartas_respuestas[3]["superficie"], f"{pregunta_actual['respuesta_4']}", (20, 10), fuente_respuesta, BLANCO) 
    ventana.blit(cuadro_pregunta["superficie"], (80, 80))

    cartas_respuestas[0]['rectangulo'] = ventana.blit(cartas_respuestas[0]['superficie'], (125, 245))
    cartas_respuestas[1]['rectangulo'] = ventana.blit(cartas_respuestas[1]['superficie'], (125, 315))
    cartas_respuestas[2]['rectangulo'] = ventana.blit(cartas_respuestas[2]['superficie'], (125, 385))
    cartas_respuestas[3]['rectangulo'] = ventana.blit(cartas_respuestas[3]['superficie'], (125, 455)) 

    mostrar_texto(ventana, f"PUNTUACION: {datos_juego['puntuacion']}", (10, 10), fuente_respuesta, NEGRO)
    mostrar_texto(ventana, f"VIDAS: {datos_juego['vidas']}", (10, 40), fuente_respuesta, NEGRO)
    mostrar_texto(ventana, str(int(16-segundos)), (390, 10), fuente_respuesta, NEGRO)
    
    #for i in range(len(cartas_respuestas)):
                        
    if respuesta_usuario:
        if verificar_respuesta(datos_juego,pregunta_actual,respuesta_usuario):
            cartas_respuestas[respuesta_usuario-1]['superficie'].fill(VERDE)
            if chance:
                datos_juego["puntuacion"] += ACIERTO
                chance=False
            print("RESPUESTA CORRECTA")
        else:
            cartas_respuestas[respuesta_usuario-1]['superficie'].fill(ROJO)
            print("RESPUESTA INCORRECTA")
            
            if datos_juego['vidas'] <= 0:
                retorno = "terminado" 
                #bandera_respuesta = True
                #break
            
            estratosferar_objeto(corazones[corazon_activo])
        
        print(f"SE HIZO CLICK EN UNA RESPUESTA {respuesta_usuario}")
        #bandera_respuesta = pygame.time.get_ticks()  
        
        if indice >= len(lista_preguntas):  
            indice = 0
            mezclar_lista(lista_preguntas)
        else:
            indice += 1
            empieza=pygame.time.get_ticks() 
    
    ventana.blit(pj_imagen, personaje)

    ventana.blit(letra_a_img, letra_a)
    ventana.blit(letra_a_img, letra_b)
    ventana.blit(letra_a_img, letra_c)
    ventana.blit(letra_a_img, letra_d)
    
    ventana.blit(corazon_fondo, LUGAR_cor_celeste)
    ventana.blit(corazon_fondo, LUGAR_cor_rosa)
    ventana.blit(corazon_fondo, LUGAR_cor_lila)
    ventana.blit(img_cor_celeste, cor_celeste)
    ventana.blit(img_cor_rosa, cor_rosa)
    ventana.blit(img_cor_lila, cor_lila)

    #Comodines
    ventana.blit(pasar_img,pasar)
    ventana.blit(puntos_img,puntos_extra)

    for pared in paredes:
        pygame.draw.rect(ventana, NEGRO, pared)
    
    pygame.display.update()

    return retorno