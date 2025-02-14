# Proyecto de NLP con spaCy

Este proyecto utiliza **spaCy** para el procesamiento de texto en español.

## Instalación

### Requisitos
- Python 3.x  
- pip (gestor de paquetes de Python)

### Clonar el repositorio
```sh
git clone https://github.com/hugomrj/spa_cy.git
cd spa_cy
```

### Instalación en Linux y macOS
```sh
# Crear y activar el entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Descargar el modelo de spaCy en español
python -m spacy download es_core_news_md
```

### Instalación en Windows
```sh
# Crear y activar el entorno virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Descargar el modelo de spaCy en español
python -m spacy download es_core_news_md
```

## Verificación de instalación
Para comprobar que todo está correctamente instalado, ejecuta el siguiente comando:
```sh
python test.py
```
Si todo está bien, verás un mensaje indicando que el entorno está listo.

## Uso
Puedes ejecutar el script de detección de palabras clave con:
```sh
python palabras_clave.py "Texto de prueba aquí"
```

