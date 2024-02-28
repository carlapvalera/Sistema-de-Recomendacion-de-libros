#!/bin/bash

# Obtiene la ruta del proyecto desde el directorio actual
PROJECT_PATH=$(pwd)

# Navega al directorio del proyecto
cd $PROJECT_PATH/Sistema-de-Recomendacion-de-libros

# Activa el entorno virtual
source venv/bin/activate

# Ejecuta Streamlit
streamlit run src/gui.py
# Desactiva el entorno virtual
deactivate