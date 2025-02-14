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

# Verificar si se pasó un argumento
if len(sys.argv) > 1:
    texto = sys.argv[1]
else:
    print("Por favor, proporciona un texto como argumento.")
    sys.exit(1)

# Procesar el texto con spaCy
doc = nlp(texto)

# Análisis morfosintáctico
print("Palabra - POS - Lematización - Dependencia")
for token in doc:
    print(f"{token.text} - {token.pos_} - {token.lemma_} - {token.dep_}")



#python analisis_morfosinta.py "la oracion esta aqui"