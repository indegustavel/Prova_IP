# PROVA – Introdução à Programação (BIA)
# Nome completo: Gustavo Henrique Barros da Silva
# Matrícula: 202505701
# E-mail institucional: henriquegustavo@discnte.ufg.br

#Parte 1: Coletando as metas de gastos do usuário
essencial = int(input('Qual sua meta de gastos na categoria "Essencial"? '))
#Pergunta ao usuário qual a meta de gastos com o essencial, com "int" definindo que vaiser número inteiro e "Input" para fazer a pergunta.

lazer = int(input('Qual a sua meta de gastos na categoria "Lazer"? '))
#Pergunta ao usuário qual a meta de gastos com lazer, com "int" definindo que vaiser número inteiro e "Input" para fazer a pergunta.

educacao = int(input('Qual sua meta de gastos na categoria "Educação"? '))
#Pergunta ao usuário qual a meta de gastos com educacao, com "int" definindo que vaiser número inteiro e "Input" para fazer a pergunta.

lancamentos = int(input('Quantos lançamentos você deseja realizar? '))
#Perguntando ao usuário quantos lançamentos ele deseja realizar, esperando também receber um número inteiro (int)

#Parte 2: Criando o bando de dados das informações
total_por_categoria = {
    'Essencial': 0,
    'Educação': 0,
    'Lazer': 0
}
#Criando dicionário para armazenar gastos por categoria

contagem_por_categoria = {
    'Essencial': 0,
    'Educação': 0,
    'Lazer': 0
}
#Criando dicionário para armazernar quantos lançamentos foram feitos por categoria

todos_lancamentos = []
#Lista para guardar detalhes dos lançamentos

todos_valores = []
#Lista para armazenar valores de cada lançamento

#Parte 3: Loop para registar lançamento
for i in range(lancamentos):
    #Para cada número no intervalo de lancamentos, o loop roda uma vez, ou seja, roda a quantidade de vezes definido em lançamentos.

    descricao = input('Com o que foi gasto? ')
    #Perguntando com o que foi gasto esse lançamento.

    valor = int(input('Qual o valor dessa despesa? '))
    #Perguntando qual o valor gasto dessa despesa, esperando receber um número inteiro (int)

    print('Em qual categoria se encaixa?\n 1- Essencial.\n 2- Lazer.\n 3- Educação.')
    # Para evitar erros nas categorias, estamos colocando números associados a três categorias pré-existentes.

    # Parte 4: Validação da categoria - loop garantindo entrada válida
    while True:
        #Loop que só encerra quando o "break" rodar, ou seja, quando for digitado 1, 2 ou 3.
        try:
            opcao = int(input("Escolha o número da categoria: "))
            #Pergunto qual o número da categoria desse lançamento, esperando receber um número inteiro (int)

            if opcao == 1:
                categoria_selecionada = "Essencial"
                break  #Se for a opção 1 (if opcao == 1:), a categoria selecionado é "Essencial" e para o loop.
            elif opcao == 2:
                categoria_selecionada = "Lazer"
                break  #Se for a opção 2 (if opcao == 2:), a categoria selecionado é "Lazer" e para o loop.
            elif opcao == 3:
                categoria_selecionada = "Educação"
                break  #Se for a opção 3 (if opcao == 3:), a categoria selecionado é "Educação" e para o loop.
            else: #Se não for digitado 1, 2 ou 3....
                print("Opção inválida. Escolha 1, 2 ou 3.")
                #Dá opção inválida e pede para escolher alguns dos números disponíveis
        except ValueError:
            print("Por favor, digite um número válido (1, 2 ou 3).")
            #Se não digitar um número (Texto, Caracteres especiais, etc) pede para escolher alguns dos números disponíveis.

    #Parte 5: Armazenando os dados
    total_por_categoria[categoria_selecionada] += valor
    #Adicionamos na categoria selecionada o valor desse lançamento

    contagem_por_categoria[categoria_selecionada] += 1
    #Aumenta o contador de lançamentos da categoria selecionada

    todos_valores.append(valor)
    #Adiciona o valor do lançamento no total gasto mensal

    lancamento = {
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria_selecionada
    }
    #Criando um dicionário com as informações do lançamento

    todos_lancamentos.append(lancamento)
    #Adicionando lançamento completo a lista de lançamentos

    print(f'Lançamento {i + 1} registrado com sucesso!')
    #Imprime no console que lançamento foi um sucesso.

#Parte 6: Cálculos
total_geral = sum(todos_valores)
#Somando todos os valores do lançamento para o gasto total.

#Calculando a média por categoria
media_por_categoria = {}
for categoria in total_por_categoria: #Loop para pegar cada lançamento em cada categoria
    if contagem_por_categoria[categoria] > 0: #Se tiver ao menos um lançamento na categoria X
        media_por_categoria[categoria] = total_por_categoria[categoria] / contagem_por_categoria[categoria]
        #Média do total gasto em X categoria pela quantidade de categorias
    else:
        media_por_categoria[categoria] = 0
        #Se não tiver lançamentos, média 0

categoria_maior_gasto = max(total_por_categoria, key=total_por_categoria.get)
#Pegando a linha com maior gasto no dicionário "total_por_categoria"

# Juntando as metas por categoria em um dicionário
metas = {
    'Essencial': essencial,
    'Lazer': lazer,
    'Educação': educacao
}

#Parte 7: Gerando relatório
print("="*50)#Linha de separação para maior clareza
print("           RELATÓRIO FINANCEIRO MENSAL           ")
print("="*50)#Linha de separação para maior clareza

print("\n 1. TOTAL DE DESPESAS NO MÊS")
print(f"R$ {total_geral:.2f}")  #Imprimo o total geral com duas casas decimais (:.2f)

print("\n2. GASTOS POR CATEGORIA")
for categoria, total in total_por_categoria.items():
    print(f"{categoria}: R$ {total:.2f}")
    #Faz um loop para mostrar o quanto gastou em cada categoria.

print("\n3. MÉDIA DE GASTOS POR CATEGORIA")
for categoria, media in media_por_categoria.items():
    print(f"{categoria}: R$ {media:.2f}")
    #Loop para mostrar a média de gastos em cada categoria.

print("\n4. CATEGORIA COM MAIOR GASTO")
print(f"{categoria_maior_gasto}: R$ {total_por_categoria[categoria_maior_gasto]:.2f}")
#Imprimi a categoria com maior gasto.

print("\n5. ANÁLISE COMPARATIVA COM METAS")
for categoria, total in total_por_categoria.items():
    meta = metas[categoria]
    diferenca = meta - total
    percentual = (total / meta * 100) if meta > 0 else 0
    #Compara a meta com o gasto e da a porcentagem que ultrapassou ou a porcentagem batida da meta

    print(f"\n{categoria}:") #Imprimo a categoria
    print(f"  Meta: R$ {meta:.2f}") #Imprimo meta da categoria
    print(f"  Gasto: R$ {total:.2f}") #Imprimo o gasto da categoria
    print(f"  {percentual:.1f}% da meta utilizada") #Imprimo o percentual da meta da categoria

print("="*50)#Linha de separação para maior clareza
print("                 FIM DO RELATÓRIO                ")
print("="*50)#Linha de separação para maior clareza