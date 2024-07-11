import pygame
from pygame.locals import *
pygame.init()

GAMETIMEOUT = USEREVENT + 2
ORIGIN = (0,0) #origen x y
FPS = 60
WIDTH = 1280 #ancho
HEIGHT = 720 #alto
MID_WIDTH_SCREEN = (WIDTH//2) #ancho medio
MID_HEIGHT_SCREEN = (HEIGHT//2) #alto medio

SCORE_POS = (MID_WIDTH_SCREEN,55) #posicion del score
LIFE_POS = (150,55) #posicion de las vidas
MUTE_POS = (MID_WIDTH_SCREEN,250) #posicion juego muteado
PAUSE_POS = (MID_WIDTH_SCREEN,150) #posicion juego pausado
CONTINUE_POS = (MID_WIDTH_SCREEN,500) #posicion continuar juego
FIN_POS = (MID_WIDTH_SCREEN,650) #posicion continuar juego

INITIAL_QUANTITY_ASTEROIDES = 3
score = 0
vida = 5

player_width = 70
player_height = 70
laser_width = 30
laser_height = 15

speed_x = 5
speed_y = 6

SCREEN_SIZE = (WIDTH,HEIGHT)
SCREEN_CENTER = (MID_WIDTH_SCREEN,MID_HEIGHT_SCREEN)


START_BUTTOM_SIZE = (200, 80)
START_BUTTOM_POS = (MID_WIDTH_SCREEN, MID_HEIGHT_SCREEN + 20)
SCORE_BUTTOM_POS = (MID_WIDTH_SCREEN, MID_HEIGHT_SCREEN + 100)
CLOSE_BUTTOM_POS = (MID_WIDTH_SCREEN, MID_HEIGHT_SCREEN + 180)

BARRA_AZUL = (400, 70)
BARRA_AZUL2 = (520, 70)
BARRA_AZUL3 = (400, 70)
BARRA_AZUL_POS = (-70,20)
BARRA_AZUL2_POS = (380,20)
BARRA_AZUL3_POS = (940,20)

SPACE_DEFENDERS = (500,250)
SPACE_DEFENDERS_POS = (MID_WIDTH_SCREEN , MID_HEIGHT_SCREEN - 180)
GAME_OVER_POS = (MID_WIDTH_SCREEN - 150, MID_HEIGHT_SCREEN - 180)
RANKING_POS = (MID_WIDTH_SCREEN - 150, MID_HEIGHT_SCREEN - 250)

HEARTH1 = (50, 50) 
HEARTH1_POS = (980, 30)
HEARTH2_POS = (1040, 30)
HEARTH3_POS = (1100, 30)
HEARTH4_POS = (1160, 30)
HEARTH5_POS = (1220, 30)

#colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
YELLOW = (255,255,0)
BLACK = (0,0,0)
WHITE = (226,226,226)
CUSTOM = (226, 203,100)

#cargo fuente
try:
  fuente = pygame.font.SysFont('Arial', 50)
except pygame.error as e:
  print("Error al cargar la fuente:", e)

#cargo sonidos
intro = pygame.mixer.Sound("./src/assets/sounds/intro.mp3")
intro.set_volume(0.2)
boton = pygame.mixer.Sound("./src/assets/sounds/button.mp3")
perder_vida = pygame.mixer.Sound("./src/assets/sounds/perder_vida.mp3")
sumar_vida = pygame.mixer.Sound("./src/assets/sounds/sumar_vida.mp3")
sumar_score = pygame.mixer.Sound("./src/assets/sounds/sumar_score.mp3")
game_over = pygame.mixer.Sound("./src/assets/sounds/game_over.mp3")
explosion_sound = pygame.mixer.Sound("./src/assets/sounds/coin.mp3")
explosion_sound.set_volume(0.1)

#musica de fondo
try:
  musica_game = pygame.mixer.music.load("./src/assets/sounds/musica_fondo.mp3")
  pygame.mixer.music.set_volume(0.2)
except Exception as e:
  print(f"Error inesperado: {e}")
  # Detener la música si se está reproduciendo
  if pygame.mixer.music.get_busy():
    pygame.mixer.music.stop()

# direcciones
move_left = False
move_right = False
move_up = False
move_down = False
laser = None
estrella = None

#IMAGENES#
nave_jugador = pygame.image.load("./src/assets/personajes/1.png")
bala = pygame.image.load("./src/assets/personajes/7.png")
imagen_ovni = pygame.image.load("./src/assets/personajes/0.png")
background = pygame.transform.scale(pygame.image.load("./src/assets/fondo1.jpeg"), SCREEN_SIZE)

home_background = pygame.transform.scale(pygame.image.load("./src/assets/home/home_fondo.png"), SCREEN_SIZE)

space_defenders = pygame.transform.scale(pygame.image.load("./src/assets/home/space_defenders.png"), SPACE_DEFENDERS)
rec_space_defenders_button = space_defenders.get_rect(center = SPACE_DEFENDERS_POS )
start_button = pygame.transform.scale(pygame.image.load("./src/assets/home/star_buttom.png"), START_BUTTOM_SIZE)
rec_start_button = start_button.get_rect(center = START_BUTTOM_POS)
score_button = pygame.transform.scale(pygame.image.load("./src/assets/home/score_buttom.png"), START_BUTTOM_SIZE)
rec_score_button = score_button.get_rect(center = SCORE_BUTTOM_POS)
close_button = pygame.transform.scale(pygame.image.load("./src/assets/home/close_buttom.png"), START_BUTTOM_SIZE)
rec_close_button = close_button.get_rect(center = CLOSE_BUTTOM_POS)

game_over_image = pygame.transform.scale(pygame.image.load("./src/assets/home/game_over.png"), SPACE_DEFENDERS)
rec_game_over_button = start_button.get_rect(center = GAME_OVER_POS)
ranking_image = pygame.transform.scale(pygame.image.load("./src/assets/home/ranking_players.png"), SPACE_DEFENDERS)
rec_ranking_button = start_button.get_rect(center = RANKING_POS)


####################################VIDA#################################################
hearth_1 = pygame.transform.scale(pygame.image.load("./src/assets/corazon.png"), HEARTH1)
hearth_2 = pygame.transform.scale(pygame.image.load("./src/assets/corazon.png"), HEARTH1)
hearth_3 = pygame.transform.scale(pygame.image.load("./src/assets/corazon.png"), HEARTH1)
hearth_4 = pygame.transform.scale(pygame.image.load("./src/assets/corazon.png"), HEARTH1)
hearth_5 = pygame.transform.scale(pygame.image.load("./src/assets/corazon.png"), HEARTH1)
hearth_black_1 = pygame.transform.scale(pygame.image.load("./src/assets/corazon_negro.png"), HEARTH1)
hearth_black_2 = pygame.transform.scale(pygame.image.load("./src/assets/corazon_negro.png"), HEARTH1)
hearth_black_3 = pygame.transform.scale(pygame.image.load("./src/assets/corazon_negro.png"), HEARTH1)
hearth_black_4 = pygame.transform.scale(pygame.image.load("./src/assets/corazon_negro.png"), HEARTH1)
hearth_black_5 = pygame.transform.scale(pygame.image.load("./src/assets/corazon_negro.png"), HEARTH1)
#########################################################################################

barra_azul = pygame.transform.scale(pygame.image.load("./src/assets/barra.png"), BARRA_AZUL)
barra_azul2 = pygame.transform.scale(pygame.image.load("./src/assets/barra.png"), BARRA_AZUL2)
barra_azul3 = pygame.transform.scale(pygame.image.load("./src/assets/barra.png"), BARRA_AZUL3)

