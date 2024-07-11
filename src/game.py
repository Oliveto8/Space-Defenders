import pygame
from pygame.locals import *
from pygame import display, time, draw, event
from colisiones import colision_circulos
from game_over import game_over_screen
import sys
from bloques import *
from funciones import *
from settings import *


def game_loop(screen):
  global vida,score,move_down,move_left,move_right,move_up,laser,estrella
  # Variables para el cronómetro
  tiempo_inicial = pygame.time.get_ticks()
  duracion_cronometro = 60  # 60 segundos
  clock = pygame.time.Clock()
  #eventos personalizados
  TIMEROVNI = USEREVENT + 1
  GAMETIMEOUT = USEREVENT + 2
  pygame.time.set_timer(TIMEROVNI, 15000)
  pygame.time.set_timer(GAMETIMEOUT, 60000)
  #musica
  pygame.mixer.music.play(-1)
  playing_music = True
  is_running = True
  is_paused = False
  while is_running:
    clock.tick(FPS)
    # Calcular tiempo transcurrido
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial
    if not is_paused:
      segundos_restantes = duracion_cronometro - (tiempo_transcurrido // 1000)
    ##DETECTAR EVENTOS##
    for e in event.get():
      #evento usuario cierra ventana de juego (x)
      if e.type == QUIT:
        salir_juego()
      if e.type == KEYDOWN:
        if e.key == K_ESCAPE:  # Pausa
          is_paused = not is_paused
          if is_paused:
              pygame.mixer.music.pause()
          else:
              pygame.mixer.music.unpause()
      #evento se presiono una tecla
        if not is_paused:
          if e.key == K_f:
            if not laser:
              laser = crear_laser(player["rect"].midright, bala)
          if e.key == K_LEFT:
            move_left =True
            move_right = False
          if e.key == K_RIGHT:
            move_right = True
            move_left = False       
          if e.key == K_UP:
            move_up = True
            move_down = False
          if e.key == K_DOWN:
            move_down = True
            move_up = False
          if e.key == K_m:
            if not is_paused:
              if playing_music:
                pygame.mixer.music.pause()
              else:
                pygame.mixer.music.unpause()
              playing_music = not playing_music

      #evento se libero una tecla
      elif e.type == KEYUP:
        if e.key == K_LEFT:
          move_left = False
        if e.key == K_RIGHT:
          move_right = False
        if e.key == K_UP:
          move_up = False
        if e.key == K_DOWN:
          move_down = False

      #evento personalizado
      elif e.type == GAMETIMEOUT:
        is_running = False

      elif e.type == TIMEROVNI:
        estrella = crear_estrella(hearth_1,40,40)

  ##ACTUALIZAR ELEMENTOS##
    if not is_paused:
    # Mover el rectángulo de acuerdo a su dirección
      if move_left and player["rect"].left > 0:
        player["rect"].left -= speed_x  
      if move_right and player["rect"].right < 350:
        player["rect"].left += speed_x    
      if move_up and player["rect"].top > 100:
        player["rect"].top -= speed_y
      if move_down and player["rect"].bottom < HEIGHT:
        player["rect"].top += speed_y

      # Mover el láser si existe
      if laser:
        laser["rect"].move_ip(laser["speed"], 0)
        # Verificar si el láser salió de la pantalla
        if laser["rect"].right > WIDTH:  
          laser = None  # Eliminar el láser 

      # Mover los ovnis
      for ovni in ovnis.copy():
        ovni["rect"].move_ip(-ovni["speed_x"], 0)  # Mover hacia la izquierda
        # Verificar si el ovni salió de la pantalla y quitar una vida
        if ovni["rect"].right < 0:
          perder_vida.play()
          vida -= 1  # Reducir una vida
          ovnis.remove(ovni)
      # Verificar colisiones entre la nave y los ovnis, y entre el láser y los ovnis
        # Colisión entre la nave y los asteroides
        if colision_circulos(player["rect"], ovni["rect"]):
          explosion_sound.play()
          perder_vida.play()
          vida -= 1
          ovnis.remove(ovni)
        # Colisión entre el láser y los ovnis
        if laser and laser["rect"].colliderect(ovni["rect"]):
          ovnis.remove(ovni)
          laser = None
          score += 5  # Sumar 5 puntos al puntaje
          explosion_sound.play()  # Reproducir sonido de moneda obtenida
          break
      if estrella:
        estrella["rect"].move_ip(-estrella["speed_x"], 0)  # Mover la estrella
        if player["rect"].colliderect(estrella["rect"]):
          if vida < 5:
            vida += 1 
            sumar_vida.play()
          else:
            score += 100# Incrementar vida si tiene menos de 5
            sumar_score.play()
          estrella = None  # Eliminar la estrella

      # Si queda 1 ovni en la lista, cargar más
      if len(ovnis) == 1 or len(ovnis) == 0:
        load_enemigo_list(ovnis, INITIAL_QUANTITY_ASTEROIDES, imagen_ovni, 80 ,80)
      # Verificar si el juego debe finalizar por falta de vidas
      if vida == 0:
        is_running = False  # Finalizar juego si se quedan sin vidas
        break

    ## ---> dibujar pantalla
    screen.blit(background, ORIGIN) #fondo
    ###PERSONAJES
    screen.blit(player["img"], player["rect"])

    if laser:
      screen.blit(laser["img"], laser["rect"]) #laser
    for ovni in ovnis:
      if ovni:
        screen.blit(ovni["img"], ovni["rect"])
    if estrella:
        screen.blit(estrella["img"], estrella["rect"])  # Dibuja la estrella

    ###VIDAS
    screen.blit(barra_azul, BARRA_AZUL_POS)
    screen.blit(barra_azul2, BARRA_AZUL2_POS)
    screen.blit(barra_azul3, BARRA_AZUL3_POS)
    if vida > 0:
      screen.blit(hearth_black_1, HEARTH1_POS)
      screen.blit(hearth_black_2, HEARTH2_POS)
      screen.blit(hearth_black_3, HEARTH3_POS)
      screen.blit(hearth_black_4, HEARTH4_POS)
      screen.blit(hearth_black_5, HEARTH5_POS)
      screen.blit(hearth_1, HEARTH1_POS)
    if vida >= 2:
      screen.blit(hearth_2, HEARTH2_POS)
    if vida >= 3:
      screen.blit(hearth_3, HEARTH3_POS)
    if vida >= 4:
      screen.blit(hearth_4, HEARTH4_POS)
    if vida >= 5:
      screen.blit(hearth_5, HEARTH5_POS)

    if not playing_music:
      mostrar_texto(screen, "mute", fuente, MUTE_POS, BLUE)
    if is_paused:
          mostrar_texto(screen, "JUEGO PAUSADO", fuente, PAUSE_POS, RED)
    mostrar_texto(screen, f"SCORE: {score}", fuente, SCORE_POS , BLACK)
    mostrar_texto(screen, f"TIME: {segundos_restantes}", fuente, LIFE_POS , BLACK)

    # ----> Actualizar pantalla
    display.update()
    
  game_over_screen(screen, score)