from OpenGL.GL import *
from OpenGL.GLU import *  
import pygame
import os

def load_texture(filepath):
    """
    Carga una imagen y la convierte en una textura OpenGL.
    
    Args:
        filepath: Ruta de la imagen a cargar.
        
    Returns:
        ID de la textura en OpenGL.
    """
    # Comprobar si el archivo existe
    if not os.path.isfile(filepath):
        print(f"Error: No se pudo encontrar la textura en {filepath}")
        # Crear textura predeterminada
        return create_default_texture()
    
    try:
        # Cargar la imagen con Pygame
        surface = pygame.image.load(filepath)
        
        # Convertir la imagen a RGB si tiene alpha
        if surface.get_bitsize() == 32:  # Has alpha channel
            surface = pygame.Surface(surface.get_size(), pygame.SRCALPHA, 32)
            surface.blit(surface, (0, 0))
        
        # Obtener dimensiones
        texture_width = surface.get_width()
        texture_height = surface.get_height()
        
        # Obtener los datos de píxeles en formato adecuado para OpenGL
        texture_data = pygame.image.tostring(surface, "RGBA", True)
        
        # Generar ID para la textura
        texture_id = glGenTextures(1)
        
        # Enlazar la textura
        glBindTexture(GL_TEXTURE_2D, texture_id)
        
        # Configurar los parámetros de la textura
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        
        # Cargar los datos de la textura
        glTexImage2D(
            GL_TEXTURE_2D, 0, GL_RGBA, texture_width, texture_height, 0, 
            GL_RGBA, GL_UNSIGNED_BYTE, texture_data
        )
        
        # Generar mipmaps
        gluBuild2DMipmaps(
            GL_TEXTURE_2D, GL_RGBA, texture_width, texture_height,
            GL_RGBA, GL_UNSIGNED_BYTE, texture_data
        )
        
        return texture_id
    except Exception as e:
        print(f"Error al cargar la textura {filepath}: {e}")
        return create_default_texture()

def create_default_texture():
    """
    Crea una textura predeterminada de tablero de ajedrez cuando no se puede cargar la textura original.
    
    Returns:
        ID de la textura en OpenGL.
    """
    # Dimensiones de la textura
    width, height = 64, 64
    
    # Crear una superficie de Pygame para el tablero de ajedrez
    surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    
    # Colores del tablero
    color1 = (200, 200, 200, 255)  # Gris claro
    color2 = (100, 100, 100, 255)  # Gris oscuro
    
    # Dibujar el tablero de ajedrez
    tile_size = 8  # Tamaño de cada cuadrado
    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):
            color = color1 if ((x // tile_size) + (y // tile_size)) % 2 == 0 else color2
            pygame.draw.rect(surface, color, (x, y, tile_size, tile_size))
    
    # Obtener los datos de píxeles
    texture_data = pygame.image.tostring(surface, "RGBA", True)
    
    # Generar ID para la textura
    texture_id = glGenTextures(1)
    
    # Enlazar la textura
    glBindTexture(GL_TEXTURE_2D, texture_id)
    
    # Configurar los parámetros de la textura
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    
    # Cargar los datos de la textura
    glTexImage2D(
        GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, 
        GL_RGBA, GL_UNSIGNED_BYTE, texture_data
    )
    
    return texture_id
