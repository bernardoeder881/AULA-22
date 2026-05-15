import pandas as pd 
import os

os.system('cls')

df_planilha_custos = pd.read_csv('planilha_de_custos.csv')
print()
print(130 * '=')
print(df_planilha_custos.head(10))

#PREPARANDO OS DADOS
#CRIANDO UMA NOVA COLUNA
#VALOR + VALOR*PORCENTAGEM

df_planilha_custos['Custo Total R$'] = (
    df_planilha_custos['Preco de Compra (R$)'] + 
    (df_planilha_custos['Preco de Compra (R$)'] * df_planilha_custos['Imposto (%)']/100) +
    df_planilha_custos['Frete (R$)'] +
    df_planilha_custos['Taxa Operacional (R$)']
    )
print(130 * '=')
print(df_planilha_custos.head(10))
print()
print(130 * '=')
print(df_planilha_custos[['Produto','Custo Total R$','Imposto (%)']])
    