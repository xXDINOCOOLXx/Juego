import random
from constantess import *
import pygame

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
    
def verificar_respuesta(datos_juego:dict,pregunta_actual:dict,respuesta:int) -> bool:
    if respuesta == pregunta_actual["respuesta_correcta"]:
        datos_juego["puntuacion"] += ACIERTO
        retorno = True
    else:
        #SIN PUNTOS NEGATIVOS
        if datos_juego["puntuacion"] > DESACIERTO:
            datos_juego["puntuacion"] -= DESACIERTO
            
        #CON PUNTOS NEGATIVOS
        #datos_juego["puntuacion"] -= PUNTUACION_ERROR
        
        datos_juego["vidas"] -= 1
        retorno = False
    
    return retorno
    
def reiniciar_estadisticas(datos_juego:dict):
    datos_juego["puntuacion"] = 0
    datos_juego["vidas"] = VIDAS





# MENU
TAMAÑO_BOTON = (250,60) # borrar
BOTON_SALIR = 3 #borrar

pygame.init()
#boton_jugar = pygame.image.load("imagenes/boton_jugar.png")

fuente_menu = pygame.font.SysFont("Arial Narrow",30)
lista_botones = []
for i in range(4):
    boton = {}
    boton["superficie"] = pygame.Surface(TAMAÑO_BOTON)
    boton["superficie"].fill(AZUL)
    boton["rectangulo"] = boton["superficie"].get_rect()
    lista_botones.append(boton)

fondo = pygame.image.load("fondo.jpg")
fondo = pygame.transform.scale(fondo,ANCHO,ALTO)

def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event])-> str:
    #Gestionar eventos:
    retorno = "menu"
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(lista_botones)): 
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    if i == BOTON_SALIR:
                        retorno = "salir"  
                    elif i == BOTON_JUGAR:
                        retorno = "juego"  
                    elif i == BOTON_PUNTUACIONES:
                        retorno = "rankings"
                    elif i == BOTON_CONFIG:
                        retorno = "configuraciones"        
        elif evento.type == pygame.QUIT:
            retorno = "salir"
                
    #Actualizar el juego:
    
    #Dibujar pantalla y las otras superficies
    #pantalla.fill(COLOR_BLANCO)
    pantalla.blit(fondo,(0,0))
    
    lista_botones[0]["rectangulo"] = pantalla.blit(lista_botones[0]["superficie"],(125,115))
    lista_botones[1]["rectangulo"] = pantalla.blit(lista_botones[1]["superficie"],(125,195))
    lista_botones[2]["rectangulo"] = pantalla.blit(lista_botones[2]["superficie"],(125,275))
    lista_botones[3]["rectangulo"] = pantalla.blit(lista_botones[3]["superficie"],(125,355))
    mostrar_texto(lista_botones[0]["superficie"],"JUGAR",(80,10),fuente_menu,BLANCO)
    mostrar_texto(lista_botones[1]["superficie"],"CONFIGURACION",(20,10),fuente_menu,BLANCO)
    mostrar_texto(lista_botones[2]["superficie"],"PUNTUACIONES",(25,10),fuente_menu,BLANCO)
    mostrar_texto(lista_botones[3]["superficie"],"SALIR",(80,10),fuente_menu,BLANCO)
    
    return retorno

#RAnkings
TAMAÑO_BOTON_VOLVER = (100,40) # es de constantes


fuente = pygame.font.SysFont("Arial Narrow",32)
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
    
    return retorno
                
    
    