import pygame
from settings import *
from pygame import display, time, event
from pygame.locals import *
from funciones import *
from game import game_loop
from ranking import *

# Inicializar los módulos de pygame
pygame.init()

clock = time.Clock()
intro.play(-1)
# Configuración de la pantalla principal
screen = display.set_mode(SCREEN_SIZE)
display.set_caption("Space Defenders")

def main_loop():
  while True:
    # Pantalla de inicio
    
    screen.blit(home_background, ORIGIN)  # fondo
    screen.blit(space_defenders, rec_space_defenders_button)  # nombre juego
    screen.blit(start_button, rec_start_button)  # boton play
    screen.blit(score_button, rec_score_button)  # boton score
    screen.blit(close_button, rec_close_button)  # boton close
    pygame.display.flip()

    # Manejo de eventos
    for e in event.get():
      if e.type == QUIT:
        salir_juego()
      elif e.type == MOUSEBUTTONDOWN:
        if e.button == 1:  # Botón izquierdo del mouse
          if rec_start_button.collidepoint(e.pos):
            boton.play()
            intro.stop()
            game_loop(screen)
          elif rec_score_button.collidepoint(e.pos):
            boton.play()
            mostrar_puntajes(screen,"retrocerder")
          elif rec_close_button.collidepoint(e.pos):
            boton.play()
            salir_juego()

    # Esperar a que el jugador presione Espacio para volver al menú principal
    if wait_user_back(K_SPACE):
      return  # Salir del bucle principal y volver al menú principal

    pygame.display.flip()

if __name__ == "__main__":
  main_loop()