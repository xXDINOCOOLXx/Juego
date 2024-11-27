import pygame
from constantess import *
from Funcioones import mostrar_texto


pygame.init()

boton_suma_imagen = pygame.image.load("imagenes/Botón volumen +.png")
boton_resta_imagen = pygame.image.load("imagenes/Botón volumen -.png")
boton_volver_imagen = pygame.image.load("imagenes/Botón volver.png")
boton_musica_imagen = pygame.image.load("imagenes/Botón mute.png")

boton_suma = {}
boton_suma["superficie"] = pygame.transform.scale(boton_suma_imagen, TAMAÑO_BOTON_VOLUMEN)
boton_suma["rectangulo"] = boton_suma["superficie"].get_rect()
boton_resta = {}
boton_resta["superficie"] = pygame.transform.scale(boton_resta_imagen, TAMAÑO_BOTON_VOLUMEN)
boton_resta["rectangulo"] = boton_resta["superficie"].get_rect()
boton_musica = {}
boton_musica["superficie"] = pygame.transform.scale(boton_musica_imagen, TAMAÑO_BOTON_VOLUMEN)
boton_musica["rectangulo"] = boton_resta["superficie"].get_rect()
boton_volver = {}
boton_volver["superficie"] = pygame.transform.scale(boton_volver_imagen, TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()

fuente_volumen = pygame.font.Font("fuentes/VCR_OSD_MONO_1.001.ttf", 50)

def actualizar_volumen_musica(datos_juego):
    porcentaje_volumen = datos_juego["volumen_musica"] / 100
    pygame.mixer.music.set_volume(porcentaje_volumen)

def mostrar_configuracion(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict,bandera_musica:bool) -> str:
    retorno = "configuraciones"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_suma["rectangulo"].collidepoint(evento.pos):
                print("SUMA VOLUMEN")
                if datos_juego["volumen_musica"] < 100:
                    datos_juego["volumen_musica"] += 5
                    actualizar_volumen_musica(datos_juego)
                CLICK_SONIDO.play()
            elif boton_resta["rectangulo"].collidepoint(evento.pos):
                print("RESTA VOLUMEN")
                if datos_juego["volumen_musica"] > 5:
                    datos_juego["volumen_musica"] -= 5
                    actualizar_volumen_musica(datos_juego)
                CLICK_SONIDO.play()
            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                print("VOLVER AL MENU")
                CLICK_SONIDO.play()
                retorno = "menu"
            elif boton_musica["rectangulo"].collidepoint(evento.pos): 
                print("MUTE MUSICA")
                if bandera_musica:
                    pygame.mixer.music.stop()
                    bandera_musica = False
                    boton_musica["superficie"] = pygame.image.load("imagenes/Botón mute.png")
                else:
                    pygame.mixer.music.load("sonidos/8bitRandom.mp3")
                    pygame.mixer.music.play(-1)
                    actualizar_volumen_musica(datos_juego)
                    bandera_musica = True
                    boton_musica["superficie"] = pygame.image.load("imagenes/Botón volumen on.png")
                CLICK_SONIDO.play()

    if bandera_musica:
        boton_musica["superficie"] = pygame.transform.scale(pygame.image.load("imagenes/Botón mute.png"), TAMAÑO_BOTON_VOLUMEN)
    else:
        boton_musica["superficie"] = pygame.transform.scale(pygame.image.load("imagenes/Botón volumen on.png"), TAMAÑO_BOTON_VOLUMEN)

    boton_musica["rectangulo"] = boton_musica["superficie"].get_rect()

    fondo_imagen = pygame.image.load("imagenes/Fondo menú.png")
    fondo_imagen = pygame.transform.scale(fondo_imagen, PANTALLA)
    pantalla.blit(fondo_imagen, (0, 0))
    
    volumen_imagen_opciones = pygame.image.load("imagenes/CartelVolumen.png")  
    volumen_imagen_opciones = pygame.transform.scale(volumen_imagen_opciones, (400, 100))  
    opciones_rect = volumen_imagen_opciones.get_rect(center=(PANTALLA[0] // 2, 190))  
    pantalla.blit(volumen_imagen_opciones, opciones_rect)

    boton_resta["rectangulo"] = pantalla.blit(boton_resta['superficie'], (PANTALLA[0] // 2 - 300 - boton_resta['superficie'].get_width() // 2, 320))
    boton_suma["rectangulo"] = pantalla.blit(boton_suma['superficie'], (PANTALLA[0] // 2 + 300 - boton_suma['superficie'].get_width() // 2, 320))

    volumen_imagen = pygame.image.load("imagenes/Volumen.png")
    volumen_imagen = pygame.transform.scale(volumen_imagen, (300, 100)) 
    volumen_rect = volumen_imagen.get_rect(center=(PANTALLA[0] // 2, 400)) 
    pantalla.blit(volumen_imagen, volumen_rect)

    volumen_texto = fuente_volumen.render(f"{datos_juego['volumen_musica']}%", True, BLANCO)
    volumen_texto_rect = volumen_texto.get_rect(center=volumen_rect.center)  
    pantalla.blit(volumen_texto, volumen_texto_rect)

    boton_musica["rectangulo"] = pantalla.blit(boton_musica["superficie"], (PANTALLA[0] // 2 - boton_musica["superficie"].get_width() // 2, 500))
    boton_volver["rectangulo"] = pantalla.blit(boton_volver['superficie'],(15,15))

    return retorno, bandera_musica