
def punto_en_rectangulo(punto, rect):
  x, y = punto
  return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom

def distancia_entre_puntos(pto_1: tuple[int, int], pto_2: tuple[int, int])->float:
  ca = pto_1[0] - pto_2[0]
  co = pto_1[1] - pto_2[1]
  distancia = (ca ** 2 + co ** 2) ** 0.5
  return distancia

def colision_circulos(rec_1, rec_2)-> bool:
  r1 = rec_1.width // 2
  r2 = rec_2.width // 2
  distancia = distancia_entre_puntos(rec_1.center, rec_2.center)
  return distancia <= r1 + r2