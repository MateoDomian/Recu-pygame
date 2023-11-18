import pygame


#RESOLUCION PANTALLA
resolucion_pantalla = {"ancho": 1100, "alto": 700}

#SCREEN
screen = pygame.display.set_mode((resolucion_pantalla["ancho"], resolucion_pantalla["alto"]))

#TITULO
pygame.display.set_caption("Zombie Survive")

icono = pygame.image.load(r"./Recursos\icono_zombie.png")   

pygame.display.set_icon(icono)

#ORIGEN 0, 0

origen = (0, 0)