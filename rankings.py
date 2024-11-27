import pygame
from constantess import *
from Funcioones import mostrar_texto

pygame.init()

boton_volver_imagen = pygame.image.load("imagenes/Botón volver.png")

boton_volver = {}
boton_volver["superficie"] = pygame.transform.scale(boton_volver_imagen, TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()


fuente = pygame.font.SysFont("Arial Narrow",32)
fuente_boton = pygame.font.SysFont("Arial Narrow",23)


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
    boton_volver["rectangulo"] = pantalla.blit(boton_volver['superficie'],(15,15))
    mostrar_texto(pantalla,f"ACA SE DEBE MOSTRAR EL TOP 10",(20,200),fuente,BLANCO)
    
    return retorno