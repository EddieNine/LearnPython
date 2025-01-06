d = float(input("Uma distância em metros: "))
km = d / 1000
hm = d / 100
dam = d / 10
dm = d * 10
cm = d * 100
mm = d * 1000
print(f"A medida de {d}m corresponde a"
      f"\n{km}km"
      f"\n{hm}hm"
      f"\n{dam}dam"
      f"\n{dm:.0f}dm"
      f"\n{cm:.0f}cm"
      f"\n{mm:.0f}mm")