import pygame
from config import *
import sys


def funcion_como_jugar(): 

    pygame.init()



    imagen_fondo_inicio = pygame.image.load(r"./Recursos\fondo_como_jugar.jpg")
    imagen_fondo_inicio = pygame.transform.scale(imagen_fondo_inicio,(resolucion_pantalla["ancho"], resolucion_pantalla["alto"]))

    volver_al_menu = pygame.Rect(resolucion_pantalla["ancho"]/2-100,  resolucion_pantalla["alto"]/3+250, 230, 60)

    fuente_inicio = pygame.font.Font(None, 32)

    pantalla_como_jugar = True

    while pantalla_como_jugar:
        

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                
                pantalla_como_jugar = False
            
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:

                if volver_al_menu.collidepoint(pygame.mouse.get_pos()):

                    return 0

        screen.blit(imagen_fondo_inicio, origen)

        pygame.draw.rect(screen,(255,30,15), volver_al_menu, 0)
        

        mensaje_volver_al_menu = fuente_inicio.render("VOLVER AL MENU", True, (255,255,255))

        screen.blit(mensaje_volver_al_menu, (volver_al_menu.x+(volver_al_menu.width - mensaje_volver_al_menu.get_width())/2,volver_al_menu.y+(volver_al_menu.height - mensaje_volver_al_menu.get_height())/2))


            


        pygame.display.flip()

