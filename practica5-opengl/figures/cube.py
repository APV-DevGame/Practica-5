from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

class Cube:
    def __init__(self, texture_id):
        self.texture_id = texture_id
        self.size = 1.0
        
        # Definir vértices del cubo
        self.vertices = [
            # Cara frontal (Z+)
            [-self.size, -self.size, self.size],
            [self.size, -self.size, self.size],
            [self.size, self.size, self.size],
            [-self.size, self.size, self.size],
            
            # Cara trasera (Z-)
            [-self.size, -self.size, -self.size],
            [self.size, -self.size, -self.size],
            [self.size, self.size, -self.size],
            [-self.size, self.size, -self.size]
        ]
        
        # Definir normales para cada cara
        self.normals = [
            [0.0, 0.0, 1.0],    # Frontal
            [0.0, 0.0, -1.0],   # Trasera
            [1.0, 0.0, 0.0],    # Derecha
            [-1.0, 0.0, 0.0],   # Izquierda
            [0.0, 1.0, 0.0],    # Superior
            [0.0, -1.0, 0.0]    # Inferior
        ]
        
        # Coordenadas de textura
        self.texcoords = [
            [0.0, 0.0],
            [1.0, 0.0],
            [1.0, 1.0],
            [0.0, 1.0]
        ]
    
    def draw(self, use_texture=True):
        if use_texture:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.texture_id)
        else:
            glDisable(GL_TEXTURE_2D)
        
        glBegin(GL_QUADS)
        
        # Cara frontal (Z+)
        glNormal3fv(self.normals[0])
        glTexCoord2fv(self.texcoords[0])
        glVertex3fv(self.vertices[0])
        glTexCoord2fv(self.texcoords[1])
        glVertex3fv(self.vertices[1])
        glTexCoord2fv(self.texcoords[2])
        glVertex3fv(self.vertices[2])
        glTexCoord2fv(self.texcoords[3])
        glVertex3fv(self.vertices[3])
        
        # Cara trasera (Z-)
        glNormal3fv(self.normals[1])
        glTexCoord2fv(self.texcoords[0])
        glVertex3fv(self.vertices[7])
        glTexCoord2fv(self.texcoords[1])
        glVertex3fv(self.vertices[6])
        glTexCoord2fv(self.texcoords[2])
        glVertex3fv(self.vertices[5])
        glTexCoord2fv(self.texcoords[3])
        glVertex3fv(self.vertices[4])
        
        # Cara derecha (X+)
        glNormal3fv(self.normals[2])
        glTexCoord2fv(self.texcoords[0])
        glVertex3fv(self.vertices[1])
        glTexCoord2fv(self.texcoords[1])
        glVertex3fv(self.vertices[5])
        glTexCoord2fv(self.texcoords[2])
        glVertex3fv(self.vertices[6])
        glTexCoord2fv(self.texcoords[3])
        glVertex3fv(self.vertices[2])
        
        # Cara izquierda (X-)
        glNormal3fv(self.normals[3])
        glTexCoord2fv(self.texcoords[0])
        glVertex3fv(self.vertices[4])
        glTexCoord2fv(self.texcoords[1])
        glVertex3fv(self.vertices[0])
        glTexCoord2fv(self.texcoords[2])
        glVertex3fv(self.vertices[3])
        glTexCoord2fv(self.texcoords[3])
        glVertex3fv(self.vertices[7])
        
        # Cara superior (Y+)
        glNormal3fv(self.normals[4])
        glTexCoord2fv(self.texcoords[0])
        glVertex3fv(self.vertices[3])
        glTexCoord2fv(self.texcoords[1])
        glVertex3fv(self.vertices[2])
        glTexCoord2fv(self.texcoords[2])
        glVertex3fv(self.vertices[6])
        glTexCoord2fv(self.texcoords[3])
        glVertex3fv(self.vertices[7])
        
        # Cara inferior (Y-)
        glNormal3fv(self.normals[5])
        glTexCoord2fv(self.texcoords[0])
        glVertex3fv(self.vertices[4])
        glTexCoord2fv(self.texcoords[1])
        glVertex3fv(self.vertices[5])
        glTexCoord2fv(self.texcoords[2])
        glVertex3fv(self.vertices[1])
        glTexCoord2fv(self.texcoords[3])
        glVertex3fv(self.vertices[0])
        
        glEnd()
        
        # Desactivar textura si estaba activada
        glDisable(GL_TEXTURE_2D)
