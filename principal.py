import pygame
from constantess import *
from Funcioones import *
import random
from menu import *
from juego import *
from configuración import *
from terminado import *
from rankings import *

# Inicializar
pygame.init()
pygame.display.set_caption("Appa Fans")
pygame.display.set_icon(pygame.image.load("imagenes/appa.png"))
ventana = pygame.display.set_mode(PANTALLA)
reloj = pygame.time.Clock()
datos_juego = {"puntuacion":0,"vidas":VIDAS,"nombre":"","volumen_musica":100}
jugando = True
ventana_actual = "menu"

pygame.mixer.music.load("sonidos/8bitRandom.mp3")
pygame.mixer.music.set_volume(datos_juego["volumen_musica"] / 100)
pygame.mixer.music.play(-1)  
bandera_musica = True


while jugando:
    reloj.tick(FPS)
    cola_eventos = pygame.event.get()

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            jugando = False 
    #Menú
    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(ventana,cola_eventos)
    elif ventana_actual == "juego":
        ventana_actual = mostrar_juego(ventana,cola_eventos,datos_juego)
    elif ventana_actual == "configuraciones":
        ventana_actual, bandera_musica = mostrar_configuracion(ventana, cola_eventos, datos_juego, bandera_musica)
        if not bandera_musica: 
            pygame.mixer.music.stop()
        else:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(-1)
    elif ventana_actual == "terminado":
        ventana_actual = mostrar_fin_juego(ventana,cola_eventos,datos_juego)
    elif ventana_actual == "rankings":
        ventana_actual = mostrar_top_10(ventana, cola_eventos, "partidas.json")
    elif ventana_actual == "salir":
        jugando = False

    pygame.display.flip()

pygame.quit()
exit()
