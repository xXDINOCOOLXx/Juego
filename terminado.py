import json
import pygame
import os
from datetime import datetime
from constantess import * 
from Funcioones import *

pygame.init()

fuente = pygame.font.SysFont("Arial Narrow", 40)
cuadro = {}
cuadro["superficie"] = pygame.Surface(CUADRO_TEXTO)
cuadro["rectangulo"] = cuadro["superficie"].get_rect()
#cuadro['superficie'].fill(AZUL)
boton_volver_imagen = pygame.image.load("imagenes/Botón volver.png")
boton_volver = {}
boton_volver["superficie"] = pygame.transform.scale(boton_volver_imagen, TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect(topleft=(15, 15))

nombre = ""
partida_guardada = False  
nombre_completo = False 

def guardar_partida(nombre_archivo: str, nombre: str, puntaje: int) -> None:
    global partida_guardada
    if partida_guardada:
        print(f"Ya se ha guardado la partida para {nombre}. No se guardará nuevamente.")
        return
    partida = {
        "nombre": nombre,
        "puntaje": puntaje,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    partidas = []
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, "r") as archivo:
                partidas = json.load(archivo)
        except json.JSONDecodeError:
            print("El archivo JSON está vacío o tiene un formato incorrecto. Se inicializará una nueva lista.")
    for partida_existente in partidas:
        if partida_existente["nombre"] == nombre: 
            print(f"Ya existe una partida guardada para {nombre}. No se agregará de nuevo.")
            return
    partidas.append(partida)
    with open(nombre_archivo, "w") as archivo:
        json.dump(partidas, archivo, indent=4)
    partida_guardada = True 
    print(f"Partida guardada correctamente para {nombre}.")
    
def mostrar_fin_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict) -> str:
    global nombre, partida_guardada, nombre_completo
    retorno = "terminado"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                print("VOLVER AL MENÚ")
                CLICK_SONIDO.play()
                retorno = "menu"
        elif evento.type == pygame.KEYDOWN:
            bloc_mayus = pygame.key.get_mods() & pygame.KMOD_CAPS 
            letra_presionada = pygame.key.name(evento.key)
            
            if letra_presionada == "backspace" and len(nombre) > 0:
                nombre = nombre[:-1]
                print(f"Nombre después de backspace: {nombre}") 

            elif letra_presionada == "space":
                nombre += " "
            elif len(letra_presionada) == 1:  
                if bloc_mayus != 0:
                    nombre += letra_presionada.upper()  
                else:
                    nombre += letra_presionada.lower() 

            if evento.key == pygame.K_RETURN and nombre != "":
                nombre_completo = True  

            if len(nombre) > 10:
                nombre = nombre[:10]
                print(f"Nombre recortado a 10 caracteres: {nombre}")
            #if evento.key == pygame.K_ESCAPE: 
            #    retorno = "salir"

    fondo_imagen = pygame.image.load("imagenes/Fondo menú.png")
    fondo_imagen = pygame.transform.scale(fondo_imagen, PANTALLA)
    pantalla.blit(fondo_imagen, (0, 0))

    cuadro["superficie"].fill(VIOLETA2)

    mostrar_texto(cuadro["superficie"], nombre, (10, 0), fuente, BLANCO)
    pantalla.blit(cuadro["superficie"], (200, 200)) 

    mostrar_texto(pantalla, f"Usted obtuvo: {datos_juego['puntuacion']} puntos", (250, 100), fuente, NEGRO)

    if nombre_completo and not partida_guardada: 
        guardar_partida("partidas.json", nombre, datos_juego["puntuacion"])

    pantalla.blit(boton_volver["superficie"], boton_volver["rectangulo"])

    return retorno