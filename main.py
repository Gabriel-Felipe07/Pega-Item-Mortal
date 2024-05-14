import random 
import pygame

class JanelaPrincipal:
    def __init__(self, width, height):
        pygame.init()  
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        self.fonte_game_over = pygame.font.SysFont('Arial', 50)

    def background(self):
        estrada = pygame.image.load("imagens/fundo.png")
        estrada = pygame.transform.scale(estrada, (self.width, self.height))
        self.display.blit(estrada, (0,0))

    def mostra_game_over(self):
        texto_game_over = self.fonte_game_over.render("Game Over", True, (255, 0, 0))
        largura_texto, altura_texto = texto_game_over.get_size()
        pos_x = (self.width - largura_texto) // 2
        pos_y = (self.height - altura_texto) // 2
        self.display.blit(texto_game_over, (pos_x, pos_y))


class Jogador:
    def __init__(self, width, height, pos_x, pos_y, imagem):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.original_imagem = pygame.image.load(imagem)
        self.imagem = pygame.transform.scale(self.original_imagem, (self.width, self.height))
        self.mascara = pygame.mask.from_surface(self.imagem)
        self.velocidade_normal = 10
        self.velocidade_especial = 20
        self.tamanho_normal = (width, height)
        self.tamanho_especial = (int(width * 0.8), int(height * 0.8))
        self.especial_ativo = False
        self.tempo_especial = 5  # Tempo em segundos
        self.vezes_usadas = 3

    def cria_jogador(self, tela):
        tela.blit(self.imagem, (self.pos_x, self.pos_y))

    def movimentacao_jogador(self, velocidade):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.pos_x -= velocidade
        elif keys[pygame.K_RIGHT]:
            self.pos_x += velocidade

        if self.pos_x >= 800 or self.pos_x <= 0:
            self.pos_x = 350
            self.pos_y = 355

        if self.especial_ativo:
            self.tempo_especial -= 1 / 60  # Reduz o tempo especial
            if self.tempo_especial <= 0:
                self.desativa_especial()

    def ativa_especial(self):
        if self.vezes_usadas > 0:
            self.vezes_usadas -= 1
            self.especial_ativo = True
            self.imagem = pygame.transform.scale(self.original_imagem, self.tamanho_especial)
            self.velocidade_normal = self.velocidade_especial
            self.tempo_especial = 5  # Reinicia o tempo especial

    def desativa_especial(self):
        self.especial_ativo = False
        self.imagem = pygame.transform.scale(self.original_imagem, self.tamanho_normal)
        self.velocidade_normal = 10

class Cogumelos:
    def __init__(self, width, height, pos_x, pos_y, velocidade, tipo):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.velocidade = velocidade
        self.pos_y = pos_y
        self.imagem = pygame.image.load(tipo)
        self.imagem = pygame.transform.scale(self.imagem, (self.width, self.height))
        self.mascara = pygame.mask.from_surface(self.imagem)

    def move_cogumelos(self):
        self.pos_y += self.velocidade
        if self.pos_y >= 800:
            self.pos_y = 0
            self.pos_x = random.randint(0,500)

    def cria_cogumelos(self, tela):
        tela.blit(self.imagem, (self.pos_x, self.pos_y))


class Inimigos:
    def __init__(self, width, height, pos_x, pos_y, velocidade, tipo):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.velocidade = velocidade
        self.pos_y = pos_y
        self.imagem = pygame.image.load(tipo)
        self.imagem = pygame.transform.scale(self.imagem, (self.width, self.height))
        self.mascara = pygame.mask.from_surface(self.imagem)

    def move_inimigo(self):
        self.pos_y += self.velocidade
        if self.pos_y >= 800:
            self.pos_y = 0

    def cria_inimigo(self, tela):
        tela.blit(self.imagem, (self.pos_x, self.pos_y))


class MenuPontuacao:
    def __init__(self, fonte, tamanho_fonte):
        self.fonte = pygame.font.SysFont(fonte, tamanho_fonte)
        self.pontuacao = 0

    def atualiza_pontuacao(self, tela):
        texto = self.fonte.render("Pontuação: " + str(self.pontuacao), True, (255, 255, 255))
        tela.blit(texto, (10, 10))

    def aumenta_pontuacao(self):
        self.pontuacao += 1

    def diminui_pontuacao(self):
        self.pontuacao -= 1


def main():
    janela = JanelaPrincipal(800, 500)
    janela.background()

    cogumelos_lista = [
        Cogumelos(60,60,random.randint(50,500),-100,random.randint(5,20),"imagens/amarelo.png"),
        Cogumelos(60,60,random.randint(50,500),-100,random.randint(5,20),"imagens/verde.png"),
        Cogumelos(60,60,random.randint(50,500),-100,random.randint(5,20),"imagens/vermelho.png"),
        Cogumelos(60,60,random.randint(50,500),-100,random.randint(5,20),"imagens/azul.png")
        ]

    inimigos_lista = [
        Inimigos(60,60,random.randint(50,500),-100,random.randint(5,20),"imagens/bomba.png"),
        Inimigos(60,60,random.randint(50,500),-100,random.randint(5,20),"imagens/goomba.png"),
        Inimigos(60,60,random.randint(50,500),-100,random.randint(5,20),"imagens/inimigo.png")
    ]

    personagem = Jogador(110,100, 350,355,"imagens/mario.png")

    menu_pontuacao = MenuPontuacao('Arial', 20)

    clock = pygame.time.Clock()

    rodando = True
    game_over = False


    #carregando som
    som_bonus = pygame.mixer.Sound("sons/bonus.mp3")
    som_cogumelo = pygame.mixer.Sound("sons/cogumelo.mp3")
    som_gameOver = pygame.mixer.Sound("sons/gameOver.mp3")
    
    pygame.mixer.music.load("sons/fundo.mp3")
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.play()

    tempo_especial = 0
    vezes_usadas = 3
    tempo_ultimo_uso = 0

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        if not game_over:
            for cogumelo in cogumelos_lista:
                cogumelo.move_cogumelos()

            for inimigo in inimigos_lista:
                inimigo.move_inimigo()

            janela.background()
            for cogumelo in cogumelos_lista:
                cogumelo.cria_cogumelos(janela.display)


            for inimigo in inimigos_lista:
                inimigo.cria_inimigo(janela.display)
                
            if pygame.key.get_pressed()[pygame.K_SPACE] and tempo_ultimo_uso == 0 and vezes_usadas > 0:
                personagem.ativa_especial()
                som_bonus.play()
                tempo_ultimo_uso = pygame.time.get_ticks()
                vezes_usadas -= 1
            
            if tempo_ultimo_uso != 0:
                tempo_especial = (pygame.time.get_ticks() - tempo_ultimo_uso) / 1000
            
            if tempo_especial >= 5:
                personagem.desativa_especial()
                tempo_ultimo_uso = 0
            
            personagem.movimentacao_jogador(personagem.velocidade_normal if not personagem.especial_ativo else personagem.velocidade_especial)
            personagem.cria_jogador(janela.display)

            for cogumelo in cogumelos_lista:
                if personagem.mascara.overlap(cogumelo.mascara,(cogumelo.pos_x - personagem.pos_x, cogumelo.pos_y - personagem.pos_y)):
                    cogumelo.pos_x = random.randint(50,499)
                    cogumelo.pos_y = -100
                    menu_pontuacao.aumenta_pontuacao()
                    som_cogumelo.play()

            for inimigo in inimigos_lista:
                if personagem.mascara.overlap(inimigo.mascara,(inimigo.pos_x - personagem.pos_x, inimigo.pos_y - personagem.pos_y)):
                    game_over = True

            menu_pontuacao.atualiza_pontuacao(janela.display)
        else:
            janela.mostra_game_over()
            som_gameOver.play()


        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()