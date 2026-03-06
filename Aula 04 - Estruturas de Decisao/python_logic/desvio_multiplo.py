quantidade = int(input("Digite a quantidade em estoque"))

if quantidade < 1:
    print("Status: Em falta.")
elif quantidade < 5: #elif é a forma abreviada de else e if
    print("Status: Alerta de estoque baixo")
else:
    print("Status: Estoque OK.")