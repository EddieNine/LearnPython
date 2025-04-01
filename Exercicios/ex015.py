dias = int(input("Quantos dias alugados? "))
km = int(input("Quantos Km rodados? "))

total = (60 * dias) + (0.15 * km)

print(f"O total a pagar é de R${total:.2f}")