import pygame
import sys
from archivo import obtener_puntajes
from config import *
from juego import *
from archivo import *


def pantalla_fin(puntos, rondas):
        
    pygame.init()
    


    imagen_fondo_fin = pygame.image.load(r"./Recursos\fondo_pantalla_fin1.jpg")
    imagen_fondo_fin = pygame.transform.scale(imagen_fondo_fin,(resolucion_pantalla["ancho"], resolucion_pantalla["alto"]))
    
    

    reiniciar_partida = pygame.Rect(resolucion_pantalla["ancho"]/2-100,  resolucion_pantalla["alto"]/3+250, 230, 60)
    salir_del_juego = pygame.Rect(resolucion_pantalla["ancho"]/2-100,  resolucion_pantalla["alto"]/3+350, 230, 60)
    
    fuente_inicio = pygame.font.Font(None, 32)

    
    audio_game_over = pygame.mixer.Sound("./sonidos\game_over.mp3")

    pantalla_de_fin = True
    
    audio_game_over.play()

    while pantalla_de_fin:
                
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:

                pantalla_de_fin = False
                
                
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            
                if reiniciar_partida.collidepoint(pygame.mouse.get_pos()):

                    return 1

                if salir_del_juego.collidepoint(pygame.mouse.get_pos()):
                    
                    
                    aux_puntaje = str(obtener_puntajes("puntajes.csv"))
    
                    lista_puntajes = formatear_puntajes(aux_puntaje)
                    
                    obtener_mejores_puntajes(lista_puntajes)
                    
                    agregar_puntaje(lista_puntajes, puntos, "puntajes.csv")
                    
                    

                    pygame.quit()
                    sys.exit()
                    

        screen.blit(imagen_fondo_fin, origen)

        pygame.draw.rect(screen,(65,255,15), reiniciar_partida, 0)
        pygame.draw.rect(screen,(255,30,15), salir_del_juego, 0)
        
        texto_puntaje = fuente_inicio.render(f"Tu puntaje final fue: {puntos}, sobreviviste {rondas} rondas", True, (255,255,255))
        
        mensaje_reinicio = fuente_inicio.render("REINICIAR PARTIDA", True, (255,255,255))
        mensaje_salir = fuente_inicio.render("SALIR DEL JUEGO", True, (255,255,255))

        screen.blit(mensaje_reinicio, (reiniciar_partida.x+(reiniciar_partida.width - mensaje_reinicio.get_width())/2,reiniciar_partida.y+(reiniciar_partida.height - mensaje_reinicio.get_height())/2))
        screen.blit(mensaje_salir, (salir_del_juego.x+(salir_del_juego.width - mensaje_salir.get_width())/2,salir_del_juego.y+(salir_del_juego.height - mensaje_salir.get_height())/2))
        screen.blit(texto_puntaje, (resolucion_pantalla["alto"]/2-50, resolucion_pantalla["ancho"]/8))
    

        pygame.display.flip()
    
