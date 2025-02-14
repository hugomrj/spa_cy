import spacy
import sys

from spacy.util import get_installed_models


# Obtener la lista de modelos instalados
modelos_instalados = get_installed_models()

# Verificar si hay modelos instalados
if modelos_instalados:
    # Cargar el primer modelo disponible
    nlp = spacy.load(modelos_instalados[0])    
else:
    print("No hay modelos de spaCy instalados.")
    exit(1)






def detectar_palabras_clave(texto):
    # Procesar el texto con spaCy
    doc = nlp(texto)

    # Extraer las palabras clave (sustantivos y adjetivos)
    palabras_clave = [token.text for token in doc if token.pos_ in ['NOUN', 'ADJ']]

    return palabras_clave





# Comprobamos si se pasó un texto como parámetro
if len(sys.argv) > 1:
    # El primer argumento es el texto
    texto_entrada = sys.argv[1]
else:
    # Si no se pasa texto, se da un mensaje de error
    print("Por favor, pasa un texto como parámetro.")
    sys.exit(1)

# Llamar a la función para detectar palabras clave
palabras_clave = detectar_palabras_clave(texto_entrada)

# Mostrar las palabras clave
print("Palabras clave detectadas:")
for palabra in palabras_clave:
    print(palabra)



#python detectar_palabras_clave.py "¿Qué ofertas tienen hoy?"
