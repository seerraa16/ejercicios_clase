caracteres = input("Introduzca caracteres: ")
# Ejemplo con aA019Ã©Ã @#`{

for caracter in caracteres:
    print("El carácter {} tiene como ordinal {}".format(caracter, ord(caracter)))


# El carácter a tiene como ordinal 97
# El carácter A tiene como ordinal 65
# El carácter 0 tiene como ordinal 48
# El carácter 1 tiene como ordinal 49
# El carácter 9 tiene como ordinal 57
# El carácter Ã© tiene como ordinal 233
# El carácter Ã  tiene como ordinal 224
# El carácter @ tiene como ordinal 64
# El carácter # tiene como ordinal 35
# El carácter ` tiene como ordinal 96
# El carácter { tiene como ordinal 123


numeros = input("Escriba números, separados por un espacio: ")
# Ejemplo con 123 233 42 420 4200 4242 42000 424242

for numero in numeros.split(" "):
    try:
        print("El carácter de ordinal {} es {}".format(numero,
                                                        chr(int(numero))))
    except:
        print("El número {} no es un ordinal válido".format(numero))

# El carácter de ordinal 123 es {
# El carácter de ordinal 233 es Ã©
# El carácter de ordinal 42 es *
# El carácter de ordinal 420 es Æ¤
# El carácter de ordinal 4200 es á¨
# El carácter de ordinal 4242 es á‚’
# El carácter de ordinal 42000 es ê
# El carácter de ordinal 424242 es ñ§¤²


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

# âŒ˜ âœ„ â¤ â™› â˜  â˜¢ ğŸ“ ğŸ‚„ ğŸƒ‘
