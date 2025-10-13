numeros = [12, 5, 23, 8, 19]
maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print("O maior número é:", maior)
