# Desafio: Classificador de Números em Intervalos
# Crie uma função chamada classificar_numero que recebe um número e retorna uma
# mensagem com base no intervalo em que ele se encontra:


def classificar_numero(num):

    if num < 0 :
        print("| Número negativo")
    elif num > 0 and num <=10:
        print("| Entre 0 e 10")
    elif num > 10 and num <=100:
        print("| Entre 10 e 100")
    elif num > 100:
        print("| Maior que 100")
    else:
        print("| Você não digitou um número, ou seu numero é igual a 0")


print(classificar_numero(float(input("| Digite seu numero " ))))

