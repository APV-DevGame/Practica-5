from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

class Pyramid:
    def __init__(self, texture_id):
        self.texture_id = texture_id
        self.size = 1.0
        
        # Definir vértices de la pirámide (base cuadrada + punto superior)
        self.vertices = [
            # Base (cuadrado)
            [-self.size, -self.size, -self.size],  # 0 - Esquina inferior izquierda
            [self.size, -self.size, -self.size],   # 1 - Esquina inferior derecha
            [self.size, -self.size, self.size],    # 2 - Esquina superior derecha
            [-self.size, -self.size, self.size],   # 3 - Esquina superior izquierda
            
            # Punta de la pirámide
            [0.0, self.size, 0.0]                 # 4 - Punta
        ]
        
        # Calcular normales para cada cara
        # Cara frontal (triángulo)
        v1 = np.array(self.vertices[3]) - np.array(self.vertices[2])
        v2 = np.array(self.vertices[4]) - np.array(self.vertices[2])
        self.normal_front = np.cross(v1, v2)
        self.normal_front = self.normal_front / np.linalg.norm(self.normal_front)
        
        # Cara trasera (triángulo)
        v1 = np.array(self.vertices[1]) - np.array(self.vertices[0])
        v2 = np.array(self.vertices[4]) - np.array(self.vertices[0])
        self.normal_back = np.cross(v1, v2)
        self.normal_back = self.normal_back / np.linalg.norm(self.normal_back)
        
        # Cara derecha (triángulo)
        v1 = np.array(self.vertices[2]) - np.array(self.vertices[1])
        v2 = np.array(self.vertices[4]) - np.array(self.vertices[1])
        self.normal_right = np.cross(v1, v2)
        self.normal_right = self.normal_right / np.linalg.norm(self.normal_right)
        
        # Cara izquierda (triángulo)
        v1 = np.array(self.vertices[0]) - np.array(self.vertices[3])
        v2 = np.array(self.vertices[4]) - np.array(self.vertices[3])
        self.normal_left = np.cross(v1, v2)
        self.normal_left = self.normal_left / np.linalg.norm(self.normal_left)
        
        # Normal para la base (cuadrado)
        self.normal_base = [0.0, -1.0, 0.0]
        
        # Coordenadas de textura
        self.texcoords_tri = [
            [0.0, 0.0],  # Esquina inferior izquierda
            [1.0, 0.0],  # Esquina inferior derecha
            [0.5, 1.0]   # Punta superior
        ]
        
        self.texcoords_quad = [
            [0.0, 0.0],  # Esquina inferior izquierda
            [1.0, 0.0],  # Esquina inferior derecha
            [1.0, 1.0],  # Esquina superior derecha
            [0.0, 1.0]   # Esquina superior izquierda
        ]
    
    def draw(self, use_texture=True):
        if use_texture:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.texture_id)
        else:
            glDisable(GL_TEXTURE_2D)
        
        # Cara base (cuadrado)
        glBegin(GL_QUADS)
        glNormal3fv(self.normal_base)
        glTexCoord2fv(self.texcoords_quad[0])
        glVertex3fv(self.vertices[0])
        glTexCoord2fv(self.texcoords_quad[1])
        glVertex3fv(self.vertices[1])
        glTexCoord2fv(self.texcoords_quad[2])
        glVertex3fv(self.vertices[2])
        glTexCoord2fv(self.texcoords_quad[3])
        glVertex3fv(self.vertices[3])
        glEnd()
        
        # Caras laterales (triángulos)
        glBegin(GL_TRIANGLES)
        
        # Cara frontal
        glNormal3fv(self.normal_front)
        glTexCoord2fv(self.texcoords_tri[0])
        glVertex3fv(self.vertices[3])
        glTexCoord2fv(self.texcoords_tri[1])
        glVertex3fv(self.vertices[2])
        glTexCoord2fv(self.texcoords_tri[2])
        glVertex3fv(self.vertices[4])
        
        # Cara trasera
        glNormal3fv(self.normal_back)
        glTexCoord2fv(self.texcoords_tri[0])
        glVertex3fv(self.vertices[0])
        glTexCoord2fv(self.texcoords_tri[1])
        glVertex3fv(self.vertices[1])
        glTexCoord2fv(self.texcoords_tri[2])
        glVertex3fv(self.vertices[4])
        
        # Cara derecha
        glNormal3fv(self.normal_right)
        glTexCoord2fv(self.texcoords_tri[0])
        glVertex3fv(self.vertices[1])
        glTexCoord2fv(self.texcoords_tri[1])
        glVertex3fv(self.vertices[2])
        glTexCoord2fv(self.texcoords_tri[2])
        glVertex3fv(self.vertices[4])
        
        # Cara izquierda
        glNormal3fv(self.normal_left)
        glTexCoord2fv(self.texcoords_tri[0])
        glVertex3fv(self.vertices[3])
        glTexCoord2fv(self.texcoords_tri[1])
        glVertex3fv(self.vertices[0])
        glTexCoord2fv(self.texcoords_tri[2])
        glVertex3fv(self.vertices[4])
        
        glEnd()
        
        # Desactivar textura si estaba activada
        glDisable(GL_TEXTURE_2D)
