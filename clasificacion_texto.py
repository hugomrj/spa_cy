import sys
import spacy
from spacy.util import get_installed_models
from spacy.training.example import Example

# Obtener la lista de modelos instalados
modelos_instalados = get_installed_models()

# Verificar si hay modelos instalados
if modelos_instalados:
    # Cargar el primer modelo disponible
    nlp = spacy.load(modelos_instalados[0])    
else:
    print("No hay modelos de spaCy instalados.")
    exit(1)

# Comprobamos si se pasó un texto como parámetro
if len(sys.argv) > 1:
    # El primer argumento es el texto
    texto_entrada = sys.argv[1]
else:
    # Si no se pasa texto, se da un mensaje de error
    print("Por favor, pasa un texto como parámetro.")
    sys.exit(1)

# Definir las categorías para clasificar el texto
categorias = ["Tecnología", "Negocios", "Salud", "Deportes", "Educación"]

# Función para predecir la categoría de un texto
def clasificar_texto(texto):
    # Procesar el texto con el modelo de spaCy
    doc = nlp(texto)
    
    # Aquí puedes agregar un modelo de clasificación entrenado o utilizar la
    # capacidad de clasificación basada en entidades del modelo spaCy
    # Para fines de ejemplo, asignamos una categoría de forma aleatoria
    import random
    categoria = random.choice(categorias)  # Esto es un ejemplo simple
    
    return categoria

# Clasificar el texto
categoria_predicha = clasificar_texto(texto_entrada)

# Mostrar la categoría predicha
print(f"El texto pertenece a la categoría: {categoria_predicha}")




#python clasificacion_texto.py "La inteligencia artificial está transformando el mundo de la tecnología."
