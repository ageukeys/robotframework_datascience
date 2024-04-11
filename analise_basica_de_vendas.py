import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
data = pd.read_csv('data.csv')

# Visualizar as primeiras linhas dos dados
print(data.head())

# Resumo estatístico dos dados
print(data.describe())

#Verificar tipos de dados e possiveis valores nulos
print(data.info())


# Insights
# 1. Total de vendas por segmento
total_vendas_por_segmento = data.groupby('Segmento')['Valor_Venda'].sum()
print("\nTotal de Vendas por segmento:")
print(total_vendas_por_segmento)


# 2. Media de vendas por país
media_vendas_por_pais = data.groupby('Pais')['Valor_Venda'].mean()
print("\nMedia de vendas por pais:")
print(media_vendas_por_pais)


# 3. Vendas por categoria e subcategoria
vendas_por_categoria_subcategoria = data.groupby(['Categoria', 'SubCategoria'])['Valor_Venda'].sum()
print("n\Vendas por categoria e subcategoria:")
print(vendas_por_categoria_subcategoria)


