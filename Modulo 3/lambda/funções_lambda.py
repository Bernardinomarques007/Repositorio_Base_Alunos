jogadores = [
    {'nome': 'PlayerOne', 'score': 1200, 'level': 15},
    {'nome': 'Ninjagui', 'score': 950, 'level': 12},
    {'nome': 'PaiTaOff', 'score': 200, 'level': 3},
    {'nome': 'Aninha_Gamer', 'score': 1500, 'level': 18},
    {'nome': 'Zezinho', 'score': 400, 'level': 5},
]

ranking = sorted(jogadores, key=lambda jogador: jogador['score'], reverse=True)
for jogador in ranking:
    print(jogador)
    