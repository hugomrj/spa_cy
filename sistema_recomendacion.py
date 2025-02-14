import sys
import spacy
from spacy.util import get_installed_models
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

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

# Artículos a recomendar (esto normalmente vendría de una base de datos o archivo)
articulos = [
    "El análisis de datos es fundamental para la toma de decisiones.",
    "La inteligencia artificial está cambiando el mundo de la tecnología.",
    "El marketing digital se está convirtiendo en una parte esencial de los negocios.",
    "El desarrollo web se está moviendo hacia el uso de frameworks modernos.",
    "Las nuevas tendencias en inteligencia artificial incluyen aprendizaje automático y redes neuronales profundas."
]

# Procesar el texto de entrada
doc_entrada = nlp(texto_entrada)

# Función para calcular la similitud entre el texto de entrada y los artículos
def obtener_similitudes(texto_entrada, articulos):
    similitudes = []
    vector_entrada = texto_entrada.vector
    for articulo in articulos:
        doc_articulo = nlp(articulo)
        vector_articulo = doc_articulo.vector

        # Normalizar los vectores antes de calcular la similitud
        vector_entrada_normalizado = vector_entrada / np.linalg.norm(vector_entrada)
        vector_articulo_normalizado = vector_articulo / np.linalg.norm(vector_articulo)

        similitud = cosine_similarity([vector_entrada_normalizado], [vector_articulo_normalizado])[0][0]
        similitudes.append(similitud)
    return similitudes

# Obtener las similitudes
similitudes = obtener_similitudes(doc_entrada, articulos)

# Ordenar los artículos según la similitud con el texto de entrada
articulos_similares = sorted(zip(similitudes, articulos), reverse=True)

# Mostrar los artículos recomendados
print("Recomendaciones basadas en el texto proporcionado:")
for idx, (similitud, articulo) in enumerate(articulos_similares, start=1):
    print(f"Recomendación {idx}: {articulo} (Similitud: {similitud:.2f})")
