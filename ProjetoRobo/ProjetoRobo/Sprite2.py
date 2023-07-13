from typing import Any
import pygame
from pygame.locals import *
from sys import exit
import random 
import ctypes
import win32gui
import win32con
import time

# randomizador


# Obter as dimensões da tela
user32 = ctypes.windll.user32
largura_monitor = user32.GetSystemMetrics(0)
altura_monitor = user32.GetSystemMetrics(1)



# Inicialização do pygame e definir as dimensões da janela sem a moldura
pygame.init()
tela = pygame.display.set_mode((largura_monitor, altura_monitor), pygame.NOFRAME,pygame.FULLSCREEN)

# Cor do Background da Tela
preto = (0,0,0)

# Definir a janela como superior no Windows
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

pygame.display.set_caption('Sprites')

class ClebinhoPiscas(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\PiscandoCapado\Piscando.png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\PiscandoCapado\Piscando2.png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\PiscandoCapado\Piscando5.png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\PiscandoCapado\Piscando8.png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\PiscandoCapado\Piscando11.png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\PiscandoCapado\Piscando13.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        
        #Aumentar o Sprite pras dimensões da tela
        self.screen_width = tela.get_width()
        self.screen_height = tela.get_height()

        #Modifica o Tamanho da imagem(Nesse exemplo, modificamos praficar do 
        #tamanho de toda a janela pygame)
        self.image = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))
        
        self.rect = self.image.get_rect()
        #Centraliza a imagem no centroda janela
        self.rect.center = (self.screen_width // 2, self.screen_height // 2)

    
    
    #Vai fazer a troca de frames, animando a imagem, fazendo a troca dinâmica
    def update(self):
        #troca de frames dinâmica
        #Ao adicionar mais 1, a animação de quadros 
        #começa, mais rápido demais, pra controlar essa velocidade, usaremos int() 
        # no código mais abaixo, pois, ao usar o self.atual como indice da animação,
        # ele só pode receber apresentar números inteiros.
        self.atual = self.atual + 0.5
        #Se self.atual chegar ao limite de frames da classe clebinho,
        # ela irá resetar para a primeira imagem, reiniciando a animação
        if self.atual >= len(self.sprites):
            self.atual = 0
            #Array com valores numerais
            WaitAnimation = [0,1,2,3,4,5]
            #Variavel que randomiza os valores da variavel "WaitAnimation"
            i = random.choice(WaitAnimation)
            #Usando a variavel "i" que randomiza o valor da WaitAnimation, ele cria
            #um espaço de tempo entre cada reinicio da animação
            time.sleep(i)

        #Int() vai sempre arrendondar o número quebrado como 0.5 ou 0.05 pra baixo,
        # logo, a mudança de frames só vai acontecer quando a soma desses números 
        # quebrados der 1,2,3 e por ai vai.
        self.image = self.sprites[int(self.atual)]
        #Modifica o Tamanho da imagem(Nesse exemplo, modificamos praficar do tamanho de toda a janela pygame)
        self.image = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))
class ClebinhoApaixonado(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (1).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (2).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (3).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (9).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (10).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (11).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (12).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (13).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (14).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (15).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (16).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (17).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (34).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (35).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (36).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (37).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (38).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\ApaixonadoCapado\Apaixonado (39).png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        
        self.screen_width = tela.get_width()
        self.screen_height = tela.get_height()

        self.image = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))
        
        self.rect = self.image.get_rect()
        
        self.rect.center = (self.screen_width // 2, self.screen_height // 2)
        self.animar = False
    def atacar(self):
     self.animar = True
    def update(self):
        if self.animar == True:
         
         self.atual = self.atual + 1
         
         if self.atual >= len(self.sprites):
             self.atual = 0
             self.animar = False

         
         self.image = self.sprites[int(self.atual)]
         self.image = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))

class ClebinhoIdentificar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\IdentificandoCapado\Identificando(0).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\IdentificandoCapado\Identificando(1).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\IdentificandoCapado\Identificando(2).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\IdentificandoCapado\Identificando(8).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\IdentificandoCapado\Identificando(9).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\IdentificandoCapado\Identificando(10).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\IdentificandoCapado\Identificando(11).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\IdentificandoCapado\Identificando(12).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\IdentificandoCapado\Identificando(13).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\IdentificandoCapado\Identificando(14).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\IdentificandoCapado\Identificando(15).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\IdentificandoCapado\Identificando(16).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\IdentificandoCapado\Identificando(17).png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        
        
        self.screen_width = tela.get_width()
        self.screen_height = tela.get_height()

        
        self.image = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))
        
        self.rect = self.image.get_rect()
       
        self.rect.center = (self.screen_width // 2, self.screen_height // 2)
        self.animar = False
    def atacar(self):
     self.animar = True
    def update(self):
        if self.animar == True:
         
         self.atual = self.atual + 1
         
         if self.atual >= len(self.sprites):
             self.atual = 0
             self.animar = False

         
         self.image = self.sprites[int(self.atual)]
         self.image = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))

class ClebinhoRaiva(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (1).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (2).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (3).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (18).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (19).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (20).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (21).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (22).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (23).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (24).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (25).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (26).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (27).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (28).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (29).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (30).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (31).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (32).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (33).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (34).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (35).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (36).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (37).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (38).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (39).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (40).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\RaivaCapado\Raiva (41).png'))
       
        self.atual = 0
        self.image = self.sprites[self.atual]
        
       
        self.screen_width = tela.get_width()
        self.screen_height = tela.get_height()

        
        self.image = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))
        
        self.rect = self.image.get_rect()
        self.rect.center = (self.screen_width // 2, self.screen_height // 2)
        self.animar = False
    def atacar(self):
     self.animar = True
    def update(self):
        if self.animar == True:
         
         self.atual = self.atual + 1
         
         if self.atual >= len(self.sprites):
             self.atual = 0
             self.animar = False

         
         self.image = self.sprites[int(self.atual)]
         self.image = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))

class ClebinhoTriste(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\TristeCapado\Triste (1).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\TristeCapado\Triste (2).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\TristeCapado\Triste (7).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\TristeCapado\Triste (8).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\TristeCapado\Triste (9).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\TristeCapado\Triste (10).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\TristeCapado\Triste (11).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\TristeCapado\Triste (12).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\TristeCapado\Triste (13).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\TristeCapado\Triste (14).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\TristeCapado\Triste (15).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\TristeCapado\Triste (16).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\TristeCapado\Triste (17).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\TristeCapado\Triste (18).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\TristeCapado\Triste (19).png'))
        self.sprites.append(pygame.image.load('Imagens_e_Vídeos\Frames\TristeCapado\Triste (20).png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        
        
        self.screen_width = tela.get_width()
        self.screen_height = tela.get_height()

        
        self.image = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))
        
        self.rect = self.image.get_rect()
        
        self.rect.center = (self.screen_width // 2, self.screen_height // 2)
        self.animar = False
    def atacar(self):
     self.animar = True
    
    def update(self):
        if self.animar == True:
         
         self.atual = self.atual + 1
         
         if self.atual >= len(self.sprites):
             self.atual = 0
             self.animar = False

         
         self.image = self.sprites[int(self.atual)]
         
         self.image = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))
     

todas_as_sprites = pygame.sprite.Group()
clebinho = ClebinhoPiscas()
todas_as_sprites.add(clebinho)

todas_as_sprites0 = pygame.sprite.Group()
clebinho0 = ClebinhoTriste()
todas_as_sprites0.add(clebinho0)

todas_as_sprites1 = pygame.sprite.Group()
clebinho1 = ClebinhoApaixonado()
todas_as_sprites1.add(clebinho1)

todas_as_sprites2 = pygame.sprite.Group()
clebinho2 = ClebinhoIdentificar()
todas_as_sprites2.add(clebinho2)

todas_as_sprites3 = pygame.sprite.Group()
clebinho3 = ClebinhoRaiva()
todas_as_sprites3.add(clebinho3)
     

#Variavel com o comando de Frames por Segundo
clock = pygame.time.Clock()

while True:
    clock.tick(30)
    tela.fill(preto)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == pygame.K_1:
             clebinho0.atacar()
             quantidade_frames = len(clebinho0.sprites)
             for i in range(quantidade_frames):
                 todas_as_sprites0.draw(tela)
                 todas_as_sprites0.update()
                 pygame.display.flip()
             time.sleep(0.5)
            if event.key == pygame.K_2:
             clebinho1.atacar()
             quantidade_frames = len(clebinho1.sprites)
             for i in range(quantidade_frames):
                 todas_as_sprites1.draw(tela)
                 todas_as_sprites1.update()
                 pygame.display.flip()
             time.sleep(0.5)
            if event.key == pygame.K_3:
             clebinho2.atacar()
             quantidade_frames = len(clebinho2.sprites)
             for i in range(quantidade_frames):
                 todas_as_sprites2.draw(tela)
                 todas_as_sprites2.update()
                 pygame.display.flip()
             time.sleep(0.5)
              
            if event.key == pygame.K_4:
             clebinho3.atacar()
             quantidade_frames = len(clebinho3.sprites)
             for i in range(quantidade_frames):
                 todas_as_sprites3.draw(tela)
                 todas_as_sprites3.update()
                 pygame.display.flip()
             time.sleep(0.5)
             
            
        
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()