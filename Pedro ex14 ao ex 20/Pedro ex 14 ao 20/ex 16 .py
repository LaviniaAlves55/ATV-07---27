idade = int(input("idade: "))
carteira = input("tem carteira Sim/Não: ")

if idade >= 18 and carteira == "Sim":
    print("Pode dirigir")
else:
    print("Não pode dirigir")