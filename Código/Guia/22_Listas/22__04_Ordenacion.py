frase = "Ah! La frase a ordenar se ha declarado con éxito."

frase = frase.replace("!", "").replace(".", "")

palabras = frase.split()

print("palabras no ordenadas: {}".format(palabras))

palabras.sort()

print("Ordenación simple: {}".format(palabras))

palabras.sort(key=str.lower)

print("Tratar mayúsculas: {}".format(palabras))

translation = str.maketrans(
   "àäâéèëêïîöôùüûÿŷç_-",
   "aaaeeeeiioouuuyyc  ",
   "#~.?,;:!")

print("Diccionario de reemplazo", translation)

def transformation(x):
    return x.lower().translate(translation)

palabras.sort(key=transformation)

print("Acentos tratados: {}".format(palabras))

