def diccionario(numero):
  diccionario = {}
  for i in range(1, numero + 1):
    diccionario[i] = i ** 2
  return diccionario


def orden():
  numero = int(input("Introduce un número: "))
  diccionario = diccionario(numero)
  print(diccionario)


if __name__ == "__orden__":
  orden()

