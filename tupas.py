import random

def tupla():
  tupla = tuple(random.randint(1, 10) for _ in range(10))
  return tupla

def cubo():
  tupla = tupla()
  for numero in tupla:
    print(f"{numero}: {numero**2} {numero**3}")

if __name__ == "__cubo__":
  cubo()