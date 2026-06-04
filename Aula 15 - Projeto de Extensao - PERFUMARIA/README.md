# Perfumaria Bella Aroma — Sistema de Gestão de Estoque

MVP desenvolvido como projeto de extensão da disciplina **Linguagem de Programação I**, com o objetivo de digitalizar o controle de estoque de uma perfumaria de bairro, substituindo processos manuais por um sistema simples, robusto e persistente.

## Contextualização do problema

A Perfumaria Bella Aroma realizava o controle de estoque de forma manual (caderno/planilha), o que gerava:

- Dificuldade em identificar produtos em falta
- Erros de arredondamento em cálculos de reposição
- Perda de dados ao fechar o sistema

O MVP resolve esses problemas com uma interface de linha de comando (CLI) simples, persistência em arquivo CSV e alertas automáticos de reposição.


## Estrutura do projeto
Projeto de Extensão
 python_logic
   fase1_dados.py       # Modelagem estática e relatório inicial
   fase2_cli.py         # CLI com banco de dados em memória
   fase3_poo.py         # Refatoração orientada a objetos
   fase4_final.py       # MVP completo (use este para rodar)
 README.md

# Pré-requisitos

- Python 3.10 ou superior
- Nenhuma biblioteca externa — apenas módulos da biblioteca padrão (`csv`, `os`, `decimal`)

## Como usar a CLI
Perfumaria Bella Aroma

1. Cadastrar produto
2. Listar produtos
3. Alerta de reposição
4. Atualizar quantidade
5. Salvar estoque
6. Salvar e sair

| Opção | Ação |
|-------|------|
| `1`   | Cadastra um novo produto (nome, preço, quantidade, mínimo desejado) |
| `2`   | Lista todos os produtos com preço e estoque atual |
| `3`   | Exibe apenas os produtos abaixo do estoque mínimo |
| `4`   | Atualiza a quantidade de um produto existente |
| `5`   | Salva o estado atual no arquivo CSV |
| `0`   | Salva e encerra o programa |



## Arquitetura

## Fase 1 — Dados primitivos
Declaração de constantes e tipos precisos com `Decimal` para valores monetários, evitando erros de arredondamento de ponto flutuante.

## Fase 2 — Fluxo e automação
Introdução de lista em memória, menu iterativo com `while` e estruturas de decisão (`if/elif`) para as operações de cadastro, listagem e alerta.

## Fase 3 — Orientação a objetos
Duas classes principais:
- **`Produto`** — encapsula nome, preço, quantidade e mínimo. O setter de `quantidade` rejeita valores negativos com `ValueError`.
- **`GerenciadorEstoque`** — centraliza as operações sobre a coleção de produtos.

## Fase 4 — Resiliência e persistência
- Leitura do CSV ao iniciar (`carregar_csv`) e gravação ao salvar/sair (`salvar_csv`)
- Funções auxiliares `ler_decimal` e `ler_inteiro` com `try/except` em todas as entradas do usuário
- O sistema nunca trava por entrada inválida — exibe aviso e continua

---

## Autores

Desenvolvido por: **Sabrina Pereira de OLiveira, Júlia Barros Freitas e Lívia Mariano Teixeira** 
Curso: Informática para Negócios
3º Semestre - período noturno