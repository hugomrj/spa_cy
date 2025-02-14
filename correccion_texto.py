import sys
from spellchecker import SpellChecker

def corregir_ortografia(texto):
    # Inicializar el corrector ortográfico
    spell = SpellChecker(language='es')
    palabras = texto.split()
    
    # Corregir las palabras con errores ortográficos
    palabras_corregidas = []
    for palabra in palabras:
        correc = spell.correction(palabra)
        # Si la corrección no es la misma que la palabra original, la corregimos
        if correc != palabra:
            palabras_corregidas.append(correc)
        else:
            palabras_corregidas.append(palabra)
    
    # Unir las palabras corregidas de nuevo en un solo texto
    texto_corregido = " ".join(palabras_corregidas)
    return texto_corregido

# Comprobamos si se pasó un texto como parámetro
if len(sys.argv) > 1:
    # El primer argumento es el texto
    texto_entrada = sys.argv[1]
else:
    # Si no se pasa texto, se da un mensaje de error
    print("Por favor, pasa un texto como parámetro.")
    sys.exit(1)

# Corregir la ortografía del texto de entrada
texto_corregido = corregir_ortografia(texto_entrada)

# Mostrar el texto corregido
print(texto_corregido)

