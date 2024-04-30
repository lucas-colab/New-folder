def decimal_para_binario(numero):
    binario = ""
    passos = []
    while numero > 0:
        passos.append(f"{numero} / 2 = {numero // 2}, resto = {numero % 2}")
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2
    passos.append("Resultado: " + binario)
    return passos

def decimal_para_hexadecimal(numero):
    hexadecimal = ""
    passos = []
    while numero > 0:
        passos.append(f"{numero} / 16 = {numero // 16}, resto = {numero % 16}")
        resto = numero % 16
        if resto < 10:
            hexadecimal = str(resto) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + resto - 10) + hexadecimal
        numero = numero // 16
    passos.append("Resultado: " + hexadecimal)
    return passos

def decimal_para_octal(numero):
    octal = ""
    passos = []
    while numero > 0:
        passos.append(f"{numero} / 8 = {numero // 8}, resto = {numero % 8}")
        resto = numero % 8
        octal = str(resto) + octal
        numero = numero // 8
    passos.append("Resultado: " + octal)
    return passos

def binario_para_decimal(numero):
    decimal = 0
    passos = []
    for i, digito in enumerate(reversed(numero)):
        valor_digito = int(digito)
        passos.append(f"{valor_digito} * 2^{i} = {valor_digito * (2 ** i)}")
        decimal += valor_digito * (2 ** i)
    passos.append("Resultado: " + str(decimal))
    return passos

def hexadecimal_para_decimal(numero):
    decimal = 0
    passos = []
    for i, digito in enumerate(reversed(numero)):
        valor_digito = int(digito, 16)
        passos.append(f"{valor_digito} * 16^{i} = {valor_digito * (16 ** i)}")
        decimal += valor_digito * (16 ** i)
    passos.append("Resultado: " + str(decimal))
    return passos

def octal_para_decimal(numero):
    decimal = 0
    passos = []
    for i, digito in enumerate(reversed(numero)):
        valor_digito = int(digito)
        passos.append(f"{valor_digito} * 8^{i} = {valor_digito * (8 ** i)}")
        decimal += valor_digito * (8 ** i)
    passos.append("Resultado: " + str(decimal))
    return passos

def main():
    print("Bem-vindo ao conversor de sistemas de numeração!")
    while True:
        print("\nEscolha a operação desejada:")
        print("1. Decimal para Binário")
        print("2. Decimal para Hexadecimal")
        print("3. Decimal para Octal")
        print("4. Binário para Decimal")
        print("5. Hexadecimal para Decimal")
        print("6. Octal para Decimal")
        print("7. Sair")
        
        escolha = input("Digite o número da operação desejada: ")
        
        switch = {
            "1": lambda: decimal_para_binario(int(input("Digite o número decimal: "))),
            "2": lambda: decimal_para_hexadecimal(int(input("Digite o número decimal: "))),
            "3": lambda: decimal_para_octal(int(input("Digite o número decimal: "))),
            "4": lambda: binario_para_decimal(input("Digite o número binário: ")),
            "5": lambda: hexadecimal_para_decimal(input("Digite o número hexadecimal: ")),
            "6": lambda: octal_para_decimal(input("Digite o número octal: ")),
            "7": lambda: print("Saindo do programa...")
        }

        if escolha in switch:
            if escolha == "7":
                switch[escolha]()
                break
            else:
                passos = switch[escolha]()
                for passo in passos:
                    print(passo)
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

main()
