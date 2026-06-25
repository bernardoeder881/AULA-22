# python -m venv venv
# source ./venv/Scripts/activate
# pip install pandas numpy matplotlib
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 


# obtendo os dados
try:
    print('Obtendo os dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # iso-8859-1  | utf-8  | latin1 | cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
  
    # delimitando as variáveis
    df_recuperacao_veiculos = df_ocorrencias[['cisp', 'recuperacao_veiculos']]

    # agrupando e quantificando as variáveis quantitativa
    df_recuperacao_veiculos = df_recuperacao_veiculos.groupby('cisp', as_index=False)['recuperacao_veiculos'].sum()

    # ordenando em decrescente:
    df_recuperacao_veiculos = df_recuperacao_veiculos.sort_values(by='recuperacao_veiculos', ascending=False)
    
    print(df_recuperacao_veiculos)

except Exception as e:
    print(f'Erro ao obter os dados: {e}')
    exit()


# Obtendo informações
try:
    print('Obtendo informações a cerca dos recuperação de veículos... ')
    array_recuperacao_veiculos = np.array(df_recuperacao_veiculos['recuperacao_veiculos'])

    media_recuperacao_veiculos = np.mean(array_recuperacao_veiculos)
    mediana_recuperacao_veiculos = np.median(array_recuperacao_veiculos)
    distancia = abs((media_recuperacao_veiculos - mediana_recuperacao_veiculos) / mediana_recuperacao_veiculos * 100)
    variancia = np.var(array_recuperacao_veiculos)
    distancia_var_media = variancia /( media_recuperacao_veiculos ** 2)*100
    desvio_padrao= np.std(array_recuperacao_veiculos)
    coef_variacao = desvio_padrao / media_recuperacao_veiculos

    print('\nMedidas de tendência Central')
    print(40*'=')
    print(f'Média: {media_recuperacao_veiculos}')
    print(f'Mediana: {mediana_recuperacao_veiculos}')
    print(f'Distância ente média e mediana: {distancia}%')


    # Obtendo os quartis
    q1 = np.quantile(array_recuperacao_veiculos, 0.25)
    q2 = np.quantile(array_recuperacao_veiculos, 0.50)
    q3 = np.quantile(array_recuperacao_veiculos, 0.75)

    print('\nMedidas de Posição')
    print(40*'=')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')


    # menores
    df_recuperacao_veiculos_menores = df_recuperacao_veiculos[df_recuperacao_veiculos['recuperacao_veiculos'] < q1]

    # maiores
    df_recuperacao_veiculos_maiores = df_recuperacao_veiculos[df_recuperacao_veiculos['recuperacao_veiculos'] > q3]
    
    print('\nCisps com Mais Recuperações')
    print(40*'=')
    print(df_recuperacao_veiculos_maiores)

    print('\nCispscom Menos Recuperações')
    print(40*'=')
    print(df_recuperacao_veiculos_menores.sort_values(by='recuperacao_veiculos', ascending=True))# ordem crescente

except Exception as e:
    print(f'Erro ao calcular as informações...')


# Medidas de Dispersão - Amplitude Total
try:
    maximo = np.max(array_recuperacao_veiculos)
    minimo = np.min(array_recuperacao_veiculos)
    amplitude = maximo - minimo

    print('\nMedidas de Dispersão')
    print(40*'=')
    print(f'Máximo: {maximo}')
    print(f'Mínimo: {minimo}')
    print(f'Amplitude Total: {amplitude}')

except Exception as e:
    print(f'Erro ao calcular medida de dispersão {e}')


# Outliers
try:

    iqr = q3 - q1  # 969.5

    # print(f'\nIQR: {iqr}')

    # limite inferior
    limite_inferior = q1 - (1.5 * iqr)

    # limite superior
    limite_superior = q3 + (1.5 * iqr)


    # outliers
    df_recuperacao_veiculos_outliers_superiores = df_recuperacao_veiculos[df_recuperacao_veiculos['recuperacao_veiculos'] > limite_superior]
        
    df_recuperacao_veiculos_outliers_inferiores = df_recuperacao_veiculos[df_recuperacao_veiculos['recuperacao_veiculos'] < limite_inferior]

    print('\nMedidas:')
    print(40*'=')
    print(f'Mínimo: {minimo}')
    print(f'Limite Inferior: {limite_inferior}')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')  # mediana
    print(f'Q3: {q3}')
    print(f'IQR: {iqr}')
    print(f'Limite Superior: {limite_superior}')
    print(f'Máximo: {maximo}')


    print('\nOutliers Superiores:')
    print(40*'=')
    if len(df_recuperacao_veiculos_outliers_superiores) == 0:
        print('Não existe outliers superiores')
    else:
        print(df_recuperacao_veiculos_outliers_superiores)


    print('\nOutliers Inferiores:')
    print(40*'=')
    if len(df_recuperacao_veiculos_outliers_inferiores) == 0:
        print('Não existe outliers inferiores')
    else:
        print(df_recuperacao_veiculos_outliers_inferiores)

except Exception as e:
    print(f'Erro ao calcular Outliers {e}')



# Visualizando os dados
try:
    # mostrando cisp com maiores recuperações
   
    plt.figure(figsize=(16, 8))

   
   
    # 1 Maiores
    plt.subplot(3, 3, 1)

    # 1. Ordena do maior para o menor e pega os 10 primeiros
    df_recuperacao_veiculos_maiores = (
        df_recuperacao_veiculos_maiores.sort_values(by='recuperacao_veiculos', ascending=False)
        .head(10)
    )

    # 2. SOLUÇÃO: Converte a coluna CISP para texto para o Matplotlib tratar como categorias
    df_recuperacao_veiculos_maiores['cisp'] = df_recuperacao_veiculos_maiores['cisp'].astype(str)

    # 3. Inverte a ordem das linhas para a maior barra ir para o topo
    df_plot = df_recuperacao_veiculos_maiores.iloc[::-1]

    # 4. Plota as barras juntas e ordenadas
    plt.barh(df_plot['cisp'], df_plot['recuperacao_veiculos'])

    # 5. Rótulo de dados (números) posicionados corretamente ao lado de cada barra
    deslocamento = max(df_plot['recuperacao_veiculos']) * 0.01
    for i, valor in enumerate(df_plot['recuperacao_veiculos']):
        plt.text(
            valor + deslocamento,  # posição x
            i,                    # posição y (índice sequencial de 0 a 9)
            f'{valor:,}',
            ha="left",
            va="center",
            fontsize='8'
        )

    plt.title('CISPS com maiores recuperações')

#================================================================================================================================================
    # POSIÇÃO 2 - OUTLIERS SUPERIORES
    plt.subplot(3, 3, 2) 

    # 1. Ordena do maior para o menor (garante a ordem correta caso venham desordenados)
    df_outliers = df_recuperacao_veiculos_outliers_superiores.sort_values(by='recuperacao_veiculos', ascending=False)

    # 2. SOLUÇÃO: Converte a coluna CISP para texto para juntar as barras
    df_outliers['cisp'] = df_outliers['cisp'].astype(str)

    # 3. Inverte a ordem das linhas para a maior barra ir para o topo
    df_plot_outliers = df_outliers.iloc[::-1]

    # 4. Plota as barras juntas e ordenadas
    plt.barh(df_plot_outliers['cisp'], df_plot_outliers['recuperacao_veiculos'])

    # 5. Adiciona os rótulos de dados na frente das barras
    deslocamento_outliers = max(df_plot_outliers['recuperacao_veiculos']) * 0.01
    for i, valor in enumerate(df_plot_outliers['recuperacao_veiculos']):
        plt.text(
            valor + deslocamento_outliers,  # posição x
            i,                             # posição y (índice sequencial)
            f'{valor:,}',
            ha="left",
            va="center",
            fontsize='8'
        )

    plt.title('Outliers Superiores')

#==============================================================================================================================================
    plt.subplot(3, 3, 3)

    
    # showfliers=False - retira outliers
    plt.boxplot(array_recuperacao_veiculos, vert=False, showmeans=True)
    plt.title('Boxplot dos Recuperacoses por cisp')

     
        # POSIÇÃO 4 - DUAS COLUNAS (10 MAIORES E 10 MENORES)
       # POSIÇÃO 4 - DUAS COLUNAS (10 MAIORES E 10 MENORES)
       # POSIÇÃO 4 - DUAS COLUNAS (10 MAIORES E 10 MENORES)
    plt.subplot(3, 3, 4) 
    plt.axis('off') 
    
    # 1. Prepara e ordena os dados de cada DataFrame correspondente
    top_10_maiores = df_recuperacao_veiculos_maiores.sort_values(by='recuperacao_veiculos', ascending=False).head(10)
    top_10_menores = df_recuperacao_veiculos_menores.sort_values(by='recuperacao_veiculos', ascending=True).head(10)
    
    # Configurações de layout do texto
    y_inicial = 0.85
    espacamento_y = 0.07
    
    # --- COLUNA 1: 10 MAIORES (Eixo X em 0.05) ---
    plt.text(0.05, 0.95, "10 MAIORES RECOUP.", fontsize=10, fontweight='bold', color='navy')
    
    for idx, (_, row) in enumerate(top_10_maiores.iterrows()):
        y_pos = y_inicial - (idx * espacamento_y)
        cisp = row['cisp']
        valor = row['recuperacao_veiculos']
        plt.text(0.05, y_pos, f"{idx+1}º - CISP {cisp}: {valor:,}", fontsize=9)
        
    # --- COLUNA 2: 10 MENORES (Eixo X em 0.55) ---
    plt.text(0.55, 0.95, "10 MENORES RECOUP.", fontsize=10, fontweight='bold', color='darkred')
    
    for idx, (_, row) in enumerate(top_10_menores.iterrows()):
        y_pos = y_inicial - (idx * espacamento_y)
        cisp = row['cisp']
        valor = row['recuperacao_veiculos']
        plt.text(0.55, y_pos, f"{idx+1}º - CISP {cisp}: {valor:,}", fontsize=9)
    
    plt.title('Delegacias com Maiores e Menores Recuperações')

    plt.tight_layout()  # Ajustar o Layout
    
#========================================================================================================================
    plt.subplot(3, 3, 5) 
    plt.axis('off') 
    
    assimetria = df_recuperacao_veiculos['recuperacao_veiculos'].skew()
    curtose = df_recuperacao_veiculos['recuperacao_veiculos'].kurtosis()

    print('\nMedidas de Distribuição')
    print(40*'=')
    print(f'Assimetria: {assimetria}')
    print(f'Curtose: {curtose}')

   # 1. Plotagem do Histograma (com bordas sutis e labels para a legenda)
    plt.hist(array_recuperacao_veiculos, bins=50, color='#1f77b4', edgecolor='white', alpha=0.8)
    
    # 2. Linhas de Média e Mediana (mais visíveis e com identificação)
    plt.axvline(media_recuperacao_veiculos, color='green', linewidth=2, linestyle='-', label=f'Média: {media_recuperacao_veiculos:.1f}')
    plt.axvline(mediana_recuperacao_veiculos, color='orange', linewidth=2, linestyle='-', label=f'Mediana: {mediana_recuperacao_veiculos:.1f}')

    # 3. Rótulos e Títulos (Essencial para conseguir ler o gráfico!)
    plt.title('Distribuição de Recuperação de Veículos', fontsize=12, fontweight='bold')
    plt.xlabel('Veículos Recuperados', fontsize=10)
    plt.ylabel('Quantidade de Municípios', fontsize=10)
    plt.legend(loc='upper right') # Mostra a legenda com os valores da média/mediana
    plt.grid(axis='y', linestyle='--', alpha=0.5) # Grade sutil ao fundo

    # 4. Cálculo das faixas para o Console
    # CORREÇÃO: Mudado bins=1 para bins=10 (ou outro número) para o print fazer sentido
    contagens, limites = np.histogram(array_recuperacao_veiculos, bins=10)

    print('\nFaixas do Histograma')
    print(50*'-')
    for i in range(len(contagens)):
        if contagens[i] > 0:
            print(
                f'Faixa {i+1:2d}: '
                f'{limites[i]:6.0f} até {limites[i+1]:6.0f} veículos recuperados: '
                f'=> {contagens[i]:4d} municípios'
            )
    print(50*'-')

    plt.tight_layout() # Ajusta o espaçamento para não cortar nenhum rótulo
    

#============================================================================================================================
    plt.subplot(3, 3, 6) 
    plt.text(0.1, 0.9, f'Média: {media_recuperacao_veiculos}', fontsize=8) 
    plt.text(0.1, 0.8, f'Mediana: {mediana_recuperacao_veiculos}', fontsize=8) # A mediana significa que 50% de todas as delegacias recuperam no máximo 1.610 veículos
    plt.text(0.1, 0.7, f'Distância: {distancia}', fontsize=8)
    plt.text(0.1, 0.6, f'Menor Valor: {minimo}', fontsize=8)
    plt.text(0.1, 0.5, f'Limite Inferior: {limite_inferior}', fontsize=8)
    plt.text(0.1, 0.4, f'Q1: {q1}', fontsize=8)
    plt.text(0.1, 0.3, f'Q3: {q3}', fontsize=8)
    plt.text(0.1, 0.2, f'Limite Superior: {limite_superior}', fontsize=8)
    plt.text(0.1, 0.1, f'Maior Valor: {maximo}', fontsize=8)
    plt.text(0.5, 0.7, f'Variância: {variancia}', fontsize=8) #
    plt.text(0.1, 0.0, f'Amplitude Total: {amplitude}', fontsize=8)# Próxima do maior valor  o que indica maior dispersão.
    plt.text(0.5, 0.9, f'Assimetria: {assimetria}', fontsize=8) # Assimetria 2.62  Positiva Alta  Valores Altos puxando a média para cima. A média tende a ser maior que a mediana
    plt.text(0.5, 0.8, f'Curtose: {curtose}', fontsize=8)  #Curtose: 8.095246616576523 Leptocúrtica Pico mais alto,  Mais valores próximo a média. É comum ter outliers bem pesados.
    plt.text(0.5, 0.6, f'Distância Variância: {distancia_var_media}', fontsize=8)# 
    plt.text(0.5, 0.5, f'Desvio Padrão: {desvio_padrao}', fontsize=8)#
    plt.text(0.5, 0.4, f'Coeficiente de variação: {coef_variacao}%', fontsize=8)#

   
    plt.title('Resumo Estatístico')

    plt.axis('off') #retirar eixos
    plt.tight_layout() #Ajustar o Layout
    plt.show()

except Exception as e:
    print(f'Erro ao plotar gráfico: {e}')






