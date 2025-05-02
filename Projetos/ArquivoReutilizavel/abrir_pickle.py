import pickle

with open("relatorio.pkl", "rb") as arquivo:
    relatorio_importado = pickle.load(arquivo)

print(relatorio_importado)