import pygame
from config import *
from pantalla_inicio import *
from juego import *
from pantalla_como_jugar import *
from pantalla_fin import *

pygame.init()

jugando = 0

while True:
    
    if jugando == 0:
        
        jugando = pantalla_inicio()
        
    if jugando == 1:
        
        jugando = pantalla_principal()

        jugando = pantalla_fin()
        
    if jugando == 2:
        
        jugando = funcion_como_jugar()
