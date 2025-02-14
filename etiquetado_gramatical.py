import sys
import spacy
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

# Comprobamos si se pasó un texto como parámetro
if len(sys.argv) > 1:
    # El primer argumento es el texto
    texto_entrada = sys.argv[1]
else:
    # Si no se pasa texto, se da un mensaje de error
    print("Por favor, pasa un texto como parámetro.")
    sys.exit(1)

# Procesamos el texto
doc = nlp(texto_entrada)

# Mostramos el etiquetado gramatical
print("Etiquetado gramatical (POS tagging) de los tokens:")
for token in doc:
    print(f"{token.text} -> {token.pos_}")


#python etiquetado_gramatical.py "La inteligencia artificial está revolucionando el marketing digital."
