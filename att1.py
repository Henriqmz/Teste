"""1. Elabore um programa que:
• Mostre um menu de opções de conversão entre moedas (1 – dólar americano,
2 – euro, 3 – libra esterlina e 4 – yuan;
• Leia a escolha do usuário;
• Leia o custo em R$ (reais) da operação;
• Imprima o valor da transação na moeda escolhida, de acordo com os fatores
de conversão da tabela abaixo.
Moeda           Valor (R$)
Dólar americano 3,258
Euro            4,095
Libra esterlina 4,529
Yuan            0,515"""

print(f"Opções disponíveis:\n1- Dólar americano\n2- Euro\n3- Libra esterlina\n4- Yuan")
escolha=int(input("Digite a sua escolha: "))
valor=float(input("Quanto você deseja converter? "))
if escolha ==1:
    print("Valor da transação:", valor*3.258, "dólares americanos.")
elif escolha ==2:
    print("Valor da transação:", valor*4.095, "euros.")
elif escolha ==3:
    print("Valor da transação:", valor*4.529, "libras esterlinas.")
elif escolha ==4:
    print("Valor da transação:", valor*0.515, "yuans.")
else:

    print("Escolha inválida.")
