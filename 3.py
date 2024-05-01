def binario_para_decimal(numero_binario):
    decimal = 0
    potencia = len(numero_binario) - 1
    
    for digito in numero_binario:
        if digito == '1':
            decimal += 2 ** potencia
        potencia -= 1
    
    return decimal

def binario_para_decimal_com_explicacao(numero_binario):
    decimal = 0
    potencia = len(numero_binario) - 1
    explicacao = ""
    
    for i, digito in enumerate(numero_binario):
        if digito == '1':
            valor = 2 ** potencia
            decimal += valor
            if explicacao:
                explicacao += " + "
            explicacao += f"({digito} × 2^{potencia})"
        potencia -= 1
    
    explicacao += f" = {decimal}"
    return decimal, explicacao

def decimal_para_binario_com_explicacao(decimal):
    numero_binario = ""
    resto_explicacao = ""
    explicacao = ""
    
    # Converte o número decimal para binário
    while decimal > 0:
        resto = decimal % 2
        # Adiciona o resto à esquerda do número binário
        numero_binario = str(resto) + numero_binario
        # Constrói a explicação passo a passo
        if explicacao:
            explicacao += " + "
        explicacao += f"({decimal} ÷ 2 = {decimal // 2}, resto {resto})"
        # Divide o decimal pelo número base (2) para encontrar o próximo dígito binário
        decimal //= 2
    
    # Finaliza a explicação com o número binário completo
    explicacao += f" = {numero_binario}"
    
    return numero_binario, explicacao

def decimal_para_hexadecimal_com_explicacao(decimal):
    numero_hexadecimal = ""
    explicacao = ""
    
    while decimal > 0:
        resto = decimal % 16
        if resto < 10:
            numero_hexadecimal = str(resto) + numero_hexadecimal
        else:
            numero_hexadecimal = chr(65 + resto - 10) + numero_hexadecimal
        if explicacao:
            explicacao += " + "
        explicacao += f"({decimal} ÷ 16 = {decimal // 16}, resto {resto})"
        decimal //= 16
    
    explicacao += f" = {numero_hexadecimal}"
    
    return numero_hexadecimal, explicacao

def hexadecimal_para_decimal_com_explicacao(numero_hexadecimal):
    decimal = 0
    explicacao = ""
    
    for i, digito in enumerate(numero_hexadecimal):
        if digito.isdigit():
            valor = int(digito) * (16 ** (len(numero_hexadecimal) - 1 - i))
        else:
            valor = (ord(digito) - 55) * (16 ** (len(numero_hexadecimal) - 1 - i))
        decimal += valor
        if explicacao:
            explicacao += " + "
        explicacao += f"({digito} × 16^{len(numero_hexadecimal) - 1 - i})"
    
    explicacao += f" = {decimal}"
    
    return decimal, explicacao

def binario_para_hexadecimal_com_explicacao(numero_binario):
    # Dividindo os dígitos binários de 4 em 4, da direita para a esquerda
    grupos = [numero_binario[max(i - 4, 0):i] for i in range(len(numero_binario), 0, -4)]
    
    # Convertendo cada grupo de binário para decimal e mapeando para hexadecimal
    hex_digitos = [hex(int(grupo, 2))[2:].upper() for grupo in grupos]
    
    # Unindo os dígitos hexadecimais
    numero_hexadecimal = ''.join(hex_digitos)
    
    # Construindo a explicação passo a passo
    explicacao = ""
    for grupo, hexa in zip(grupos, hex_digitos):
        decimal = int(grupo, 2)
        if explicacao:
            explicacao += " + "
        explicacao += f"({grupo} → {decimal} → {hexa})"
    
    return numero_hexadecimal, explicacao

def hexadecimal_para_binario_com_explicacao(numero_hexadecimal):
    # Convertendo cada dígito hexadecimal para binário separadamente
    binario_dos_digitos = [bin(int(digito, 16))[2:].zfill(4) for digito in numero_hexadecimal]
    
    # Unindo os dígitos binários
    numero_binario = ''.join(binario_dos_digitos)
    
    # Construindo a explicação passo a passo
    explicacao = ""
    for digito, binario in zip(numero_hexadecimal, binario_dos_digitos):
        if explicacao:
            explicacao += " + "
        explicacao += f"({digito} → {binario})"
    
    return numero_binario, explicacao

def octal_para_decimal(numero_octal):
    decimal = 0
    potencia = len(numero_octal) - 1
    
    for digito in numero_octal:
        decimal += int(digito) * (8 ** potencia)
        potencia -= 1
    
    return decimal

def octal_para_decimal_com_explicacao(numero_octal):
    decimal = 0
    potencia = len(numero_octal) - 1
    explicacao = ""
    
    for i, digito in enumerate(numero_octal):
        valor = int(digito) * (8 ** potencia)
        decimal += valor
        if explicacao:
            explicacao += " + "
        explicacao += f"({digito} × 8^{potencia})"
        potencia -= 1
    
    explicacao += f" = {decimal}"
    return decimal, explicacao

def decimal_para_octal_com_explicacao(decimal):
    numero_octal = ""
    explicacao = ""
    
    while decimal > 0:
        resto = decimal % 8
        numero_octal = str(resto) + numero_octal
        if explicacao:
            explicacao = f"{decimal} ÷ 8 = {decimal // 8}, resto {resto} + " + explicacao
        else:
            explicacao = f"{decimal} ÷ 8 = {decimal // 8}, resto {resto}"
        decimal //= 8
    
    explicacao += f" = {numero_octal}"
    
    return numero_octal, explicacao

def octal_para_binario_com_explicacao(numero_octal):
    # Convertendo cada dígito do número octal para binário separadamente
    binario_dos_digitos = [bin(int(digito))[2:].zfill(3) for digito in numero_octal]
    
    # Unindo os dígitos binários e removendo os zeros à esquerda
    numero_binario = ''.join(binario_dos_digitos).lstrip('0')
    
    # Montando a explicação passo a passo
    explicacao = ""
    for i, digito in enumerate(numero_octal):
        binario = binario_dos_digitos[i]
        if explicacao:
            explicacao += " + "
        explicacao += f"({digito} → {binario})"
    
    return numero_binario, explicacao

def octal_para_hexadecimal_com_explicacao(numero_octal):
    decimal = octal_para_decimal(numero_octal)
    hexadecimal, explicacao = decimal_para_hexadecimal_com_explicacao(decimal)
    return hexadecimal, explicacao

def main():
    while True:
        print("\nMenu:")
        print("1. Converter número binário para decimal")
        print("2. Converter número decimal para binário")
        print("3. Converter número decimal para hexadecimal")
        print("4. Converter número hexadecimal para decimal")
        print("5. Converter número binário para hexadecimal")
        print("6. Converter número hexadecimal para binário")
        print("7. Converter número octal para decimal")
        print("8. Converter número decimal para octal")
        print("9. Converter número octal para binário")
        print("10. Converter número octal para hexadecimal")
        print("11. Sair do programa")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            numero_binario = input("Digite o número binário: ")
            decimal, explicacao = binario_para_decimal_com_explicacao(numero_binario)
            print("O número binário", numero_binario, "equivale a", decimal, "em decimal.")
            print("Explicação do cálculo:", explicacao)
        elif escolha == '2':
            numero_decimal = int(input("Digite o número decimal: "))
            numero_binario, explicacao = decimal_para_binario_com_explicacao(numero_decimal)
            print("O número decimal", numero_decimal, "equivale a", numero_binario, "em binário.")
            print("Explicação do cálculo:", explicacao)
        elif escolha == '3':
            numero_decimal = int(input("Digite o número decimal: "))
            numero_hexadecimal, explicacao = decimal_para_hexadecimal_com_explicacao(numero_decimal)
            print("O número decimal", numero_decimal, "equivale a", numero_hexadecimal, "em hexadecimal.")
            print("Explicação do cálculo:", explicacao)
        elif escolha == '4':
            numero_hexadecimal = input("Digite o número hexadecimal: ")
            decimal, explicacao = hexadecimal_para_decimal_com_explicacao(numero_hexadecimal)
            print("O número hexadecimal", numero_hexadecimal, "equivale a", decimal, "em decimal.")
            print("Explicação do cálculo:", explicacao)
        elif escolha == '5':
            numero_binario = input("Digite o número binário: ")
            numero_hexadecimal, explicacao = binario_para_hexadecimal_com_explicacao(numero_binario)
            print("O número binário", numero_binario, "equivale a", numero_hexadecimal, "em hexadecimal.")
            print("Explicação do cálculo:", explicacao)
        elif escolha == '6':
            numero_hexadecimal = input("Digite o número hexadecimal: ")
            numero_binario, explicacao = hexadecimal_para_binario_com_explicacao(numero_hexadecimal)
            print("O número hexadecimal", numero_hexadecimal, "equivale a", numero_binario, "em binário.")
            print("Explicação do cálculo:", explicacao)
        elif escolha == '7':
            numero_octal = input("Digite o número octal: ")
            decimal, explicacao = octal_para_decimal_com_explicacao(numero_octal)
            print("O número octal", numero_octal, "equivale a", decimal, "em decimal.")
            print("Explicação do cálculo:", explicacao)
        elif escolha == '8':
            numero_decimal = int(input("Digite o número decimal: "))
            numero_octal, explicacao = decimal_para_octal_com_explicacao(numero_decimal)
            print("O número decimal", numero_decimal, "equivale a", numero_octal, "em octal.")
            print("Explicação do cálculo:", explicacao)
        elif escolha == '9':
            numero_octal = input("Digite o número octal: ")
            numero_binario, explicacao = octal_para_binario_com_explicacao(numero_octal)
            print("O número octal", numero_octal, "equivale a", numero_binario, "em binário.")
            print("Explicação do cálculo:", explicacao)
        elif escolha == '10':
            numero_octal = input("Digite o número octal: ")
            numero_hexadecimal, explicacao = octal_para_hexadecimal_com_explicacao(numero_octal)
            print("O número octal", numero_octal, "equivale a", numero_hexadecimal, "em hexadecimal.")
            print("Explicação do cálculo:", explicacao)
        elif escolha == '11':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
