import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
import numpy as np
import math

# Importamos los módulos para las figuras
from figures.cube import Cube
from figures.pyramid import Pyramid
from figures.sphere import Sphere
from figures.cylinder import Cylinder
from figures.superellipsoid import Superellipsoid
from utils.texture_loader import load_texture

# Inicialización de Pygame y fuente
pygame.init()
pygame.font.init()
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Escena 3D - OpenGL & PyGame")
font = pygame.font.SysFont('Arial', 24)

# Configuración inicial de OpenGL
def init_gl():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glLightfv(GL_LIGHT0, GL_POSITION, [5.0, 5.0, 5.0, 0.0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)
    set_perspective_projection()

# Proyección perspectiva para escenas 3D
def set_perspective_projection():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width/height, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

# Proyección ortográfica para escenas 3D
def set_orthographic_scene():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Define volúmen ortográfico que incluya la escena (coordenadas similares a gluPerspective)
    glOrtho(-4, 4, -3, 3, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

# Proyección ortográfica para menú 2D
def set_orthographic_menu():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -1, 1)
    glMatrixMode(GL_MODELVIEW)

# Renderizado de texto con OpenGL
def render_text(text, x, y, font):
    surface = font.render(text, True, (255, 255, 255, 255))
    data = pygame.image.tostring(surface, 'RGBA', True)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glRasterPos2f(x, y)
    glDrawPixels(surface.get_width(), surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, data)

# Dibuja el menú principal en 2D
def draw_menu():
    glPushAttrib(GL_ENABLE_BIT)
    glDisable(GL_DEPTH_TEST)
    glDisable(GL_LIGHTING)
    set_orthographic_menu()
    glLoadIdentity()
    lines = [
        "MENÚ PRINCIPAL - Práctica 5: Escena 3D",
        "",
        "1. Mostrar Cubo",
        "2. Mostrar Pirámide",
        "3. Mostrar Esfera",
        "4. Mostrar Cilindro",
        "5. Mostrar Superelipsoide",
        "6. Salir"
    ]
    y = height - 40
    for line in lines:
        render_text(line, 20, y, font)
        y -= 40
    glPopAttrib()
    # Restaurar proyección de escena
    if use_perspective:
        set_perspective_projection()
    else:
        set_orthographic_scene()

# Variables globales de toggles de proyección
use_perspective = True

# Función principal
def main():
    global use_perspective
    init_gl()

    # Cargar texturas y crear objetos
    textures = {k: load_texture(f"practica5-opengl/textures/{k}.jpg") for k in ["cube", "pyramid", "sphere", "cylinder", "superellipsoid"]}
    cube = Cube(textures["cube"])
    pyramid = Pyramid(textures["pyramid"])
    sphere = Sphere(textures["sphere"])
    cylinder = Cylinder(textures["cylinder"])
    superellipsoid = Superellipsoid(textures["superellipsoid"])

    current = None
    in_menu = True
    use_texture = True
    use_lighting = True
    translation = [0,0,-5]
    rotation = [0,0,0]
    scale = [1,1,1]

    clock = pygame.time.Clock()
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == QUIT:
                running = False
            elif e.type == KEYDOWN:
                if in_menu:
                    if e.key in (K_1,K_2,K_3,K_4,K_5):
                        current = [cube,pyramid,sphere,cylinder,superellipsoid][e.key-K_1]
                        in_menu = False
                    elif e.key == K_6:
                        running = False
                else:
                    if e.key == K_ESCAPE:
                        in_menu = True
                        translation, rotation, scale = [0,0,-5],[0,0,0],[1,1,1]
                    elif e.key == K_p:
                        use_perspective = not use_perspective
                        if use_perspective:
                            set_perspective_projection()
                        else:
                            set_orthographic_scene()
                    elif e.key == K_t:
                        use_texture = not use_texture
                    elif e.key == K_i:
                        use_lighting = not use_lighting
                        e = glEnable if use_lighting else glDisable
                        e(GL_LIGHTING)
                    elif e.key == K_r:
                        translation, rotation, scale = [0,0,-5],[0,0,0],[1,1,1]
                    elif e.key in (K_PLUS,K_KP_PLUS,K_EQUALS): scale = [s+0.05 for s in scale]
                    elif e.key in (K_MINUS,K_KP_MINUS):     scale = [max(0.1,s-0.05) for s in scale]

        # Movimiento continuo
        if not in_menu:
            keys = pygame.key.get_pressed()
            if keys[K_UP]: rotation[0]+=2
            if keys[K_DOWN]:rotation[0]-=2
            if keys[K_LEFT]:rotation[1]+=2
            if keys[K_RIGHT]:rotation[1]-=2
            if keys[K_w]:translation[1]+=0.1
            if keys[K_s]:translation[1]-=0.1
            if keys[K_a]:translation[0]-=0.1
            if keys[K_d]:translation[0]+=0.1

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        if in_menu:
            draw_menu()
        else:
            glLoadIdentity()
            glTranslatef(*translation)
            glRotatef(rotation[0],1,0,0)
            glRotatef(rotation[1],0,1,0)
            glRotatef(rotation[2],0,0,1)
            glScalef(*scale)
            if use_lighting: glEnable(GL_LIGHTING)
            else:           glDisable(GL_LIGHTING)
            if current:     current.draw(use_texture)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
