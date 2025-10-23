numeros = [1,-23,3,344,5,-6,97,8,19,-910]

calc = map(lambda x: x % 2 == 0, numeros)

print(list(calc))