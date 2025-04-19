import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

dados = {
    'nota_prova1': [7, 4, 6, 9, 3, 8, 5, 2],
    'nota_prova2': [8, 5, 5, 10, 2, 9, 6, 3],
    'frequencia': [90, 60, 75, 95, 50, 85, 70, 40],
    'aprovado': [1, 0, 1, 1, 0, 1, 1, 0]  # 1 = Aprovado, 0 = Reprovado
}

df = pd.DataFrame(dados)
print(df)

# Separar os dados em entradas (X) e saída (y)
X = df[['nota_prova1', 'nota_prova2', 'frequencia']]
y = df['aprovado']

# Dividir em treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=42)

# Criar e treinar o modelo
modelo = DecisionTreeClassifier()
modelo.fit(X_treino, y_treino)

# Fazer previsões
y_pred = modelo.predict(X_teste)

# Ver a precisão
print("Acurácia:", accuracy_score(y_teste, y_pred))

# Exemplo: nota1 = 6, nota2 = 7, frequência = 80%
previsao = modelo.predict([[6, 7, 80]])
print("Vai ser aprovado?", "Sim" if previsao[0] == 1 else "Não")

# Plotar a árvore de decisão
plt.figure(figsize=(10, 8))
plot_tree(modelo, filled=True, feature_names=['nota_prova1', 'nota_prova2', 'frequencia'],
          class_names=['Reprovado', 'Aprovado'], rounded=True, fontsize=12)
plt.show()

# Salvar o gráfico como imagem
plt.savefig('arvore_decisao.png')

# Opcionalmente, abra a imagem com uma ferramenta externa (como o visualizador de imagens)
import os
os.system('start arvore_decisao.png')  # No Windows, isso vai abrir a imagem.

