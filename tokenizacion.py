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

# Procesamos el texto con spaCy
doc = nlp(texto_entrada)

# Mostramos los tokens (palabras) del texto
print("Tokens en el texto:")
for token in doc:
    print(f"Texto: {token.text} | Lemma: {token.lemma_} | POS: {token.pos_}")

# También mostramos las oraciones del texto
print("\nOraciones en el texto:")
for sent in doc.sents:
    print(f"Oración: {sent.text}")




#python tokenizacion.py "El precio del petróleo subió un 10% en los últimos tres meses."
