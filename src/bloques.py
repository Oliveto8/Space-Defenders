import pygame
from random import randint
from settings import *
import random

def crear_bloque(imagen = None, left=0, top=0, ancho=40, alto=40, dir=3, borde=0, radio=-1, speed_x=10, speed_y=10)->dict:
  rec = pygame.Rect(left, top, ancho, alto)
  if imagen:
    imagen = pygame.transform.scale(imagen,(ancho, alto))
  return {"rect": rec, "dir": dir, "borde": borde, "radio": radio, "speed_x": speed_x, "speed_y": speed_y, "img": imagen}

def crear_laser(posicion: tuple[int, int], imagen = None,speed:int=20):
  rectangulo = pygame.Rect(0, 0, laser_width, laser_height)
  rectangulo.midbottom = posicion
  if imagen:
    imagen = pygame.transform.scale(imagen,(laser_width, laser_height))
  return {"rect": rectangulo, "img": imagen, "speed": speed}

def crear_enemigo(imagen=None, enemigo_width = 50, enemigo_height = 50 ) -> dict: 
  initial_x = randint(WIDTH, WIDTH + 300)
  initial_y = randint(100, HEIGHT - enemigo_height)  
  speed_x = -randint(5, 7)  
  return crear_bloque(imagen, initial_x, initial_y, enemigo_width, enemigo_height, speed_x=-speed_x, radio=enemigo_height // 2)

def load_enemigo_list(lista:list, cantidad:int, imagen = None, enemigo_width = 50, enemigo_height = 50):
  for _ in range(cantidad):
    lista.append(crear_enemigo(imagen, enemigo_width, enemigo_height))

def crear_estrella(imagen=None, estrella_width=30, estrella_height=30) -> dict: 
  initial_x = WIDTH
  initial_y = randint(100, HEIGHT - estrella_height)  
  speed_x = -3  
  return crear_bloque(imagen, initial_x, initial_y, estrella_width, estrella_height, speed_x=-speed_x, radio=estrella_height // 2)

player = crear_bloque(nave_jugador, 100, 360, player_width, player_height,  radio= player_height//2)

ovnis = []
load_enemigo_list(ovnis, INITIAL_QUANTITY_ASTEROIDES, imagen_ovni, 80,80)

