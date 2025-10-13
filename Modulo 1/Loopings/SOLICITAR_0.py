numeros = 0

while True:
    num = int(input("Digite um numero inteiro de 0 a 100: " ))
    if num > 0:
        numeros += num
    elif num == 0:
        print("O numero digitado é igual a 0, isso encerra o progama")
        print(f"A soma de todos os numeros digitados é {numeros}")
        break
