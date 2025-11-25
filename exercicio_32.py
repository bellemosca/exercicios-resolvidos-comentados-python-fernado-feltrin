# Crie um programa que exibe em tela a tabuada de um determinado número
# fornecido pelo usuário:

num = int(input("Digite um número: "))

for n in range(1, 11):
    print(f"{num} x {n} = {num * n}")
