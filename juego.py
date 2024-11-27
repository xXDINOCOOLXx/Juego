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
bandera_respuesta = False

def mostrar_juego(ventana:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global indice
    global bandera_respuesta
    retorno = "juego"

    if datos_juego["vidas"] <= 0:
        if not bandera_respuesta: 
            retorno = "terminado"  
            bandera_respuesta = True  
        return retorno

    cuadro_pregunta["superficie"].fill(AMARILLO)
    for carta in cartas_respuestas:
        carta["superficie"].fill(VIOLETA)

    if bandera_respuesta:
        pygame.time.delay(500)
        bandera_respuesta = False

    pregunta_actual = lista_preguntas[indice]

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(cartas_respuestas)):
                if cartas_respuestas[i]['rectangulo'].collidepoint(evento.pos):
                    respuesta_usuario = (i + 1)
                    
                    if verificar_respuesta(datos_juego,pregunta_actual,respuesta_usuario):
                        CLICK_SONIDO.play()
                        cartas_respuestas[i]['superficie'].fill(VERDE)
                        print("RESPUESTA CORRECTA")
                    else:
                        CLICK_SONIDO.play()
                        cartas_respuestas[i]['superficie'].fill(ROJO)
                        print("RESPUESTA INCORRECTA")
                        datos_juego['vidas'] -= 1 
                        
                        if datos_juego['vidas'] <= 0:
                            retorno = "terminado" 
                            bandera_respuesta = True
                            break
                    print(f"SE HIZO CLICK EN UNA RESPUESTA {respuesta_usuario}")
                    bandera_respuesta = pygame.time.get_ticks()  
                    
                    if indice >= len(lista_preguntas):  
                        indice = 0
                        mezclar_lista(lista_preguntas)
                    else:
                        indice += 1

    mostrar_texto(cuadro_pregunta["superficie"], f"{pregunta_actual['pregunta']}", (20, 20), fuente_pregunta, NEGRO)

    mostrar_texto(cartas_respuestas[0]["superficie"], f"{pregunta_actual['respuesta_1']}", (20, 10), fuente_respuesta, BLANCO)
    mostrar_texto(cartas_respuestas[1]["superficie"], f"{pregunta_actual['respuesta_2']}", (20, 10), fuente_respuesta, BLANCO)
    mostrar_texto(cartas_respuestas[2]["superficie"], f"{pregunta_actual['respuesta_3']}", (20, 10), fuente_respuesta, BLANCO)
    mostrar_texto(cartas_respuestas[3]["superficie"], f"{pregunta_actual['respuesta_4']}", (20, 10), fuente_respuesta, BLANCO) 
    ventana.fill(BLANCO)
    ventana.blit(cuadro_pregunta["superficie"], (80, 80))

    cartas_respuestas[0]['rectangulo'] = ventana.blit(cartas_respuestas[0]['superficie'], (125, 245))
    cartas_respuestas[1]['rectangulo'] = ventana.blit(cartas_respuestas[1]['superficie'], (125, 315))
    cartas_respuestas[2]['rectangulo'] = ventana.blit(cartas_respuestas[2]['superficie'], (125, 385))
    cartas_respuestas[3]['rectangulo'] = ventana.blit(cartas_respuestas[3]['superficie'], (125, 455)) 

    mostrar_texto(ventana, f"PUNTUACION: {datos_juego['puntuacion']}", (10, 10), fuente_respuesta, NEGRO)
    mostrar_texto(ventana, f"VIDAS: {datos_juego['vidas']}", (10, 40), fuente_respuesta, NEGRO)

    pygame.display.update()

    return retorno
