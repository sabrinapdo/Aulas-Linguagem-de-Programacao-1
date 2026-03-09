while True:

    nome_do_produto = input("Digite o nome do produto: ")
    quantidade_em_estoque = int(input("Digite a quantidade em estoque: "))
    preco_unitario = float(input("Digite o preço do produto: "))

    if quantidade_em_estoque >= 0:
        print(f"Nome do produto: {nome_do_produto}, quantidade em estoque: {quantidade_em_estoque}, preço unitário: R$ {preco_unitario:.2f}.")
    else:
        print("ERRO: a quantidade não pode ser um valor negativo. Por favor, tente novamente.")

    print()