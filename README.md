Implementación de una Escena 3D Realista con OpenGL y PyGame

Descripción
Este proyecto implementa una escena 3D realista utilizando OpenGL y PyGame, donde se pueden visualizar y manipular diferentes figuras 3D con transformaciones, iluminación y texturas.

Requisitos
- Python 3.10 o superior
- PyOpenGL
- PyOpenGL_accelerate
- Pygame
- NumPy

Instalación
1. Clona este repositorio:
   git clone https://github.com/tu-usuario/practica5-opengl.git
   cd practica5-opengl

2. Crea un entorno virtual (opcional pero recomendado):
   python -m venv venv
   En Windows: venv\Scripts\activate
   En macOS/Linux: source venv/bin/activate

3. Instala las dependencias:
   pip install PyOpenGL PyOpenGL_accelerate pygame numpy

Estructura del Proyecto
practica5-opengl/
├── main.py                  # Archivo principal
├── figures/                 # Módulos para las figuras 3D
│   ├── __init__.py
│   ├── cube.py              # Implementación del cubo
│   ├── pyramid.py           # Implementación de la pirámide
│   ├── sphere.py            # Implementación de la esfera
│   ├── cylinder.py          # Implementación del cilindro
│   └── superellipsoid.py    # Implementación del superelipsoide
├── utils/                   # Utilidades
│   ├── __init__.py
│   └── texture_loader.py    # Cargador de texturas
└── textures/                # Directorio para las texturas
    ├── cube.jpg
    ├── pyramid.jpg
    ├── sphere.jpg
    ├── cylinder.jpg
    └── superellipsoid.jpg

Ejecución
python main.py

Controles

Menú Principal
- 1 – Mostrar Cubo
- 2 – Mostrar Pirámide
- 3 – Mostrar Esfera
- 4 – Mostrar Cilindro
- 5 – Mostrar Superelipsoide
- 6 – Salir del programa

Controles de Visualización
- Flechas (↑, ↓, ←, →) – Rotar la figura sobre los ejes X/Y
- W, S, A, D – Trasladar la figura en los ejes X/Z
- + / - – Escalar la figura
- R – Reiniciar transformaciones
- P – Alternar entre proyección en perspectiva y paralela
- T – Activar/desactivar textura
- I – Activar/desactivar iluminación
- ESC – Volver al menú principal

Características Implementadas
- Figuras 3D: Cubo, Pirámide, Esfera, Cilindro, Superelipsoide
- Transformaciones: traslación, rotación, escalado
- Iluminación activable
- Texturizado
- Cambio de proyección (perspectiva / ortográfica)

Autor
Alan PV
