import pygame
import csv
from ranking import *
from pygame.locals import *
from funciones import *
from settings import *

def game_over_screen(screen, score):
  global game_over
  pygame.mixer_music.stop()
  game_over.play()
  intro.play(-1)
  
  # Mostrar la pantalla de Game Over
  screen.blit(background, ORIGIN)
  screen.blit(game_over_image, rec_game_over_button) 
  mostrar_texto(screen, "Pulsa espacio para ver el ranking", fuente, CONTINUE_POS, RED)
  pygame.display.flip()
  wait_user(K_SPACE) 
  
  update_scores("scores.csv", score)
  mostrar_puntajes(screen,"finalizar el juego")
  salir_juego()  # Esperar nuevamente a que el usuario pulse espacio para salir