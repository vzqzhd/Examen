def most_repeated(words):
    max_word = ''
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq


def count_words(text):
    """Función que cuenta el número de veces que aparece cada palabra en un texto.
    Parámetros:
        - text: Es una cadena de caracteres.
    Devuelve: 
        Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia.
    """
    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words

' Defino el texto a evaluar
text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'

' Imprimo por pantalla
print ("Palabras: Cantidad")
print(count_words(text))
print ("Palabra Mas repetida: Cantidad")
print(most_repeated(count_words(text)))
