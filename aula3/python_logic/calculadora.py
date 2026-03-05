"""" O fluxo do programa seguirá estes passos lógicos:
Entrada: solicitar ao usuário o primeiro número.
Entrada: solicitar ao usuário o segundo número.
Processamento: realizar os cálculos de Adição, Subtração, Multiplicação e Divisão
utilizando operadores aritméticos.
Saída: exibir os resultados formatados para o suário. """

# Passo 1: entrada de dados
# Utilizamos float() para permitir cálculos com casas decimais
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Passo 2: processamento (cálculos aritméticos)
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

# Passo 3: saída de resultados formatados
print(f"Soma (A + B): {soma}")
print(f"Subtracao (A - B): {subtracao}")
print(f"Multiplicacao (A * B): {multiplicacao}")
print(f"Divisao (A / B): {divisao}")
