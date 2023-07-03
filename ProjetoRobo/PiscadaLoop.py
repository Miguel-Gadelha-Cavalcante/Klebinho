import pygame # pip install pygame --user
import cv2 # pip install opencv-python --user
import numpy as np # pip pip install numpy --user
import time 
import random 
import ctypes
import win32gui
import win32con
import threading

# Obter as dimensões da tela
user32 = ctypes.windll.user32
largura_monitor = user32.GetSystemMetrics(0)
altura_monitor = user32.GetSystemMetrics(1)

#Intervalos das piscadas
stopAnimation = [1,2,3,4,5]

# Inicialização do pygame e definir as dimensões da janela sem a moldura
pygame.init()
tela = pygame.display.set_mode((largura_monitor, altura_monitor), pygame.NOFRAME)

# Definir a janela como superior no Windows
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


# Caminho do arquivo de vídeo
caminho_video = 'Imagens_e_Vídeos/exemplo_de_sprites/Piscando.mp4'

# Função para converter o vídeo em sequência de imagens
def converter_video_para_sprites(caminho_video):
    sprites = []
    cap = cv2.VideoCapture(caminho_video)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Conversão do frame para sprite (imagem)
        sprite = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        sprite = np.rot90(sprite)
        sprite = pygame.surfarray.make_surface(sprite)
        sprite = pygame.transform.scale(sprite, (largura_monitor, altura_monitor))
        sprites.append(sprite)

    cap.release()

    return sprites

# Função para exibir animação de sprites
def exibir_animacao_thread(sprites):
    i = random.choice(stopAnimation)
    clock = pygame.time.Clock()
    for sprite in sprites:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        tela.blit(sprite, (0, 0))
        pygame.display.flip()
        clock.tick(250) #Velocidade da animação(+250 a velocidade é igual)

    time.sleep(i)  # Intervalo da animação

# Loop principal
if __name__ == "__main__":
    sprites = converter_video_para_sprites(caminho_video)
    while True:
        exibir_animacao_thread(sprites)
def reproduzir_video_com_sprites(caminho_video):
    
    user32 = ctypes.windll.user32
    largura_monitor = user32.GetSystemMetrics(0)
    altura_monitor = user32.GetSystemMetrics(1)
    
    stopAnimation = [1,2,3,4,5]
    
    pygame.init()
    tela = pygame.display.set_mode((largura_monitor, altura_monitor), pygame.NOFRAME)
    
    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    sprites = converter_video_para_sprites(caminho_video)

    #Cria e inicia a thread de animação
    animacao_thread = threading.Thread(target=exibir_animacao_thread, args=(sprites,))
    animacao_thread.start()


