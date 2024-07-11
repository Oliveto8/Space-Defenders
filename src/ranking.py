import pygame
from pygame.locals import *
import sys
import csv
from settings import *
from funciones import mostrar_texto,wait_user_back

def read_csv(filename:str):
  try:
    # Leer los puntajes desde el archivo CSV
    with open(filename, 'r', newline='') as file:
      reader = csv.reader(file)
      scores = [line for line in reader if len(line) >= 2]  # Filtrar líneas con al menos 2 elementos
  except FileNotFoundError:
    scores = []
  return scores

def update_scores(filename, score:int):
  scores = read_csv(filename)
  # Agregar el puntaje actual a la lista de scores
  scores.append(['Jugador', str(score)])
  # Guardar todos los puntajes en el archivo CSV
  with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(scores)  
  # Ordenar los puntajes por puntaje (segundo elemento en cada lista)
  scores.sort(key=lambda x: int(x[1]), reverse=True)
  return scores

def read_scores(filename):
  scores = read_csv(filename)
  # Ordena los puntajes por puntaje (segundo elemento en cada lista)
  scores.sort(key=lambda x: int(x[1]), reverse=True)
  return scores

def mostrar_puntajes(screen, mensaje:str):
  while True:
    # Mostrar los puntajes
    scores = read_scores("scores.csv")
    screen.blit(background, ORIGIN)
    screen.blit(ranking_image, rec_ranking_button)
    y_offset = 350
    mostrar_texto(screen, f"Pulsa espacio para {mensaje}", fuente, FIN_POS, RED)
    for i, score in enumerate(scores[:3]):
      score_text = fuente.render(f'{i+1}. {score[0]}: {score[1]}', True, WHITE)
      screen.blit(score_text, (MID_WIDTH_SCREEN - 150, y_offset))
      y_offset += 60
    pygame.display.flip()
    if wait_user_back(K_SPACE):
      return  # Salir de la función y volver al bucle principal