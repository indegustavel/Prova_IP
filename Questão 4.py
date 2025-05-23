# PROVA – Introdução à Programação (BIA)
# Nome completo: Gustavo Henrique Barros da Silva
# Matrícula: 202505701
# E-mail institucional: henriquegustavo@discnte.ufg.br


#Bibliotecas necessárias
import pygame
import random
import time

#Iniciando o PyGame
pygame.init()

#Medidas do jogo
LARGURA, ALTURA = 400, 500  #Dimensões da janela
LARGURA_GRADE = 10
ALTURA_GRADE = 20
TAMANHO_BLOCO = 20  #Tamanho de cada bloco
BORDA_ESQUERDA = (LARGURA - LARGURA_GRADE * TAMANHO_BLOCO) // 2
TOPO = ALTURA - ALTURA_GRADE * TAMANHO_BLOCO - 50

#Definindo as cores básicas
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (128, 128, 128)
AZUL = (0, 0, 255)
CIANO = (0, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
MAGENTA = (255, 0, 255)
AMARELO = (255, 255, 0)
LARANJA = (255, 165, 0)

# Definindo das formas das peças
FORMAS = [
    [[0, 0], [0, 1], [1, 0], [1, 1]],  # O (quadrado)
    [[0, 0], [-1, 0], [1, 0], [2, 0]],  # I (linha)
    [[0, 0], [-1, 0], [1, 0], [0, 1]],  # T
    [[0, 0], [1, 0], [0, 1], [1, 1]],  # O (quadrado)
    [[0, 0], [-1, 0], [0, 1], [1, 1]],  # Z
    [[0, 0], [1, 0], [-1, 1], [0, 1]],  # S
    [[0, 0], [-1, 0], [1, 0], [-1, 1]],  # J
    [[0, 0], [-1, 0], [1, 0], [1, 1]]  # L
]

# Lista de cores para as peças
CORES = [CIANO, AZUL, LARANJA, AMARELO, VERDE, MAGENTA, VERMELHO]

# Configuração da janela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Mini Tetris - Prova de IP - Gustavo H. B. da Silva')

clock = pygame.time.Clock()  #Controlando tempo


#Classe para representar a peça atual
class Peca:
    def __init__(self):
        # Escolhe uma forma aleatória entre as definidas
        self.forma = random.choice(FORMAS)
        # Escolhe uma cor aleatória
        self.cor = random.choice(CORES)
        # Posição inicial (meio do topo da grade)
        self.x = LARGURA_GRADE // 2
        self.y = 0
        self.rotacao = 0  # 0, 1, 2, 3 para as 4 possíveis rotações

    def blocos(self):
        """Retorna a lista de blocos (posições) da peça atual com base na rotação"""
        blocos_posicionados = []
        for x, y in self.forma:
            # Aplica rotação (sentido horário)
            if self.rotacao == 0:
                blocos_posicionados.append((self.x + x, self.y + y))
            elif self.rotacao == 1:
                blocos_posicionados.append((self.x + y, self.y - x))
            elif self.rotacao == 2:
                blocos_posicionados.append((self.x - x, self.y - y))
            elif self.rotacao == 3:
                blocos_posicionados.append((self.x - y, self.y + x))
        return blocos_posicionados


#Criando a grade do jogo (matriz)
def criar_grade():
    # Inicializa uma grade vazia 10x20, com zeros representando espaços vazios
    return [[0 for _ in range(LARGURA_GRADE)] for _ in range(ALTURA_GRADE)]


def desenhar_grade(grade):
    #Desenha a grade e as peças fixadas nela
    for i in range(ALTURA_GRADE):
        for j in range(LARGURA_GRADE):
            # Desenha um retângulo para cada célula da grade
            pygame.draw.rect(
                tela,
                CINZA,
                (BORDA_ESQUERDA + j * TAMANHO_BLOCO,
                 TOPO + i * TAMANHO_BLOCO,
                 TAMANHO_BLOCO,
                 TAMANHO_BLOCO),
                1  # Espessura da borda
            )
            # Se houver uma peça na célula (valor > 0), preenche com a cor correspondente
            if grade[i][j] > 0:
                cor_idx = min(grade[i][j] - 1, len(CORES) - 1)  # Evita índice fora do intervalo
                pygame.draw.rect(
                    tela,
                    CORES[cor_idx],
                    (BORDA_ESQUERDA + j * TAMANHO_BLOCO,
                     TOPO + i * TAMANHO_BLOCO,
                     TAMANHO_BLOCO,
                     TAMANHO_BLOCO)
                )


def desenhar_peca(peca):
    for x, y in peca.blocos():
        # Verifica se o bloco está dentro da área visível
        if 0 <= y < ALTURA_GRADE and 0 <= x < LARGURA_GRADE:
            pygame.draw.rect(
                tela,
                peca.cor,
                (BORDA_ESQUERDA + x * TAMANHO_BLOCO,
                 TOPO + y * TAMANHO_BLOCO,
                 TAMANHO_BLOCO,
                 TAMANHO_BLOCO)
            )


def colisao(grade, peca):
    #Verifica se há colisão da peça com as bordas ou outras peças
    for x, y in peca.blocos():
        # Verifica limites laterais e inferior
        if x < 0 or x >= LARGURA_GRADE or y >= ALTURA_GRADE:
            return True
        # Verifica colisão com outras peças (apenas se estiver dentro da grade)
        if y >= 0 and x >= 0 and y < ALTURA_GRADE and x < LARGURA_GRADE and grade[y][x] > 0:
            return True
    return False


def fixar_peca(grade, peca):
    for x, y in peca.blocos():
        # Verifica se a posição está dentro dos limites da grade
        if 0 <= y < ALTURA_GRADE and 0 <= x < LARGURA_GRADE:
            # Protege contra índice de cor inválido
            cor_idx = CORES.index(peca.cor) if peca.cor in CORES else 0
            grade[y][x] = cor_idx + 1
    return grade


def verificar_linhas_completas(grade):
    #Verifica e remove linhas completas, retornando o número de linhas removidas
    linhas_completas = 0
    for i in range(ALTURA_GRADE):
        # Se todos os elementos da linha forem diferentes de zero (preenchidos)
        if all(grade[i]):
            linhas_completas += 1
            # Move todas as linhas acima para baixo
            for y in range(i, 0, -1):
                grade[y] = grade[y - 1][:]
            # A linha do topo fica vazia
            grade[0] = [0] * LARGURA_GRADE
    return linhas_completas


def desenhar_interface(pontuacao, nivel):
    fonte = pygame.font.SysFont('Arial', 20)
    texto_pontuacao = fonte.render(f'Pontuação: {pontuacao}', True, BRANCO)
    texto_nivel = fonte.render(f'Nível: {nivel}', True, BRANCO)
    tela.blit(texto_pontuacao, (10, 10))
    tela.blit(texto_nivel, (10, 40))


def game_over(): #Definindo mensagem de fim de jogo
    fonte = pygame.font.SysFont('Arial', 30)
    texto = fonte.render('Você é muito ruim.', True, VERMELHO)
    texto_rect = texto.get_rect(center=(LARGURA // 2, ALTURA // 2))
    tela.blit(texto, texto_rect)

    instrucao = fonte.render('Pressione R para reiniciar', True, BRANCO)
    instrucao_rect = instrucao.get_rect(center=(LARGURA // 2, ALTURA // 2 + 50))
    tela.blit(instrucao, instrucao_rect)

    pygame.display.update()

    # Aguarda o jogador pressionar R para reiniciar
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    esperando = False
                    return True
    return False


def principal(): #Definindo funcao q executa o jogo
    grade = criar_grade()
    peca_atual = Peca()
    proxima_peca = Peca()

    pontuacao = 0
    nivel = 1
    linhas_totais = 0

    # Velocidade inicial de queda
    velocidade_queda = 500
    ultima_queda = time.time() * 1000

    # Flag para indicar se o jogo está em execução
    jogando = True

    while jogando:
        # Atualiza o tempo atual
        tempo_atual = time.time() * 1000

        # Move a peça para baixo quando for hora
        if tempo_atual - ultima_queda > velocidade_queda:
            ultima_queda = tempo_atual

            # Cria uma cópia temporária da peça para verificar colisão
            peca_temp = Peca()
            peca_temp.forma = peca_atual.forma
            peca_temp.cor = peca_atual.cor
            peca_temp.x = peca_atual.x
            peca_temp.y = peca_atual.y + 1  # Tenta mover para baixo
            peca_temp.rotacao = peca_atual.rotacao

            # Verifica se a peça pode mover para baixo
            if colisao(grade, peca_temp):
                # Se não pode, fixa a peça na posição atual
                grade = fixar_peca(grade, peca_atual)

                # Verifica se há linhas completas
                linhas_removidas = verificar_linhas_completas(grade)
                if linhas_removidas > 0:
                    # Atualiza pontuação (mais pontos por mais linhas de uma vez)
                    pontuacao += (linhas_removidas ** 2) * 100
                    linhas_totais += linhas_removidas

                    # Aumenta o nível a cada 10 linhas
                    nivel = linhas_totais // 10 + 1
                    # Aumenta a velocidade de queda com o nível
                    velocidade_queda = max(100, 500 - nivel * 40)

                # Criando uma nova peça
                peca_atual = proxima_peca
                proxima_peca = Peca()

                # Verifica se a nova peça já causa colisão (game over)
                if colisao(grade, peca_atual):
                    if not game_over():
                        jogando = False
                    else:
                        # Reinicia o jogo
                        grade = criar_grade()
                        peca_atual = Peca()
                        proxima_peca = Peca()
                        pontuacao = 0
                        nivel = 1
                        linhas_totais = 0
                        velocidade_queda = 500
            else:
                # Se não há colisão, move para baixo
                peca_atual.y += 1

        # Processando eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogando = False

            if evento.type == pygame.KEYDOWN:
                # Movimentos
                if evento.key == pygame.K_LEFT:
                    # Tenta mover para a esquerda
                    peca_atual.x -= 1
                    if colisao(grade, peca_atual):
                        peca_atual.x += 1  # Desfaz o movimento se causar colisão

                elif evento.key == pygame.K_RIGHT:
                    # Tenta mover para a direita
                    peca_atual.x += 1
                    if colisao(grade, peca_atual):
                        peca_atual.x -= 1  # Desfaz o movimento se causar colisão

                elif evento.key == pygame.K_DOWN:
                    # Tenta mover para baixo
                    peca_atual.y += 1
                    if colisao(grade, peca_atual):
                        peca_atual.y -= 1  # Desfaz o movimento se causar colisão

                elif evento.key == pygame.K_UP:
                    # Tenta rotacionar
                    rotacao_antiga = peca_atual.rotacao
                    peca_atual.rotacao = (peca_atual.rotacao + 1) % 4
                    if colisao(grade, peca_atual):
                        peca_atual.rotacao = rotacao_antiga  # Desfaz a rotação se causar colisão

                elif evento.key == pygame.K_SPACE:
                    # Queda rápida (hard drop)
                    while True:
                        peca_atual.y += 1
                        if colisao(grade, peca_atual):
                            peca_atual.y -= 1  # Volta uma posição para evitar a colisão
                            break

        # Limpa a tela
        tela.fill(PRETO)

        # Desenha a grade e as peças
        desenhar_grade(grade)
        desenhar_peca(peca_atual)
        desenhar_interface(pontuacao, nivel)

        # Atualiza a tela
        pygame.display.update()

        # Controla a taxa de atualização
        clock.tick(60)

    # Encerra o Pygame quando o jogo termina
    pygame.quit()


# Inicia o jogo
if __name__ == "__main__":
    principal()