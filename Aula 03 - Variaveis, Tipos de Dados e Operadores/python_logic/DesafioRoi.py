ganho = float(input("Digite o ganho: "))
investimento = float(input("Digite o investimento: "))

if investimento == 0:
    print("Erro: investimento não pode ser zero.")
else:
    roi = ((ganho - investimento) / investimento) * 100
    print(f"ROI: {roi:.2f}%")
