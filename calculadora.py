print("CALCULADORA - OPERAÇÕES BÁSICAS ENTRE DOIS NÚMEROS")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f'\nADIÇÃO: {num1} + {num2} = {num1+num2}\n')
print(f'SUBTRAÇÃO: {num1} - {num2} = {num1-num2}\n')
print(f'MULTIPLICAÇÃO: {num1} x {num2} = {num1*num2}\n')
if (num2 == 0):
    print(f'DIVISÃO: {num1} / {num2} = ERRO: Não existe divisão por zero\n')
else:
    print(f'DIVISÃO: {num1} / {num2} = {num1/num2}\n')