contador_par = 0

contador_impar = 0

soma_par = 0

soma_impar = 0

pares = []

impares = []

numerosdigitados=[]

for I in range(1,11):
    
    num = int(input("Digite um numero inteiro: "))

    if num % 2 == 0:

        numerosdigitados.append(num)

        soma_par += I

        contador_par += 1

        pares.append(I)

    else:

        soma_impar += I

        contador_impar += 1

        impares.append(I)



print("| Sua lista contém os seguintes numeros: ", numerosdigitados)

print("| Os numeros pares são: ", pares)

print("| Os numeros impares são: ", impares)

print("| Sua lista tem ",contador_par," numeros pares")

print("| Sua lista tem ",contador_impar," numeros impares")

print("| O resultado de todos os numeros pares são: ", soma_par)

print("| O resultado de todos os numeros impares são: ", soma_impar)
