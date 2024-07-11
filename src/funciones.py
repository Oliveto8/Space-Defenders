import pygame
from pygame import display, time, draw, event
from colisiones import punto_en_rectangulo
from bloques import *
from pygame.locals import *
from settings import *
import csv

def salir_juego():
  pygame.quit()
  exit()
  
def mostrar_texto(superficie: pygame.Surface, texto: str, fuente: pygame.font.Font, posicion: tuple[int, int],
color: tuple[int, int, int], color_fondo: tuple[int,int,int] = None):
  sup_texto = fuente.render(texto, True, color, color_fondo)
  rect_texto = sup_texto.get_rect(center = posicion)
  superficie.blit(sup_texto, rect_texto)

def wait_user(tecla:int):
  continuar = True
  while continuar:
    for e in event.get():
      if e.type == QUIT:
        salir_juego()
      if e.type == KEYDOWN:
        if e.key == tecla:
          continuar = False

def wait_user_back(tecla: int) -> bool:
  for event in pygame.event.get():
    if event.type == QUIT:
      salir_juego()
    if event.type == KEYDOWN:
      if event.key == tecla:
        return True
  return False

def wait_user_click(button_rect: pygame.Rect):
  continuar = True
  while continuar:
    for e in event.get():
      if e.type == QUIT:
        salir_juego()
      if e.type == MOUSEBUTTONDOWN:
        if e.button == 1:
          if punto_en_rectangulo(e.pos, button_rect):
            continuar = False





