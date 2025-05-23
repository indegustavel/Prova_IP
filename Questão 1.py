# PROVA – Introdução à Programação (BIA)
# Nome completo: Gustavo Henrique Barros da Silva
# Matrícula: 202505701
# E-mail institucional: henriquegustavo@discnte.ufg.br


while True: #Cria um laço de repetição para só parar quando "break" for chamado. Ou seja, o laço só acaba de chegar no "break"

    try: #Converter os futuros valores para número real

        potencia = int(input("Qual a potência do seu aparelho? (em kWh): ")) #definindo variável (potencia = ...)
        # definindo que vai ser número inteiro (int)
        # definindo que é uma entrada de dados (input)
        # definindo a pergunta que vai chegar ao usuário( "Qual a potência...")

        if potencia > 0: #Se a potência for maior que zero ("if" é o comando para "se")

            break #Chama a o break para encerrar o laço de repetição

        else: #Se a potência não for maior que zero

            print('Digite um número maior que 0') #Imprime no console para o usuário digitar um número maior que zero

    except ValueError: #Se o usuário não digitar um número válido

        print('Valor inválido. Digite um número real.') #Imprime no console para o usuário digitar um número válido


while True:  # Cria um laço de repetição para só parar quando "break" for chamado. Ou seja, o laço só acaba de chegar no "break"

    try:  # Converter os futuros valores para número real

        tempo = int(input("Qual o tempo médio de uso diário? (em horas): "))  # definindo variável (tempo = ...)
        # definindo que vai ser número inteiro (int)
        # definindo que é uma entrada de dados (input)
        # definindo a pergunta que vai chegar ao usuário( "Qual o tempo...")

        if tempo > 0:  # Se o tempo for maior que zero ("if" é o comando para "se")

            break  # Chama a o break para encerrar o laço de repetição

        else:  # Se o tempo não for maior que zero

            print('Digite um número maior que 0')  # Imprime no console para o usuário digitar um número maior que zero

    except ValueError:  # Se o usuário não digitar um número válido

        print('Valor inválido. Digite um número real.')  # Imprime no console para o usuário digitar um número válido

def calcular_consumo_mensal(a, b): # Definindo uma função para calcular o consumo mensal
    return a * b * 30 #Definindo o que essa função vai fazer quando receber os valores "a" e "b"

gasto_mensal = calcular_consumo_mensal(potencia, tempo) #Defino que essa variável é a "função calcular_consumo_mensal" quando é recebido as variaveis "potencia" e "tempo"

print(f'Seu gasto mensal com energia é: {gasto_mensal:.2f} kWh') #Imprimo na tela o gasto de energia do usuário, com 2 casas decimais.


