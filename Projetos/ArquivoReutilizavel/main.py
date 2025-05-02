import pickle

relatorio = {
    "cliente": "João silva",
    "total": 3570.89,
    "itens": ["Notebook", "Mouse", "Teclado"],
    "pago": True
}

with open("relatorio.pkl", "wb") as arquivo:
    pickle.dump(relatorio, arquivo)