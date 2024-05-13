# Inicialização do Pygame
import random
import time
import pygame
import os
from classes.reproduzir import GravadorAudio
import pyttsx3

def texto_para_audio(texto):
    engine = pyttsx3.init()

    engine.setProperty('rate', 150)  

    engine.setProperty('voice', 'pt-br') 

    engine.say(texto)

    engine.runAndWait()
    
GravadorAudio

pygame.init()

# Configurações
largura_tela = 480
altura_tela = 720

# Inicialização da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Meu Jogo Pygame")

# Carregando imagens
caminho_imagens = os.path.join("assets", "img")
steve_imagem = pygame.image.load(os.path.join(caminho_imagens, "steve.png"))
steve_imagem_phone = pygame.image.load(os.path.join(caminho_imagens, "steve_phone.png"))
fundo_imagem = pygame.image.load(os.path.join(caminho_imagens, "sala.jpeg"))
phone_image_front = pygame.image.load(os.path.join(caminho_imagens, "phone-front.png"))
icon_green_image = pygame.image.load(os.path.join(caminho_imagens, "icon_green.png"))
boca_aberta_imagem = pygame.image.load(os.path.join(caminho_imagens, "boca_aberta.png"))

# Carregando música de fundo e audios
pygame.mixer.music.load(os.path.join("assets", "audio", "musica_fundo.mp3"))
pygame.mixer.music.play(-1)  # -1 para loop infinito
pygame.mixer.music.set_volume(0.05)  # Configurando o volume da música para 50%

steve_speak = pygame.mixer.Sound(os.path.join("assets", "audio", "song_steve.mp3"))
chamada_phone = pygame.mixer.Sound(os.path.join("assets", "audio", "chamada.mp3"))
ligacao = pygame.mixer.Sound(os.path.join("assets", "audio", "ligacao.mp3"))
encerramento = pygame.mixer.Sound(os.path.join("assets", "audio", "encerrando.mp3"))
# Variáveis de controle
atendendo = False
gravador = None  # Inicialização do gravador de áudio

# Posições e retângulos dos ícones
icon_green_pos = (200, 600)
icon_green_rect = icon_green_image.get_rect(topleft=icon_green_pos)

# Posição do Steve na tela
steve_pos = (160, 200)
steve_phone_pos = (100, 210)

falar = True

velocidade_falar = 0.5
# Loop principal
rodando = True
while rodando:
    # Atualização da tela

    tela.blit(steve_imagem_phone, steve_phone_pos)
    tela.blit(boca_aberta_imagem, steve_phone_pos)

    tela.blit(fundo_imagem, (0, 0))

    if atendendo:

        pygame.mixer.music.set_volume(0.01)
        tela.blit(steve_imagem_phone, steve_phone_pos)

        if gravador is None:

            gravador = GravadorAudio()
            gravador.iniciar_gravacao()
        else:
            gravador.gravar_frame()
    else:
        if gravador is not None:
            steve_speak.play()
            time.sleep(1)
            gravador.encerrar()
            gravador = None
            pygame.mixer.music.set_volume(0.05)

        tela.blit(steve_imagem, steve_pos)

        tela.blit(phone_image_front, (350, 450))  # Desenha o telefone

    tela.blit(icon_green_image, icon_green_pos)
    
    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Verifica se o botão pressionado é o botão esquerdo do mouse
                if icon_green_rect.collidepoint(evento.pos):

                    if random.choice([False, False]):
                        ligacao.play()

                        time.sleep(5)
                        atendendo = True
                        
                    else:
                        texto_para_audio('não vou atender!')
                        
                        encerramento.play()

        elif evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:  # Verifica se o botão solto é o botão esquerdo do mouse
                atendendo = False

    # Lógica do jogo e desenho na tela aqui
    pygame.display.flip()

# Finalização do Pygame
pygame.quit()
