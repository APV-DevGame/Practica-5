from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

class Sphere:
    def __init__(self, texture_id):
        self.texture_id = texture_id
        self.radius = 1.0
        self.slices = 32  # Divisiones horizontales
        self.stacks = 32  # Divisiones verticales
        
        # Crear un objeto quadric para la esfera
        self.quadric = gluNewQuadric()
        gluQuadricNormals(self.quadric, GLU_SMOOTH)
        gluQuadricTexture(self.quadric, GL_TRUE)
    
    def draw(self, use_texture=True):
        if use_texture:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.texture_id)
            gluQuadricTexture(self.quadric, GL_TRUE)
        else:
            glDisable(GL_TEXTURE_2D)
            gluQuadricTexture(self.quadric, GL_FALSE)
        
        # Dibujar la esfera
        gluSphere(self.quadric, self.radius, self.slices, self.stacks)
        
        # Desactivar textura si estaba activada
        glDisable(GL_TEXTURE_2D)
    
    def __del__(self):
        # Liberar el objeto quadric al destruir la instancia
        if hasattr(self, 'quadric'):
            gluDeleteQuadric(self.quadric)
