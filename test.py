import spacy

# Cargar el modelo de spaCy en español
nlp = spacy.load("es_core_news_sm")

# Recibir un texto del usuario (puedes reemplazar esto con cualquier entrada de texto)
texto = input("Introduce tu texto: ")

# Procesar el texto con spaCy
doc = nlp(texto)

# Mostrar los tokens y sus partes del habla (POS tagging)
print("\nTokens y sus partes del habla:")
for token in doc:
    print(f"{token.text}: {token.pos_}")


