import pygame
from pantalla_como_jugar import *
from config import *
import sys

def pantalla_inicio():
    
    pygame.init()

    imagen_fondo_inicio = pygame.image.load(r"./Recursos\fondo_pantalla_inicio.jpg")
    imagen_fondo_inicio = pygame.transform.scale(imagen_fondo_inicio,(resolucion_pantalla["ancho"], resolucion_pantalla["alto"]))

    iniciar_partida = pygame.Rect(resolucion_pantalla["ancho"]/2-100,  resolucion_pantalla["alto"]/3+50, 230, 60)
    como_jugar = pygame.Rect(resolucion_pantalla["ancho"]/2-100,  resolucion_pantalla["alto"]/3+150, 230, 60)
    salir_del_juego = pygame.Rect(resolucion_pantalla["ancho"]/2-100,  resolucion_pantalla["alto"]/3+250, 230, 60)

    fuente_inicio = pygame.font.Font(None, 32)

    pantalla_inicio = True

    while pantalla_inicio:
        

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:

                pantalla_inicio = False
            
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            
                if iniciar_partida.collidepoint(pygame.mouse.get_pos()):

                    return 1
                
                if como_jugar.collidepoint(pygame.mouse.get_pos()):
                    
                        
                    return 2

                if salir_del_juego.collidepoint(pygame.mouse.get_pos()):

                    pygame.quit()
                    sys.exit()

        screen.blit(imagen_fondo_inicio, origen)

        pygame.draw.rect(screen,(65,255,15), iniciar_partida, 0)
        pygame.draw.rect(screen,(15, 15, 255), como_jugar, 0)
        pygame.draw.rect(screen,(255,30,15), salir_del_juego, 0)
        
        mensaje_inicio = fuente_inicio.render("INICIAR PARTIDA", True, (255,255,255))
        mensaje_como_jugar = fuente_inicio.render("COMO JUGAR", True, (255,255,255))
        mensaje_salir = fuente_inicio.render("SALIR DEL JUEGO", True, (255,255,255))

        screen.blit(mensaje_inicio, (iniciar_partida.x+(iniciar_partida.width - mensaje_inicio.get_width())/2,iniciar_partida.y+(iniciar_partida.height - mensaje_inicio.get_height())/2))
        screen.blit(mensaje_como_jugar, (como_jugar.x+(como_jugar.width - mensaje_como_jugar.get_width())/2,como_jugar.y +(como_jugar.height - mensaje_como_jugar.get_height())/2))
        screen.blit(mensaje_salir, (salir_del_juego.x+(salir_del_juego.width - mensaje_salir.get_width())/2,salir_del_juego.y+(salir_del_juego.height - mensaje_salir.get_height())/2))




        pygame.display.flip()
