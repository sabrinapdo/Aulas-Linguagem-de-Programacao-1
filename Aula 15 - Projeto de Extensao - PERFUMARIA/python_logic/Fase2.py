#Estruturas de Fluxo e Automação de Processos
   
from decimal import Decimal, InvalidOperation

estoque = [
    {"nome": "Perfume Floral 50ml",     "preco": Decimal("89.90"),  "quantidade": 3,  "minimo": 5},
    {"nome": "Perfume Amadeirado 100ml","preco": Decimal("159.90"), "quantidade": 1,  "minimo": 3},
    {"nome": "Hidratante Corporal",     "preco": Decimal("45.00"),  "quantidade": 8,  "minimo": 10},
    {"nome": "Sabonete Líquido",        "preco": Decimal("22.50"),  "quantidade": 12, "minimo": 15},
    {"nome": "Desodorante Colônia",     "preco": Decimal("55.00"),  "quantidade": 2,  "minimo": 6},
]

def cadastrar():
    print("\n--- Cadastrar Produto ---")
    nome = input("Nome do produto: ").strip()
    preco = Decimal(input("Preço (ex: 49.90): "))
    quantidade = int(input("Quantidade em estoque: "))
    minimo = int(input("Quantidade mínima desejada: "))
    estoque.append({"nome": nome, "preco": preco, "quantidade": quantidade, "minimo": minimo})
    print(f"✔ '{nome}' cadastrado com sucesso!")

def listar():
    print("\n--- Lista de Produtos ---")
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
    for i, p in enumerate(estoque, 1):
        print(f"{i}. {p['nome']:30} | R$ {p['preco']:>8.2f} | Estoque: {p['quantidade']:>3} | Mínimo: {p['minimo']:>3}")

def alertas():
    print("\n--- ⚠ Produtos Abaixo do Mínimo ---")
    criticos = [p for p in estoque if p["quantidade"] < p["minimo"]]
    if not criticos:
        print("✔ Todos os produtos estão com estoque adequado.")
    for p in criticos:
        falta = p["minimo"] - p["quantidade"]
        print(f"  !! {p['nome']} — faltam {falta} unidades para atingir o mínimo")

def menu():
    opcoes = {"1": cadastrar, "2": listar, "3": alertas}
    while True:
        print("\n========= Perfumaria Bella Aroma =========")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Alerta de reposição")
        print("0. Sair")
        opcao = input("Escolha: ").strip()
        if opcao == "0":
            print("Encerrando. Até logo!")
            break
        elif opcao in opcoes:
            opcoes[opcao]()
        else:
            print("Opção inválida.")

menu()