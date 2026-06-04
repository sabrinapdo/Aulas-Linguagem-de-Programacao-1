# Paradigma Orientado a Objetos (POO) e Abstração

# fase3_poo.py
# Fase 3 - POO para a Perfumaria Bella Aroma
from decimal import Decimal


class Produto:
    def __init__(self, nome: str, preco: Decimal, quantidade: int, minimo: int):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade
        self._minimo = minimo

    # Getters
    @property
    def nome(self):       return self._nome
    @property
    def preco(self):      return self._preco
    @property
    def quantidade(self): return self._quantidade
    @property
    def minimo(self):     return self._minimo

    # Setter com validação
    @quantidade.setter
    def quantidade(self, valor):
        if valor < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        self._quantidade = valor

    def precisa_repor(self):
        return self._quantidade < self._minimo

    def quanto_repor(self):
        return max(0, self._minimo - self._quantidade)

    def __str__(self):
        return (f"{self._nome:30} | R$ {self._preco:>8.2f} "
                f"| Estoque: {self._quantidade:>3} | Mínimo: {self._minimo:>3}")


class GerenciadorEstoque:
    def __init__(self):
        self._produtos: list[Produto] = []

    def adicionar(self, produto: Produto):
        self._produtos.append(produto)
        print(f"✔ '{produto.nome}' adicionado ao estoque.")

    def listar(self):
        if not self._produtos:
            print("Nenhum produto cadastrado.")
            return
        print("\n--- Lista de Produtos ---")
        for i, p in enumerate(self._produtos, 1):
            print(f"{i}. {p}")

    def alertas_reposicao(self):
        print("\n--- ⚠ Produtos que precisam de reposição ---")
        criticos = [p for p in self._produtos if p.precisa_repor()]
        if not criticos:
            print("✔ Estoque em dia!")
            return
        for p in criticos:
            print(f"  !! {p.nome} — repor {p.quanto_repor()} unidades")

    def atualizar_quantidade(self, nome: str, nova_qtd: int):
        for p in self._produtos:
            if p.nome.lower() == nome.lower():
                p.quantidade = nova_qtd  # dispara o setter com validação
                print(f"✔ Quantidade de '{p.nome}' atualizada para {nova_qtd}.")
                return
        print(f"Produto '{nome}' não encontrado.")

    def menu(self):
        while True:
            print("\n========= Perfumaria Bella Aroma =========")
            print("1. Cadastrar produto")
            print("2. Listar produtos")
            print("3. Alerta de reposição")
            print("4. Atualizar quantidade")
            print("0. Sair")
            opcao = input("Escolha: ").strip()

            if opcao == "0":
                print("Encerrando. Até logo!")
                break
            elif opcao == "1":
                nome     = input("Nome: ").strip()
                preco    = Decimal(input("Preço: "))
                qtd      = int(input("Quantidade: "))
                minimo   = int(input("Mínimo desejado: "))
                self.adicionar(Produto(nome, preco, qtd, minimo))
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.alertas_reposicao()
            elif opcao == "4":
                nome  = input("Nome do produto: ").strip()
                nova  = int(input("Nova quantidade: "))
                self.atualizar_quantidade(nome, nova)
            else:
                print("Opção inválida.")


# --- Dados iniciais ---
gerenciador = GerenciadorEstoque()
for dados in [
    ("Perfume Floral 50ml",      Decimal("89.90"),  3,  5),
    ("Perfume Amadeirado 100ml", Decimal("159.90"), 1,  3),
    ("Hidratante Corporal",      Decimal("45.00"),  8, 10),
    ("Sabonete Líquido",         Decimal("22.50"), 12, 15),
    ("Desodorante Colônia",      Decimal("55.00"),  2,  6),
]:
    gerenciador.adicionar(Produto(*dados))

gerenciador.menu()