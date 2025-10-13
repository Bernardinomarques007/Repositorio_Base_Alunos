# Conversor de Moedas USD/BRL 

# Definição da taxa de câmbio fixa (1 dólar = 5 reais)
TAXA_DOLAR_PARA_REAL = 5

# Funções de conversão
def converter_dolar_para_real(valor_dolar):
    return valor_dolar * TAXA_DOLAR_PARA_REAL

def converter_real_para_dolar(valor_real):
    return valor_real / TAXA_DOLAR_PARA_REAL

# Loop principal do programa
while True:
    # Menu de opções
    print("\n=== Conversor de Moedas ===")
    print("1 - Converter Dólar para Real")
    print("2 - Converter Real para Dólar")
    print("0 - Sair do programa")

    # Recebe a escolha do usuário
    opcao = input("Digite sua opção: ")

    # Opção 1: Converter Dólar para Real
    if opcao == "1":
        valor_dolar = float(input("Digite o valor em dólares (USD): "))
        valor_real = converter_dolar_para_real(valor_dolar)
        print(f"US$ {valor_dolar:.2f} = R$ {valor_real:.2f}")

    # Opção 2: Converter Real para Dólar
    elif opcao == "2":
        valor_real = float(input("Digite o valor em reais (BRL): "))
        valor_dolar = converter_real_para_dolar(valor_real)
        print(f"R$ {valor_real:.2f} = US$ {valor_dolar:.2f}")

    # Opção 0: Sair do programa
    elif opcao == "0":
        print("Obrigado por usar o conversor. Até mais!")
        break

    # Tratamento de opção inválida
    else:
        print("Opção inválida! Por favor, digite 1, 2 ou 0.")
