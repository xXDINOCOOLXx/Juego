import random
from constantess import *
import pygame
import os
import json

def mostrar_texto(surface, texto, posicion, fuente, color):
    words = [word.split(' ') for word in texto.splitlines()]  # 2D array where each row is a list of words.
    espacio = fuente.size(' ')[0]  # The width of a space.
    ancho_max, max_height = surface.get_size()
    x, y = posicion
    for line in words:
        for word in line:
            palabra_surface = fuente.render(word, False, color)
            ancho_palabra, alto_palabra = palabra_surface.get_size()
            if x + ancho_palabra >= ancho_max:
                x = posicion[0]  # Reset the x.
                y += alto_palabra  # Start on new row.
            surface.blit(palabra_surface, (x, y))
            x += ancho_palabra + espacio
        x = posicion[0]  # Reset the x.
        y += alto_palabra  # Start on new row.

def mezclar_lista(lista_preguntas:list) -> None:
    random.shuffle(lista_preguntas)

racha=0
def verificar_respuesta(datos_juego:dict,pregunta_actual:dict,respuesta:int) -> bool:
    global racha
    if respuesta == pregunta_actual["respuesta_correcta"]:
        datos_juego["puntuacion"] += ACIERTO
        racha+=1
        if racha==5:
            datos_juego["vidas"] += 1
            racha=0
        retorno = True
    else:
        #SIN PUNTOS NEGATIVOS
        if datos_juego["puntuacion"] > DESACIERTO:
            datos_juego["puntuacion"] -= DESACIERTO
            
        #CON PUNTOS NEGATIVOS
        #datos_juego["puntuacion"] -= PUNTUACION_ERROR
        
        datos_juego["vidas"] -= 1
        racha=0
        retorno = False
    
    return retorno

def reiniciar_estadisticas(datos_juego:dict)->None:
    datos_juego["puntuacion"] = 0
    datos_juego["vidas"] = VIDAS

def mover_objeto(personaje,corazon,letras:list=letras)->int:
    movio=False
    if personaje.y<600:
        if personaje.x>530 and personaje.x<670 :
            corazon.x=550
            corazon.y=520
            movio=True
            if movio==True :
                return 1
        elif personaje.x>796 and personaje.x<936:
            corazon.x=825
            corazon.y=520
            movio=True
            if movio==True :
                return 2
        elif personaje.x>1064 and personaje.x< 1204:
            corazon.x=1084
            corazon.y=520
            movio=True
            if movio==True :
                return 3
        elif personaje.x>1330 and personaje.x< 1470:
            corazon.x=1350
            corazon.y=520
            movio=True
            if movio==True :
                return 4

def estratosferar_objeto(objeto)->None:
    """
    Manda un objeto a donde no da la luz del sol
    """
    objeto.x=-100
    objeto.y=-100

def ubicar_imagenes(imagen, posición):     
    superficie=imagen.get_rect()
    superficie.x=posición[0]
    superficie.y=posición[1]
    return superficie

def chocar(personaje, personaje_vel_x,personaje_vel_y, ANCHO:int=1600, ALTO:int=900, paredes:list=paredes)->None:
    personaje.x += personaje_vel_x
    personaje.y += personaje_vel_y
    if personaje.x > ANCHO - personaje.width:
        personaje.x = ANCHO - personaje.width
    if personaje.x < 450:
        personaje.x = 450
    if personaje.y > ALTO - personaje.height:
        personaje.y = ALTO - personaje.height
    if personaje.y < 550:
        personaje.y = 550
    for pared in paredes:
        if personaje.colliderect(pared):
            personaje.x -= personaje_vel_x
            personaje.y -= personaje_vel_y

""" fuente = pygame.font.SysFont("Arial Narrow",32)
fuente_boton = pygame.font.SysFont("Arial Narrow",23)
boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(AZUL)

def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]):
    retorno = "rankings"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                print("VOLVER AL MENU")
                CLICK_SONIDO.play()
                retorno = "menu"
    
    pantalla.fill(BLANCO)
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    mostrar_texto(boton_volver["superficie"],"VOLVER",(10,10),fuente_boton,BLANCO)
    mostrar_texto(pantalla,f"ACA SE DEBE MOSTRAR EL TOP 10",(20,200),fuente,NEGRO)
    
    return retorno """

def crear_diccionario_pregunta(lista_valores: list) -> dict:
    pregunta = {}
    pregunta["pregunta"] = lista_valores[0].strip()
    pregunta["respuesta_1"] = lista_valores[1].strip()
    pregunta["respuesta_2"] = lista_valores[2].strip()
    pregunta["respuesta_3"] = lista_valores[3].strip()
    pregunta["respuesta_4"] = lista_valores[4].strip()
    pregunta["respuesta_correcta"] = int(lista_valores[5].strip())
    
    return pregunta

def leer_csv_preguntas(nombre_archivo: str, lista_preguntas: list) -> bool:
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            archivo.readline() 
            for linea in archivo:
                linea_aux = linea.strip()
                lista_valores = linea_aux.split(",")
                if len(lista_valores) == 6:
                    pregunta_aux = crear_diccionario_pregunta(lista_valores)
                    lista_preguntas.append(pregunta_aux)
                else:
                    return False 
        return True
    else:
        return False
    
def cargar_musica(volumen):
    porcentaje_volumen = volumen / 100
    pygame.mixer.music.load("sonidos/8bitRandom.mp3")
    pygame.mixer.music.set_volume(porcentaje_volumen)
    pygame.mixer.music.play(-1)

def obtener_top_10_partidas(nombre_archivo: str):
    if not os.path.exists(nombre_archivo):
        return []

    try:
        with open(nombre_archivo, "r") as archivo:
            partidas = json.load(archivo)
    except json.JSONDecodeError:
        print("El archivo JSON está vacío o tiene un formato incorrecto.")
        return []
    partidas_ordenadas = sorted(partidas, key=lambda x: x["puntaje"], reverse=True)

    return partidas_ordenadas[:10]