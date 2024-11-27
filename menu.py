import pygame
from constantess import *
from Funcioones import mostrar_texto

pygame.init()
lista_botones = []

imagenes_botones = [
    pygame.image.load("imagenes/Botón JUGARR.png"),
    pygame.image.load("imagenes/Botón OPCIONESS.png"),
    pygame.image.load("imagenes/Botón PUNTUACIONESS.png"),
    pygame.image.load("imagenes/Botón SALIRR.png"),
]

imagenes_botones = [pygame.transform.scale(img, TAMAÑO_BOTON) for img in imagenes_botones]

for i in range(4):
    boton = {}
    boton["superficie"] = imagenes_botones[i]
    boton["rectangulo"] = boton["superficie"].get_rect()
    lista_botones.append(boton)

def mostrar_menu(ventana:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
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

    fondo = pygame.image.load("imagenes/Fondo menú.png")
    ventana.blit(fondo, (0, 0))

    margen_superior = 375

    espacio_vertical = (PANTALLA[1] - margen_superior - len(lista_botones) * TAMAÑO_BOTON[1]) // (len(lista_botones) + 2)  

    for i, boton in enumerate(lista_botones):
        centro_x = (PANTALLA[0] - TAMAÑO_BOTON[0]) // 2 
        centro_y = margen_superior + i * (TAMAÑO_BOTON[1] + espacio_vertical)  

        boton["rectangulo"].topleft = (centro_x, centro_y)
        ventana.blit(boton["superficie"], boton["rectangulo"])

    return retorno