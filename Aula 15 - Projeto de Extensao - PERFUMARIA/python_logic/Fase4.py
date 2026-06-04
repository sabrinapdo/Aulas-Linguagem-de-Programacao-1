#Resiliência, Persistência de Dados e Entrega Final

import csv
import os
from decimal import Decimal, InvalidOperation

ARQUIVO_CSV = "estoque_perfumaria.csv"
CABECALHO   = ["nome", "preco", "quantidade", "minimo"]


# Modelo 

class Produto:
    def __init__(self, nome: str, preco: Decimal, quantidade: int, minimo: int):
        self._nome     = nome
        self._preco    = preco
        self._quantidade = quantidade
        self._minimo   = minimo

    @property
    def nome(self):       return self._nome
    @property
    def preco(self):      return self._preco
    @property
    def quantidade(self): return self._quantidade
    @property
    def minimo(self):     return self._minimo

    @quantidade.setter
    def quantidade(self, valor):
        if valor < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        self._quantidade = valor

    def precisa_repor(self):
        return self._quantidade < self._minimo

    def quanto_repor(self):
        return max(0, self._minimo - self._quantidade)

    def para_dict(self):
        return {"nome": self._nome, "preco": str(self._preco),
                "quantidade": self._quantidade, "minimo": self._minimo}

    def __str__(self):
        return (f"{self._nome:30} | R$ {self._preco:>8.2f} "
                f"| Estoque: {self._quantidade:>3} | Mínimo: {self._minimo:>3}")


# Persistência 

def carregar_csv() -> list[Produto]:
    produtos = []
    if not os.path.exists(ARQUIVO_CSV):
        return produtos
    with open(ARQUIVO_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                produtos.append(Produto(
                    row["nome"],
                    Decimal(row["preco"]),
                    int(row["quantidade"]),
                    int(row["minimo"]),
                ))
            except (KeyError, InvalidOperation, ValueError):
                print(f"  ⚠ Linha inválida ignorada no CSV: {row}")
    print(f"✔ {len(produtos)} produto(s) carregado(s) de '{ARQUIVO_CSV}'.")
    return produtos

def salvar_csv(produtos: list[Produto]):
    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CABECALHO)
        writer.writeheader()
        writer.writerows([p.para_dict() for p in produtos])
    print(f"✔ Estoque salvo em '{ARQUIVO_CSV}'.")


# Helpers de entrada segura 

def ler_decimal(prompt: str) -> Decimal:
    while True:
        try:
            return Decimal(input(prompt).strip().replace(",", "."))
        except InvalidOperation:
            print("  ⚠ Valor inválido. Use números (ex: 49.90).")

def ler_inteiro(prompt: str, minimo: int = 0) -> int:
    while True:
        try:
            valor = int(input(prompt).strip())
            if valor < minimo:
                raise ValueError
            return valor
        except ValueError:
            print(f"  ⚠ Insira um número inteiro >= {minimo}.")


# Gerenciador
class GerenciadorEstoque:
    def __init__(self, produtos: list[Produto]):
        self._produtos = produtos

    def adicionar(self):
        print("\n--- Cadastrar Produto ---")
        nome   = input("Nome: ").strip()
        preco  = ler_decimal("Preço: R$ ")
        qtd    = ler_inteiro("Quantidade em estoque: ")
        minimo = ler_inteiro("Quantidade mínima desejada: ", minimo=1)
        self._produtos.append(Produto(nome, preco, qtd, minimo))
        print(f"✔ '{nome}' cadastrado!")

    def listar(self):
        print("\n--- Lista de Produtos ---")
        if not self._produtos:
            print("Nenhum produto cadastrado.")
            return
        for i, p in enumerate(self._produtos, 1):
            print(f"{i:>2}. {p}")

    def alertas(self):
        print("\n--- ⚠ Produtos que precisam de reposição ---")
        criticos = [p for p in self._produtos if p.precisa_repor()]
        if not criticos:
            print("✔ Estoque em dia!")
            return
        for p in criticos:
            print(f"  !! {p.nome} — repor {p.quanto_repor()} unidades")

    def atualizar(self):
        self.listar()
        if not self._produtos:
            return
        idx = ler_inteiro("Número do produto a atualizar: ", minimo=1) - 1
        if idx >= len(self._produtos):
            print("  ⚠ Número fora da lista.")
            return
        nova = ler_inteiro("Nova quantidade: ")
        try:
            self._produtos[idx].quantidade = nova
            print(f"✔ Atualizado!")
        except ValueError as e:
            print(f"  ⚠ {e}")

    def salvar(self):
        salvar_csv(self._produtos)

    def menu(self):
        acoes = {"1": self.adicionar, "2": self.listar,
                 "3": self.alertas,   "4": self.atualizar, "5": self.salvar}
        while True:
            print("\n========= Perfumaria Bella Aroma =========")
            print("1. Cadastrar produto")
            print("2. Listar produtos")
            print("3. Alerta de reposição")
            print("4. Atualizar quantidade")
            print("5. Salvar estoque")
            print("0. Salvar e sair")
            opcao = input("Escolha: ").strip()
            if opcao == "0":
                self.salvar()
                print("Até logo!")
                break
            elif opcao in acoes:
                acoes[opcao]()
            else:
                print("  ⚠ Opção inválida.")


# Ponto de entrada

produtos = carregar_csv()

# Dados padrão se CSV ainda não existir
if not produtos:
    for d in [
        ("Perfume Floral 50ml",      Decimal("89.90"),  3,  5),
        ("Perfume Amadeirado 100ml", Decimal("159.90"), 1,  3),
        ("Hidratante Corporal",      Decimal("45.00"),  8, 10),
        ("Sabonete Líquido",         Decimal("22.50"), 12, 15),
        ("Desodorante Colônia",      Decimal("55.00"),  2,  6),
    ]:
        produtos.append(Produto(*d))

GerenciadorEstoque(produtos).menu()