import pygame
from constantess import * 
from Funcioones import *   

pygame.init()

boton_volver_imagen = pygame.image.load("imagenes/Botón volver.png")
boton_volver = {}
boton_volver["superficie"] = pygame.transform.scale(boton_volver_imagen, TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect(topleft=(15, 15))

fuente = pygame.font.SysFont("Arial Narrow", 32)
fuente_boton = pygame.font.SysFont("Arial Narrow", 23)

def mostrar_top_10(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], nombre_archivo: str):
    retorno = "rankings"
    top_10 = obtener_top_10_partidas(nombre_archivo) 
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            print(f"Clic detectado en la posición: {evento.pos}")
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                print("Clic dentro del botón, VOLVER AL MENU")
                CLICK_SONIDO.play()
                retorno = "menu"

    fondo_imagen = pygame.image.load("imagenes/Fondo menú.png")
    fondo_imagen = pygame.transform.scale(fondo_imagen, PANTALLA)
    pantalla.blit(fondo_imagen, (0, 0))

    fuente_top = pygame.font.SysFont("Arial Narrow", 40)
    y_pos = 50  
    mostrar_texto(pantalla, "TOP 10 Partidas", (250, 10), fuente_top, BLANCO)
    
    for idx, partida in enumerate(top_10):
        mostrar_texto(pantalla, f"{idx + 1}. {partida['nombre']} - {partida['puntaje']} puntos", (250, y_pos), fuente_top, BLANCO)
        y_pos += 50 

    pantalla.blit(boton_volver["superficie"], boton_volver["rectangulo"])

    pygame.display.flip()

    return retorno
