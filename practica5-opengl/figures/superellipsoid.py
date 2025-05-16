from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

class Superellipsoid:
    def __init__(self, texture_id):
        self.texture_id = texture_id
        self.a = 1.0  # Radio x
        self.b = 1.0  # Radio y
        self.c = 1.0  # Radio z
        self.e1 = 0.8  # Exponente para latitud (vertical) - controla "redondez"
        self.e2 = 0.8  # Exponente para longitud (horizontal) - controla "redondez"
        
        # Divisiones para la superficie paramétrica
        self.u_segments = 24  # divisiones longitudinales
        self.v_segments = 24  # divisiones latitudinales
    
    # Función para calcular el signo
    def sign(self, x):
        return 1.0 if x >= 0 else -1.0
    
    # Funciones auxiliares para superelipsoide
    def c_e(self, angle, e):
        return self.sign(math.cos(angle)) * math.pow(abs(math.cos(angle)), e)
    
    def s_e(self, angle, e):
        return self.sign(math.sin(angle)) * math.pow(abs(math.sin(angle)), e)
    
    # Función para calcular un punto en la superficie del superelipsoide
    def superellipsoid_point(self, u, v):
        # u va de 0 a 2*pi (longitud)
        # v va de -pi/2 a pi/2 (latitud)
        
        # Calcular coordenadas paramétricas
        cu = self.c_e(u, self.e1)
        su = self.s_e(u, self.e1)
        cv = self.c_e(v, self.e2)
        sv = self.s_e(v, self.e2)
        
        # Calcular coordenadas cartesianas
        x = self.a * cv * cu
        y = self.b * cv * su
        z = self.c * sv
        
        return [x, y, z]
    
    # Función para calcular la normal en un punto
    def superellipsoid_normal(self, u, v):
        # Calcular derivadas parciales
        cu = self.c_e(u, self.e1)
        su = self.s_e(u, self.e1)
        cv = self.c_e(v, self.e2)
        sv = self.s_e(v, self.e2)
        
        # Componentes de la normal (aproximación)
        nx = cu * cv / (self.a * self.a)
        ny = su * cv / (self.b * self.b)
        nz = sv / (self.c * self.c)
        
        # Normalizar
        length = math.sqrt(nx*nx + ny*ny + nz*nz)
        if length > 0:
            return [nx/length, ny/length, nz/length]
        else:
            return [0.0, 0.0, 1.0]  # Valor predeterminado
    
    def draw(self, use_texture=True):
        if use_texture:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.texture_id)
        else:
            glDisable(GL_TEXTURE_2D)
        
        # Rango de parámetros
        u_start = 0
        u_end = 2 * math.pi
        v_start = -math.pi / 2
        v_end = math.pi / 2
        
        # Incrementos
        u_step = (u_end - u_start) / self.u_segments
        v_step = (v_end - v_start) / self.v_segments
        
        # Generar malla de triángulos
        for i in range(self.u_segments):
            u1 = u_start + i * u_step
            u2 = u_start + (i + 1) * u_step
            
            glBegin(GL_TRIANGLE_STRIP)
            
            for j in range(self.v_segments + 1):
                v = v_start + j * v_step
                
                # Coordenadas de textura
                tex_u1 = i / self.u_segments
                tex_u2 = (i + 1) / self.u_segments
                tex_v = j / self.v_segments
                
                # Puntos y normales
                p1 = self.superellipsoid_point(u1, v)
                n1 = self.superellipsoid_normal(u1, v)
                p2 = self.superellipsoid_point(u2, v)
                n2 = self.superellipsoid_normal(u2, v)
                
                # Primer vértice
                glTexCoord2f(tex_u1, tex_v)
                glNormal3fv(n1)
                glVertex3fv(p1)
                
                # Segundo vértice
                glTexCoord2f(tex_u2, tex_v)
                glNormal3fv(n2)
                glVertex3fv(p2)
            
            glEnd()
        
        # Desactivar textura si estaba activada
        glDisable(GL_TEXTURE_2D)
