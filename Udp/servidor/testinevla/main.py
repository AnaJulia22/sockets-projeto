def calculadora(operacao):
    lista_operacao = operacao.split(' ')
    print(lista_operacao)

    num1 = int(lista_operacao[0])
    num2 = int(lista_operacao[2])
    sinal = lista_operacao[1]

    if sinal == "+":
        return num1 + num2
    elif sinal == "-":
        return num1 - num2
    elif sinal == "/":
        if num2 == 0:
            return "Divisão por zero não é permitida."
        return num1 / num2
    elif sinal == "*":
        return num1 * num2
    elif sinal == "**":
        return num1 ** num2
    else:
        return "Operação não suportada."


equacoes = ["20 + 10", "10 * 10", "100 - 50", "40 / 2", "5 ** 3"]
for equacao in equacoes:
    resp=calculadora(equacao)
    print(resp)


