#Iniciação e Engenharia de Dados Primitivos 

from decimal import Decimal

NOME_LOJA = "Perfumaria Bella Aroma"
MARGEM_REPOSICAO = Decimal("0.20")  # Alerta se estoque < 20% do ideal

CATALOGO = [
    {"nome": "Perfume Floral 50ml",    "preco": Decimal("89.90"),  "estoque_atual": 3,  "estoque_ideal": 20},
    {"nome": "Perfume Amadeirado 100ml","preco": Decimal("159.90"), "estoque_atual": 1,  "estoque_ideal": 15},
    {"nome": "Hidratante Corporal",    "preco": Decimal("45.00"),  "estoque_atual": 8,  "estoque_ideal": 30},
    {"nome": "Sabonete Líquido",       "preco": Decimal("22.50"),  "estoque_atual": 12, "estoque_ideal": 50},
    {"nome": "Desodorante Colônia",    "preco": Decimal("55.00"),  "estoque_atual": 2,  "estoque_ideal": 25},
]

print(f"=== {NOME_LOJA} — Relatório de Reposição ===\n")

for item in CATALOGO:
    falta = item["estoque_ideal"] - item["estoque_atual"]
    custo_reposicao = item["preco"] * falta
    print(f"Produto : {item['nome']}")
    print(f"  Estoque atual : {item['estoque_atual']} unidades")
    print(f"  Estoque ideal : {item['estoque_ideal']} unidades")
    print(f"  Repor         : {falta} unidades  (custo estimado: R$ {custo_reposicao:.2f})")
    print()