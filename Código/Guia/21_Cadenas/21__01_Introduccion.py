frase = input("Introduzca una frase (con min, May, Num, acentos, y espacios): ")
# Ejemplo con eStE es el abc de b_a_ba

print("Minúsculas        : " + frase.lower())
print("Mayúsculas        : %s" % frase.upper())
print("frase en mayúsculas: {}".format(frase.capitalize()))
print("palabras en mayúsculas :", frase.title())

# Minúsculas        : este es el abc de b_a_ba
# Mayúsculas        : ESTE ES EL ABC DE B_A_BA
# frase en mayúsculas: Este es el abc de b_a_ba
# palabras en mayúsculas : Este Es El Abc De B_A_Ba

print("Longitud de la cadena: {}".format(len(frase)))
# Longitud de la cadena: 24

print("¿Su frase contiene la letra 'a'?", "a" in frase)
print("¿Su frase contiene la secuencia 'abc'?", "abc" in frase)

# ¿Su frase contiene la letra 'a'? True
# ¿Su frase contiene la secuencia 'abc'? True


num = frase.count("a")
print("¿Cuántas ocurrencias de 'a' se encuentran en la frase?", num)
if num > 0:
    index = frase.find("a")
    print("¿Dónde se encuentra la primera ocurrencia de 'a'?", index)
    for i in range(1, num):
        index = frase.find("a", index + 1)
        print("La ocurrencia numéro {} de 'a' se encuentra en el índice {}".format(
            i + 1, index))

# ¿Cuántas ocurrencias de 'a' se encuentran en la frase? 3
# ¿Dónde se encuentra la primera ocurrencia de 'a'? 11
# La ocurrencia numéro 2 de 'a' se encuentra en el índice 20
# La ocurrencia numéro 3 de 'a' se encuentra en el índice 23


print("Reemplazar las 'a' por '*':")
frase_oculta = frase.replace("a", "*")
print(frase)
print(frase_oculta)

# Reemplazar las 'a' por '*':
# eStE es el abc de b_a_ba
# eStE es el *bc de b_*_b*


#
# Ejercicio: Cuente el número de palabras de una frase
#


def num_palabras1(frase):
    return len(frase.split(" "))

def num_palabras2(frase):
    return frase.count(" ") + 1



