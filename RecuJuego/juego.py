import pygame
from pygame.locals import *
from config import *
import random
from pantalla_fin import *
from pantalla_fin import pantalla_fin
from pantalla_pausa import funcion_pausa
from pantalla_inicio import pantalla_inicio


#INIT
def pantalla_principal():
        
    #FPS
    clock = pygame.time.Clock()


    #IMAGEN FONDO

    imagen_fondo = pygame.image.load(r"./Recursos\background.jpg")
    imagen_fondo = pygame.transform.scale(imagen_fondo,(resolucion_pantalla["ancho"], resolucion_pantalla["alto"]))

    #SOLDADO
    soldado = pygame.image.load(r"./Recursos\soldado.png")
    soldado = pygame.transform.scale(soldado, (90, 110))

    soldado_rect = soldado.get_rect()



    soldado_rect.bottomleft = (resolucion_pantalla["ancho"]//2, resolucion_pantalla["alto"])

    velocidad = 5
    altura_salto = 10
    puntos = 0
    vidas = 3

    #DISPARO / BALA

    ultimo_disparo = 0
    velocidad_bala = 10
    cooldown_disparo = 300
    lista_balas = []


    #ZOMBIES

    inmune = False
    corazones = []

    zombies_spawneados = False
    ronda = 1

    cooldown_zombies = 100
    ultimo_zombie = 0

    cantidad_base = 5
    cantidad_ronda = ronda
    cantidad_total = cantidad_base + cantidad_ronda

    velocidad_zombie = 2

    zombies = []

    flecha_arriba = False
    flecha_derecha = False
    flecha_izquierda = False
    
    #SONIDOS DEL JUEGO

    audio_disparo = pygame.mixer.Sound('./sonidos\disparo.mp3')
    audio_pierde_vida = pygame.mixer.Sound("./sonidos\soldado_pierde_vida.mp3")
    audio_zombie_muere = pygame.mixer.Sound("./sonidos\zombie_muere.mp3")


    sonidos = True
    
    fuente_en_juego = pygame.font.SysFont("dejavuserif", 40)
    
    seguir = True
    
    mirando_izquierda = False
    mirando_derecha = True
    
    #ENTRE PANTALLAS DEL JUEGO
    

    def mover_zombies(lista, velocidad_zombie):
        for enemigos in lista:
            if(enemigos[0]):
                enemigos[1].x -= velocidad_zombie 
            else:
                enemigos[1].x += velocidad_zombie


    def limpiar_zombies(enemigos):
        lista_nueva = []
        for enemigo in enemigos:
            if(enemigo[0] != 3):
                lista_nueva.append(enemigo)
            
            
        return lista_nueva


    def crear_zombie(cantidad_total):

        zombies = []
        
        distinto_lugar_izquierda = - 50
        distinto_lugar_derecha = + 50


        for _ in range(cantidad_total): 
            donde_sale = int(random.random() * 1.99)
            if donde_sale:
                zombie = pygame.transform.scale(pygame.image.load(r"./Recursos/zombie.png"), (65, 85))
                rect_zombie = zombie.get_rect()
                rect_zombie.bottomleft = (resolucion_pantalla["ancho"] + distinto_lugar_derecha, resolucion_pantalla["alto"])
                zombies.append([1, rect_zombie, zombie])
            else:
                zombie = pygame.transform.scale(pygame.transform.flip(pygame.image.load(r"./Recursos/zombie.png"), True, False), (65, 85))
                rect_zombie = zombie.get_rect()
                rect_zombie.bottomleft = (distinto_lugar_izquierda, resolucion_pantalla["alto"])
                zombies.append([0, rect_zombie, zombie])
                
            distinto_lugar_izquierda -= 50
            distinto_lugar_derecha += 50

        return zombies

    #MOVIMIENTO SOLDADO

    def movimiento_soldado(izquierda, derecha, rect, soldado, mirando_izquierda, mirando_derecha):
        
        # Se usa un único return

        if (izquierda and not derecha):
            
            rect.x -= velocidad

            if mirando_derecha:
                soldado =  pygame.transform.flip(soldado, True, False)
                mirando_izquierda = True
                mirando_derecha = False
        
        if(derecha and not izquierda):
            
            rect.x += velocidad

            if mirando_izquierda:
                soldado =  pygame.transform.flip(soldado, True, False)
                mirando_izquierda = False
                mirando_derecha = True


        return (soldado, mirando_izquierda, mirando_derecha)


    #GRAVEDAD_SOLDADO
    def gravedad_soldado(rect):
        if(rect.bottom > resolucion_pantalla["alto"]):
            rect.bottom = resolucion_pantalla["alto"]


    #PAREDES LIMITES DEL SOLDADO
    def limites_soldado(rect:pygame.rect.Rect):
        if(rect.bottomleft[0] <= 0):
            return (1,0)
        if(rect.bottomright[0] >= resolucion_pantalla["ancho"]):
            return(0,1)
        else:
            return (0,0)

    limite = [0,0]
    
    limite = limites_soldado(soldado_rect)

    #CREAR DISPARO

    def nuevo_disparo(rect, izquierda, derecha):
        
        if ((not izquierda and not derecha) or (izquierda and derecha) or (not izquierda and derecha)):
            disparo = pygame.image.load(r"./Recursos\bala_soldado.png")
            rect_disparo = disparo.get_rect()
            rect_disparo.center = rect.center
            return[1, rect_disparo, disparo]
        elif(izquierda and not derecha):
            disparo = pygame.transform.flip(pygame.image.load(r"./Recursos\bala_soldado.png"), True, False)
            rect_disparo = disparo.get_rect()
            rect_disparo.center = rect.center
            return[0, rect_disparo, disparo]

    #VELOCIDAD BALA

    def movimiento_bala(lista_balas):
        
        for bala in lista_balas:
            
            if bala[0] == 1:
                bala[1].x += velocidad_bala
            elif bala[0] == 0:
                bala[1].x -= velocidad_bala

    #BORRA DISPAROS DE LA LISTA

    def limpiar_disparos(lista_disparos):
        lista_nueva = []
        for disparo in lista_disparos:
            if(disparo[1].x > 0 and disparo[1].x < resolucion_pantalla["ancho"] and disparo[0] != 3):
                lista_nueva.append(disparo)
        return lista_nueva


    #CAMBIAR MIRADA DEL SOLDADO

    def cambiar_imagen_solado(rect, imagen):
        posicion = rect.bottomleft
        rect = imagen.get_rect()
        rect.bottomleft = posicion


    #COLISIONES ZOMBIES CON BALAS

    def colision_bala_zombie(balas, zombies, puntos):
        
        for bala in balas:
            for zombie in zombies:
                if(bala[1].colliderect(zombie[1])):
                    
                    bala[0] = 3
                    zombie[0] = 3
                    puntos += 10
                    audio_zombie_muere.play()
        for zombie in zombies:            
            if(zombie[0] and zombie[1].bottomleft[0] < 0 ):
                
                zombie[0] = 3
                
            if(not zombie[0] and zombie[1].bottomleft[0] > resolucion_pantalla["ancho"]):
                
                zombie[0] = 3

        return puntos
                
    #COLISIONES ZOMBIES CON SOLDADO

    def colision_zombie(rectangulo_soldado: pygame.rect.Rect, zombies, vidas):
        
        for zombie in zombies:
            if(rectangulo_soldado.colliderect(zombie[1])):
                
                vidas -= 1
                audio_pierde_vida.play()
        
        return vidas


    #NO MAS DE 1 COLISION AL ZOMBIE


    def prueba_inmune(rectangulo_soldado:pygame.rect.Rect, zombies):
        
        for zombie in zombies:
            if(rectangulo_soldado.colliderect(zombie[1])):
                
                return True
        
        return False

    #VIDAS

    def prueba_vidas(vidas, corazones, puntos, rondas):
        
        
        
        lista_nueva = []
        for corazon in corazones:
            if(corazon[2] < vidas):
                lista_nueva.append(corazon)

        if(vidas <= 0):
            
            pantalla_fin(puntos, rondas)
        
        return lista_nueva


    #CREACION LISTA DE CORAZONES

    for x in range(vidas):
        imagen_corazones = pygame.transform.scale(pygame.image.load(r"./Recursos\corazon.png"), (50, 50))
        rect_corazones = imagen_corazones.get_rect()
        corazones.append([imagen_corazones, rect_corazones, x])
        
    corazones[0][1].topright = (resolucion_pantalla["ancho"]-150, 50)
    corazones[1][1].topright = (resolucion_pantalla["ancho"]-90, 50)
    corazones[2][1].topright = (resolucion_pantalla["ancho"]-30, 50)





    while seguir:

        clock.tick(60)
        
        tiempo_en_juego = pygame.time.get_ticks()
        
        cambiar_imagen_solado(soldado_rect, soldado)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                
                seguir = False
            if evento.type == KEYDOWN:
                
                if evento.key == K_UP:
                    flecha_arriba = True
                if evento.key == K_LEFT:
                    flecha_izquierda = True
                if evento.key == K_RIGHT:
                    flecha_derecha = True
                if ((evento.key == K_SPACE) and (tiempo_en_juego - ultimo_disparo) >= cooldown_disparo):
                    lista_balas.append(nuevo_disparo(soldado_rect, flecha_izquierda, flecha_derecha))
                    ultimo_disparo = tiempo_en_juego
                    audio_disparo.play()
                if(evento.key == K_ESCAPE):
                    funcion_pausa()
            
            if evento.type == KEYUP:
                if evento.key == K_LEFT:
                    flecha_izquierda = False
                if evento.key == K_RIGHT:
                    flecha_derecha = False
                    
        limite = limites_soldado(soldado_rect)
        
        if limite[0]:
            flecha_izquierda = False
        if limite[1]:
            flecha_derecha = False
        
        if (flecha_arriba and altura_salto >= -10): 
            soldado_rect.y -= (altura_salto * abs(altura_salto)) * 0.45
            altura_salto -= 1
        else:
            altura_salto = 10
            flecha_arriba = False


        if not zombies_spawneados:
            zombies_spawneados = True
            zombies += crear_zombie(ronda)

        else:
            zombies = limpiar_zombies(zombies)


        if len(zombies) == 0 and (tiempo_en_juego - ultimo_zombie) > cooldown_zombies:
            zombies_spawneados = False
            ronda += 1
            
            if ronda >= 5 and ronda <= 10:
                
                velocidad_zombie += 0.2
            
            elif ronda > 10:
                
                velocidad_zombie += 0.4

        gravedad_soldado(soldado_rect)
        
        soldado, mirando_izquierda, mirando_derecha = movimiento_soldado(flecha_izquierda, flecha_derecha, soldado_rect, soldado, mirando_izquierda, mirando_derecha)
        
        
        movimiento_bala(lista_balas)
        
        lista_balas = limpiar_disparos(lista_balas)
        
        

        mover_zombies(zombies, velocidad_zombie)

        puntos = colision_bala_zombie(lista_balas, zombies, puntos)
        
        
        
        if not inmune:
            
            vidas = colision_zombie(soldado_rect, zombies, vidas)

        inmune = prueba_inmune(soldado_rect, zombies)

        corazones = prueba_vidas(vidas, corazones, puntos, ronda) 
        
        
                
        screen.blit(imagen_fondo, origen)
        
        screen.blit(soldado, soldado_rect)
        
        
        
        for bala in lista_balas:
            screen.blit(bala[2], bala[1])
        
        for zombie in zombies:
            screen.blit(zombie[2], zombie[1])

        for corazon in corazones:
            screen.blit(corazon[0], corazon[1])
            
            
        
        texto_puntos = fuente_en_juego.render(f"Puntaje: {puntos}", True, "red")
        screen.blit(texto_puntos, (0,0))
        
        zombies_restantes = len(zombies)
        texto_zombies_restantes = fuente_en_juego.render(f"Zombies restantes: {zombies_restantes}", True, "red")
        screen.blit(texto_zombies_restantes, (0, 35))
        
        texto_ronda = fuente_en_juego.render(f"Ronda: {ronda}", True, "red")
        screen.blit(texto_ronda, (0, 70))
        

        
        pygame.display.flip()



