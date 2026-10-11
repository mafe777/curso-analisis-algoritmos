# Semana 02 - Configuración del Entorno y Sintaxis en Python

## Entorno Virtual
Para crear y activar el entorno virtual utilizado en este laboratorio y en todo el curso, se ejecutaron los siguientes comandos desde la raíz del repositorio:

```bash
# Creación del entorno virtual único en la raíz
python -m venv venv

# Activación del entorno virtual en Windows (PowerShell)
.\venv\Scripts\Activate

# Instalación de dependencias y generación del archivo reproducible
pip install matplotlib
pip freeze > requirements.txt