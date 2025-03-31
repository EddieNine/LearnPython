p = float(input("Qual é o preço do produto? R$"))
d = p - (p * (5 / 100))
print(f"O produto que custava R${p:.2f}, na promoção de 5% vai custar R${d:.2f}")