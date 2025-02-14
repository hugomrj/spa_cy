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

# Función para extraer las frases clave
def extraer_frases_clave(doc):
    frases_clave = []
    
    # Extraemos sustantivos, adjetivos y verbos
    for token in doc:
        if token.pos_ in ['NOUN', 'ADJ', 'VERB']:  # NOMBRES, ADJETIVOS, VERBOS
            frases_clave.append(token.text)
    
    return frases_clave

# Extraemos las frases clave
frases_clave = extraer_frases_clave(doc)

# Mostramos las frases clave
print("Frases clave extraídas:")
print(', '.join(frases_clave))


#python frases_clave.py "La inteligencia artificial está transformando el marketing digital y la tecnología."
