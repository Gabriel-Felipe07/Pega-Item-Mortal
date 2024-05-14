import random 
import pygame

class JanelaPrincipal:
    #criando a função de init
    def __init__(self, width, height):
        #iniciando o pygame
        pygame.init()  # Inicializa o pygame
        #definindo o self de width
        self.width = width
        #definindo o self de height
        self.height = height
        #definindo o self do tamanho da tela
        self.display = pygame.display.set_mode((self.width, self.height))
        
        #carregando a imagem da estrada
    def background(self):
        estrada = pygame.image.load("imagens/fundo.png")
        #definindo uma escala para a estrada
        estrada = pygame.transform.scale(estrada, (self.width, self.height))
        #adicionando a estrada ao layout
        self.display.blit(estrada, (0,0))


class Jogador:
    #criando a função init
    def __init__(self, width, height, pos_x, pos_y, imagem):
        #definindo o self de width
        self.width = width
        self.height = height #definindo o self de height
        self.pos_x = pos_x #definindo o self da posição x do personagem
        self.pos_y = pos_y #definindo o self da posição x do personagem
        self.imagem = pygame.image.load(imagem) #carregando a imagem do personagem
        self.imagem = pygame.transform.scale(self.imagem, (self.width, self.height)) #definindo uma escala para a imagem do personagem

        self.mascara = pygame.mask.from_surface(self.imagem) #adicionando uma mascara ao personagem

    #criando o jogador
    def cria_jogador(self, tela):
        tela.blit(self.imagem, (self.pos_x, self.pos_y))

    #adicionando a função responsável por fazer a movimentação do jogador
    def movimentacao_jogador(self, velocidade):
        #definindo que será usando o teclado / mouse 
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:# se a tecla para a esquerda for pressionada
            self.pos_x -= velocidade
        elif keys[pygame.K_RIGHT]:#se a tecla para a direita for pressionada
            self.pos_x += velocidade

        if self.pos_x >= 800 or self.pos_x <= 0:
            self.pos_x = 350
            self.pos_y = 355


class cogumelos:
    def __init__(self, width, height, pos_x, pos_y, velocidade, tipo):#função init
        self.width = width#definindo width
        self.height = height#definindo height
        self.pos_x = pos_x  # Identificador da pista (1, 2, 3, etc.)
        self.velocidade = velocidade  # Velocidade horizontal dos carros
        self.pos_y = pos_y
        self.imagem = pygame.image.load(tipo)#carregando imagem
        self.imagem = pygame.transform.scale(self.imagem, (self.width, self.height))#definindo escala para o carro

        self.mascara = pygame.mask.from_surface(self.imagem) #criando mascara para o carro

    #movimentação do carro
    def move_cogumelos(self):
        # O carro vai andando conforme a velocidade descrita
        self.pos_y += self.velocidade #definindo velocidade
        # Se o carro passar do limite da tela, redefine sua posição para a posição inicial
        if self.pos_y >= 800:#se passar da tela, retorna
            self.pos_y = 0

    def cria_cogumelos(self, tela):#criando carro
        tela.blit(self.imagem, (self.pos_x, self.pos_y))

class Inimigos:
    def __init__(self, width, height, pos_x, pos_y, velocidade, tipo):#função init
        self.width = width#definindo width
        self.height = height#definindo height
        self.pos_x = pos_x  # Identificador da pista (1, 2, 3, etc.)
        self.velocidade = velocidade  # Velocidade horizontal dos carros
        self.pos_y = pos_y
        self.imagem = pygame.image.load(tipo)#carregando imagem
        self.imagem = pygame.transform.scale(self.imagem, (self.width, self.height))#definindo escala para o carro

        self.mascara = pygame.mask.from_surface(self.imagem) #criando mascara para o carro

    #movimentação do carro
    def move_inimigo(self):
        # O carro vai andando conforme a velocidade descrita
        self.pos_y += self.velocidade #definindo velocidade
        # Se o carro passar do limite da tela, redefine sua posição para a posição inicial
        if self.pos_y >= 800:#se passar da tela, retorna
            self.pos_y = 0

    def cria_inimigo(self, tela):#criando carro
        tela.blit(self.imagem, (self.pos_x, self.pos_y))

class MenuPontuacao:
    def __init__(self, fonte, tamanho_fonte):#função inicial
        self.fonte = pygame.font.SysFont(fonte, tamanho_fonte)#passando fonte e tamanho
        self.pontuacao = 0#definindo pontuação 0

    #atualizando pontuação
    def atualiza_pontuacao(self, tela):
        texto = self.fonte.render("Pontuação: " + str(self.pontuacao), True, (255, 255, 255))
        tela.blit(texto, (10, 10))

    #aumentando pontuação
    def aumenta_pontuacao(self):
        self.pontuacao += 1

    #diminuindo pontuação
    def diminui_pontuacao(self):
        self.pontuacao -= 1


def main():
    #criando a janela
    # Criando janela    
    janela = JanelaPrincipal(800, 500)
    #criando a estrada
    janela.background()


    # Criando carros
    cogumelos_lista = [
        cogumelos(60,60,random.randint(0,500),-100,15,"imagens/amarelo.png"),
        cogumelos(60,60,random.randint(0,500),-100,15,"imagens/verde.png"),
        cogumelos(60,60,random.randint(0,500),-100,15,"imagens/vermelho.png"),
        cogumelos(60,60,random.randint(0,500),-100,15,"imagens/azul.png") # cogumelo 1
        ] # Carro na pista 6
    
    inimigos_lista = [
        
    ]

    # Criando personagem
    personagem = Jogador(110,100, 350,355,"imagens/mario.png")

    # Criando menu de pontuação
    menu_pontuacao = MenuPontuacao('Arial', 20)

    # Clock para regulagem de fps
    clock = pygame.time.Clock()

    # Loop principal
    rodando = True
    #loop principal iniciado
    while rodando:
        #verificando evento de cancelar
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

    #criando os carros
        # Movimentação dos carros
        for cogumelo in cogumelos_lista:
            cogumelo.move_cogumelos()

    #desenhando os objetos
        # Desenhar objetos
        janela.background()
        for cogumelo in cogumelos_lista:
            cogumelo.cria_cogumelos(janela.display)

        personagem.movimentacao_jogador(10)
        personagem.cria_jogador(janela.display)

    #verificação de colizão e diminuindo pontuação
        for cogumelo in cogumelos_lista:
            if personagem.mascara.overlap(cogumelo.mascara,(cogumelo.pos_x - personagem.pos_x, cogumelo.pos_y - personagem.pos_y)):
                cogumelo.pos_x = random.randint(0,499)
                cogumelo.pos_y = random.randint(0,499)
                menu_pontuacao.aumenta_pontuacao()
                while menu_pontuacao.pontuacao < 0:
                    menu_pontuacao.pontuacao =0
        #verificando condição de ganhar e aumentando pontuação 
        if personagem.pos_y <= 0:
            menu_pontuacao.aumenta_pontuacao()
                        #se o personagem passar dos parametros da tela, voltará à posição inicial
            if personagem.pos_x >= 800 or personagem.pos_x <= 0:
                personagem.pos_x = 350
                personagem.pos_y = 355

        # Atualizar e desenhar a pontuação
        menu_pontuacao.atualiza_pontuacao(janela.display)

        # Atualizar janela
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()