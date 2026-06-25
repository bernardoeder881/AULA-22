
# Calculando a Assimetria
try:
    # Assimetria
    # Medida q indica como os dados estão distriuidos em torno do valor central
    # Estão distribuidos em torno do Centro?
    # Existe uma qtd maior de registros altos ou baixos?
    # Para que lado está o peso.
    # É a medida usada para descrever o grau de simetria ou assimetria

    # INTERPRETAÇÃO (Pontos de Observação):
    # Assimetria > 1: Positiva Alta
    # Valores Altos puxando a média para cima.
    # A média tende a ser maior que a mediana

    # Assimetria entre 0.5 e 1: Positiva Moderada
    # Há cauda à direita, mas é menos acentuada

    # Assimetria entre -0.5 e 0.5: Distribuição aproximadamente Simétrica
    # Tendência de dados equilibrados
    # A média, a mediana, e a moda tenha valores próximos

    # Assimetria entre -1 e -0.5: Negativa Moderada
    # Há cauda à esquerda, mas é menos acentuada

    # Assimetria < -1: Negativa Alta
    # Valores Baixo puxando a média para Baixo.
    # A média tende a ser menor que a mediana
    assimetria = df_recuperacao_veiculos['recuperacao_veiculos'].skew()
    curtose = df_roubo_veiculo['roubo_veiculo'].kurtosis()

    print('\nMedidas de Distribuição')
    print(40*'=')
    print(f'Assimetria: {assimetria}')
    print(f'Curtose: {curtose}')




except Exception as e:
    print(f'Erro ao calcular medida de distribuição: {e}')


# Medidas de dispersão "Varabilidade"
try:
    print ('Calculando a variabilidade dos dados')
    # Variância
    # É uam medida para observar a dispersão dos dados
    # Observa-se em relação a média
    # É a média dos quadrados, das diferenças entre cada valor e a média.
    # OBS: O resultado da variância está elevado ao quadrado

    # Interpretação:
    # Quanto maior a variância maior vai ser o afastamento dos valores em relação a a média.
    # Neste caso, a variância elevada indica alta dispersão.

    variancia = np.var(array_roubo_veiculo)
    distancia_var_media = variancia /( media_roubo_veiculo ** 2)*100
    # Desvio Padrão
    # É a raiz quadrada da variância
    # É a normalização da variância. Por isso é mais fácil a interpreação.
    # Apresentar o quanto os dados estão afastados da média, tanto para mais , quanto para menos.

    desvio_padrao= np.std(array_roubo_veiculo)

    # Coeficiente de Variação
    # É a magnitude do desvio Padrão em relaçõa a média.
    coef_variacao = desvio_padrao / media_roubo_veiculo

    print('\nMedidas de Dispersão')
    print(40*'=')
    print(f'Variância: {variancia}')
    print(f'Distância entre média e Variância:{distancia_var_media}')
    print(f'Desvio Padrão: {desvio_padrao}')
    print(f'')

except Exception as e:
    print(f'Erro ao calcular medida de dipersão: {e}')
 


    plt.text(0.5, 0.9, f'Assimetria: {assimetria}', fontsize=10)
    plt.text(0.5, 0.8, f'Curtose: {curtose}', fontsize=10)
    plt.text(0.5, 0.7, f'Variância: {variancia}', fontsize=10)
    plt.text(0.5, 0.6, f'Distância Variância: {distancia_var_media}', fontsize=10)
    plt.text(0.5, 0.5, f'Desvio Padrão: {desvio_padrao}', fontsize=10)
    plt.text(0.5, 0.4, f'Coeficiente de variação: {coef_variacao}%', fontsize=10)