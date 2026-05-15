
import pandas as pd 

df_eletronicos =pd.read_excel('vendas_eletronicos.xlsx')
print(df_eletronicos.head(10))


print('\n Maior valor do faturamento')
print(45 * '=')
print(df_eletronicos['Faturamento Total (R$)'].max())
print(45 * '=')

# Estudar
print('\nImprimir todas as colunas através do id do item de maior valor da coluna Faturamrnto total')
print(df_eletronicos.loc[df_eletronicos['Faturamento Total (R$)'].idxmax()])
print(45 * '=')
print('\nImprimir da coluna produto através do id do item de maior valor da coluna Faturamrnto total')
print(df_eletronicos.loc[df_eletronicos['Faturamento Total (R$)'].idxmax(),'Produto'])
print(45 * '=')


print('\n Menor valor do faturamento')
print(45 * '=')
print(df_eletronicos['Faturamento Total (R$)'].min())
print(45 * '=')

print('\n Total de unidades vendidas')
print(45 * '=')
print(df_eletronicos['Unidades Vendidas'].sum())
print(45 * '=')

print('\n Preço médio dos produtos')
print(45 * '=')
print(df_eletronicos['Preço por Unidade (R$)'].mean())
print(45 * '=')

print('\n Produtos acima da média')
print(45 * '=')
media = df_eletronicos['Faturamento Total (R$)'].mean()
print(45 * '=')
print (media)
print(45 * '=')
print(df_eletronicos[df_eletronicos['Faturamento Total (R$)'] >= media]) # imprime todos os valores maiores do que a média do Faturamento Total
print(45 * '=')

print(df_eletronicos.loc[df_eletronicos['Faturamento Total (R$)'].idxmin()])
print(df_eletronicos.loc[df_eletronicos['Faturamento Total (R$)'].idxmax(),'Produto'])
