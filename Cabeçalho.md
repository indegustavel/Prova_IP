# PROVA – Introdução à Programação (BIA)
Nome completo: Gustavo Henrique Barros da Silva
Matrícula: 202505701
E-mail institucional: henriquegustavo@discnte.ufg.br

1- Questão tranquila, apenas o básico
A) Conceitos básicos aplicados, como "Input" e "int"
B) Me fez pensar, mas utilizei o 'try', 'if' e 'except' para garantir que o valor seja valido
C) Conceitos básicos aplicados, como 'def', 'return' e operações matemáticas
D) Conceitos básicos aplicados, como 'print'

2- Questão intermediária, aborda conceitos básicos de forma aprofundada
A) 'Int' e 'Input' para solicitar aos usuários as metas
B) 'Int' e 'Input' para solicitar aos usuários os lançamentos
C) Além 'Int' e 'Input' para solicitar aos usuários os dados, tive que colocar alguns dicionários e listas também para
armazenar os resultados, e loops para garantir respostas válidas
D) Parte mais complexa da questão, tive que pesquisar acerca de operações com dicionários e etc.
Aborda os conceitos básicos de forma geral e completa

3- Aborda o nível intermediário do Python, com a utilização de bibliotecas essenciais e suas principais funções
Primeiro coisa a se fazer é importar a biblioteca random e utilizar alguns comandos para gerar números aleatorios
e guardalos em variáveis

A) Comandos básicos do Numpy (np.mean, np.median, etc), sem muita dificuldade
B) Um pouco mais complexo, envolveu algumas pesquisas sobre pandas e numpy, acerca de criar novas colunas
mas nada que deu muito trabalho.
C) Relativamente simples, criei o df em pandas, consegui criar a coluna e crei um função para classificar as temperaturas
de cada dia utilizando 'if'
D) Parte mais complexa da questão, envolveu bastantes pesquisas
i) Usei o value.counts() para contar os quantos dias teve cada classificação.
ii) Para contar os 5 dias mais quentes e mais frios, utilizei df.nlargest e df.nsmallest. Envolveu algumas pesquisas,
pois não sabia da existência desses comandos.
iii) Após isso, concatenei também os 10 dias para melhor leitura dos dados e adicionei a nova coluna. 
Envolveu algumas pesquisas, pois não sabia da existência desses comandos.
iv) Defini os dias quentes abaixo da media e frios acima da media de acordo com requisitos, e usei condicional
para verificar se existiam, depois formatei tudo e imprimi. Envolveu poucas pesquisas

4- Questão bem complexa para meu nível em python, envolveu muitas pesquisas, vídeos e LLMs.
Utilizei a biblioteca PyGame, random e time para controlar o Tetris.
Abordei muuitos recursos que nunca tinha visto antes, desde básicos como "class" até avançados do próprio PyGame.
Tive de utilizar bastante pesquisas, vídeos e LLM para estruturação e lógica de código, principalmente na parte de colisão.
Gostei do resultado final, apesar de ter sido com "consulta"

5- 
A)
==================================================

Quais ferramentas utilizamos?
Nós utilizamos a ferramenta ChatVolt e o n8n, para a construção de Agentes Inteligentes 
 destinados a academias, criando nossa Startup Neurofit. 

Por que utilizamos?
Utilizamos a ChatVolt pela patricidade e escalabilidade de criar Agentes de I.A, e utilizamos 
 eventualmente o n8n para fazer automações externas de acordo com a necessidade dos nossos clientes
==================================================

B) UMA FUNCIONALIDADE CONCRETA:

Criamos um Agente Inteligente para a Academia Ideal, em Anápolis - GO.
Seu nome é Caroline, e ela é responsável pelo atendimento completos dos clientes via WhatsApp.
Além disso, ela também ajuda na retenção de alunos com follow-ups automáticos e tira as dúvidas que algum leads podem ter.
Nós criamos esse Agente na ChatVolt, utilizando a LLM GPT 4o Mini, com a temperatura em 0.1 (para evitar alucionações).
Colocamos todos os dados da academia na base de conhecimento, e instruímos ela no prompt para atender de acordo com as preferências do nosso cliente.
Criamos também algumas HTTP Tools para o agente mudar o Status da conversa para resolvido, evitando follow-ups desnecessários
Utilizamos também o Z API para a integração do Agente Inteligente ao WhatsApp, principal canal de conversas da academia.
==================================================

C) FUNCIONALIDADES QUE ESTAMOS BUSCANDO IMPLEMENTAR

Estamos estudando implementar o Agente Inteligente direto a API das academias para automatizar ainda mais o trabalho
Se conseguirmos, as possibilidades de automações são diversas, desde mensagens automáticas aos clientes de acordo com sua inatividade
até a manipulação de cadastros, cancelamentos, etc.
==================================================

6)Questão extremamente complexa para meu nível em python, envolveu muitas pesquisas, vídeos e LLMs.

Criei um sistema para verificar a variação e o preço de criptomoedas nas últimas 24h. 
O sistema usa a API pública do CoinGecko (bem limitada) e uma interface construída com Tkinter.

Usei as bibliotecas:
'tkinter' para criar a interface gráfica
'requests' para fazer as chamadas à API
'threading' para não travar a interface durante as requisições
'datetime' para registrar o momento das atualizações
'json' para manipular o cache de dados
'pathlib' para gerenciar os arquivos de cache de forma mais segura.
Para evitar o erro 429 (Muitas requisições), adicionei um controle simples que impede que duas requisições sejam feitas em um intervalo menor que 10 segundos.
Principais desafios:
Limitação da API: O maior desafio foi lidar com o limite de requisições da API do CoinGecko. Resolvi isso implementando um sistema de cache e controle de taxa.
Feedback aousuário: Adicionei mensagens claras para que o usuário entenda o que está acontecendo, especialmente quando há problemas com a API.
Abordei DIVERSOS temas que não conhecia, desde comandos básicos até avançados.
Pela complexidade do tema ante à minha experiência em python, considerei bastante complexa.
Tive de utilizar bastante consulta externa para conseguir estruturar o código.





