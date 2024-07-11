# SPACE DEFENDERS

### ¡Eres el piloto de la nave Apolo, y estás en una misión crítica! La nave se está quedando sin oxígeno, y solo dispones de 60 segundos para destruir la mayor cantidad de enemigos posible antes de que lleguen a la base espacial.

## Instalación
Sigue estos pasos para configurar y ejecutar el juego en tu máquina local.

### Clonar Repositorio
Primero, clona este repositorio en tu máquina local:

git clone https://github.com/Oliveto8/Space-Defenders.git

### Crear Entorno Virtual

python -m venv env

### Activar Entorno Virtual
Activa el entorno virtual. Los comandos pueden variar según tu sistema operativo:

En Windows (PowerShell):

  - .\env\Scripts\Activate.ps1

En macOS y Linux:

 - source env/bin/activate

### Instalar Dependencias

Instala las dependencias necesarias para el juego desde el archivo requirements.txt:

pip install -r requirements.txt

### Ejecutar el Juego

Para ejecutar el juego, asegúrate de estar en el directorio raíz del proyecto y tener el entorno virtual activado. Luego, ejecuta el siguiente comando:

python main.py
Asegúrate de tener pygame y todas las dependencias instaladas correctamente.

### Controles del Juego

Flechas: Mover la nave espacial.

F: Disparar láser.

M: Alternar música de fondo.

ESC: Pausar/Reanudar juego.
