from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

class Cylinder:
    def __init__(self, texture_id):
        self.texture_id = texture_id
        self.base_radius = 1.0
        self.top_radius = 1.0
        self.height = 2.0
        self.slices = 32  # Divisiones alrededor del eje del cilindro
        self.stacks = 1   # Divisiones a lo largo del eje del cilindro
        
        # Crear un objeto quadric para el cilindro y las tapas
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
        
        # Guardar la matriz actual
        glPushMatrix()
        
        # Desplazar para que el cilindro esté centrado en el origen
        glTranslatef(0.0, 0.0, -self.height/2)
        
        # Dibujar el cilindro
        gluCylinder(self.quadric, self.base_radius, self.top_radius, self.height, self.slices, self.stacks)
        
        # Dibujar la tapa inferior
        glPushMatrix()
        glRotatef(180, 1, 0, 0)  # Rotar para que la normal apunte hacia afuera
        gluDisk(self.quadric, 0.0, self.base_radius, self.slices, 1)
        glPopMatrix()
        
        # Dibujar la tapa superior
        glPushMatrix()
        glTranslatef(0.0, 0.0, self.height)
        gluDisk(self.quadric, 0.0, self.top_radius, self.slices, 1)
        glPopMatrix()
        
        # Restaurar la matriz
        glPopMatrix()
        
        # Desactivar textura si estaba activada
        glDisable(GL_TEXTURE_2D)
    
    def __del__(self):
        # Liberar el objeto quadric al destruir la instancia
        if hasattr(self, 'quadric'):
            gluDeleteQuadric(self.quadric)
