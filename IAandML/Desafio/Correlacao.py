import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


# Dados fictícios: duas listas representando vendas e temperatura
vendas = [120, 150, 180, 220, 250, 300, 350, 400]
temperatura = [22, 24, 26, 28, 30, 32, 34, 36]

# Calculando a correlação
correlacao = np.corrcoef(vendas, temperatura)[0, 1]

# Exibindo os resultados
print(f'Correlação entre vendas e temperatura: {correlacao:.2f}')

# Visualizando os dados
plt.scatter(vendas, temperatura, color='blue')
plt.title('Vendas vs Temperatura')
plt.xlabel('Vendas')
plt.ylabel('Temperatura')
plt.show()
