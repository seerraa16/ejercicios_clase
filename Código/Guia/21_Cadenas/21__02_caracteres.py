caracteres = input("Introduzca caracteres: ")
# Ejemplo con aA019éà@#`{

for caracter in caracteres:
    print("El car�cter {} tiene como ordinal {}".format(caracter, ord(caracter)))


# El car�cter a tiene como ordinal 97
# El car�cter A tiene como ordinal 65
# El car�cter 0 tiene como ordinal 48
# El car�cter 1 tiene como ordinal 49
# El car�cter 9 tiene como ordinal 57
# El car�cter é tiene como ordinal 233
# El car�cter à tiene como ordinal 224
# El car�cter @ tiene como ordinal 64
# El car�cter # tiene como ordinal 35
# El car�cter ` tiene como ordinal 96
# El car�cter { tiene como ordinal 123


numeros = input("Escriba n�meros, separados por un espacio: ")
# Ejemplo con 123 233 42 420 4200 4242 42000 424242

for numero in numeros.split(" "):
    try:
        print("El car�cter de ordinal {} es {}".format(numero,
                                                        chr(int(numero))))
    except:
        print("El n�mero {} no es un ordinal v�lido".format(numero))

# El car�cter de ordinal 123 es {
# El car�cter de ordinal 233 es é
# El car�cter de ordinal 42 es *
# El car�cter de ordinal 420 es Ƥ
# El car�cter de ordinal 4200 es ၨ
# El car�cter de ordinal 4242 es ႒
# El car�cter de ordinal 42000 es ꐐ
# El car�cter de ordinal 424242 es 񧤲


print("Y ahora, algunos caracteres poco usuales:")
print(chr(0x2318),
      chr(0x2704),
      chr(0x2764),
      chr(0x265b),
      chr(0x2620),
      chr(0x2622),
      chr(0x1f053),
      chr(0x1f084),
      chr(0x1f0d1))

# ⌘ ✄ ❤ ♛ ☠ ☢ 🁓 🂄 🃑
