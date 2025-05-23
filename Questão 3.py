# PROVA – Introdução à Programação (BIA)
# Nome completo: Gustavo Henrique Barros da Silva
# Matrícula: 202505701
# E-mail institucional: henriquegustavo@discnte.ufg.br

#IMPORTANDO BIBLIOTECAS
import numpy as np #Importando a biblioteca numpy e abreviando como np
import pandas as pd #Importando a biblioteca pandas e abreviando como pd
import random #Importando a biblioteca random

# Gerando 30 temperaturas aleatórias entre 10°C e 30°C, para representar dias do mês
temperaturas = np.random.uniform(10, 30, 30) #Definindo limites e tamanho dos numeros gerados (temperaturas)
temperaturas = np.round(temperaturas, 1)  #Colocando apenas 1 casa decimal

print("Temperaturas geradas:")
print(temperaturas)

#CÁLCULOS COM NUMPY

media = np.mean(temperaturas) #Média das temperaturas com Numpy (np.mean)
mediana = np.median(temperaturas) #Mediana das temperaturas com Numpy (np.median)
desvio_padrao = np.std(temperaturas) #Desvio padrão das temperaturas com Numpy (np.std)
variacao_termica = np.max(temperaturas) - np.min(temperaturas) #Variação das temperaturas com Numpy (np.max - np.min)

print('='*70)
print('Relatório Mensal de temperaturas:')
print(f'\n A média das temperaturas desse mês foi {media:.2f}°Celsius')
print(f' A mediana das temperaturas desse mês foi {mediana:.2f}°Celsius')
print(f' O desvio padrãp das temperaturas desse mês foi {desvio_padrao:.2f}°Celsius')
print(f' A variação térmica das temperaturas desse mês foi {variacao_termica:.2f}°Celsius\n')
print('='*70)

#CRIANDO DATAFRAMES COM PANDAS

dias = np.arange(1, 31) #Criando os dias de 1 a 30

dados = {
    'Dia': dias,
    'Temperatura': temperaturas
} #Criando o dicionário com o dia e sua respectiva temperatura

df = pd.DataFrame(dados) #Transformando o dicionário acima em DataFrame com pandas

df['Diferença para a média'] = df['Temperatura'] - media #Fazendo a diferença da temperatura de cada dia com a média


def classificacao_termica(temp): #Definindo a função de classificar a temperatura
    if temp < 18:
        return 'Frio' #Se a temperatura for menor que 18, retorna 'Frio'.
    elif 18 <= temp <=25 :
        return 'Agradável' #Se a temperatura for de 18 a 25, retorna 'Agradável'.
    else:
        return 'Quente' #Se a temperatura for maior que 25, retorna 'Quente'.

df['Classificação Térmica'] = df['Temperatura'].apply(classificacao_termica) #Crio a nova coluna de classificação térmica no DataFrame

print('\n Relatório detalhado de temperaturas') #Imprimo o título do relatório
print(df, '\n') #Imprimo o DataFrame
#i - Contando dias classificados como cada temperatuas

contagem = df['Classificação Térmica'].value_counts() #Definindo quantos dias teve por classificação térmica, usando o value_counts
print('='*70)
print('Dias por classificação térmica') #Título da tabela
print(contagem) #Imprimindo a tabela
print('='*70)
#ii - 5 dias mais quentes e 5 dias mais frios

#Criar uma coluna com a situação em relação à média (Útil na questão iii)
df['Situação'] = np.where(df['Diferença para a média'] > 0, 'Acima da média',
                         np.where(df['Diferença para a média'] < 0, 'Abaixo da média',
                                 'Exatamente na média'))

dias_mais_quentes = df.nlargest(5, 'Temperatura')
dias_mais_frios = df.nsmallest(5, 'Temperatura')
print('5 Dias mais quentes: ')
print(dias_mais_quentes, '\n')
print('='*70)
print('5 dias mais frios')
print(dias_mais_frios, '\n')
print('='*70)

#iii - Análise dos 5 dias mais quentes/frios com base na média mensal

print("\nAnálise dos dias extremos em relação à média:")

#Unir os dias mais quentes e mais frios
dias_extremos = pd.concat([dias_mais_quentes, dias_mais_frios])

# Exibir apenas as colunas relevantes
colunas_mostrar = ['Dia', 'Temperatura', 'Classificação Térmica', 'Situação']
print(dias_extremos[colunas_mostrar].to_string(index=False))
print('='*70)
# iv. 'responda com base nos dados'
frios_acima_media = df[(df['Classificação Térmica'] == "Frio") & (df['Diferença para a média'] > 0)] #Definindo dias frios c temperatura acima da média
quentes_abaixo_media = df [(df['Classificação Térmica'] == "Quente") & (df['Diferença para a média'] < 0)] #Definindo dias quentes c temperatura abaixo da média

print("\nPerguntas:") #Cabeçalho das perguntas
print(f"Houve dias classificados como 'Frio' acima da média?") #Faço a pergunta
if not frios_acima_media.empty: #Se existir dias frios acima da média
    print(frios_acima_media[['Dia', 'Temperatura', 'Diferença para a média']]) #Imprimo esse dia com dados
else: #Se não
    print('\n Não houveram.') #Imprimo que não houveram

print(f"\nHouve dias classificados como 'Quente' abaixo da média?") #Faço a pergunta
if not quentes_abaixo_media.empty: #Se existir dias quentes abaixo da média
    print(quentes_abaixo_media[['Dia', 'Temperatura', 'Diferença para a média']])#Imprimo esse dia com dados
else: #Se não
    print('\n Não houveram.') #Imprimo que não houveram
print('='*70)

