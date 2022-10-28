from random import choice, sample, shuffle

cartas = [chr(x) for x in range(0x1f0a1, 0x1f0af)]

print("He aquí las cartas presentadas: ", " ".join(cartas))

print("Selecciona una al azar:", " ".join(choice(cartas)))
print("Selecciona cinco al azar:", " ".join(sample(cartas, 5)))
shuffle(cartas)
print("Las mezcla:", " ".join(cartas))

