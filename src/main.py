# Inicialização do Pygame
import io
import random
import time
from gtts import gTTS
import pygame
import os
from classes.reproduzir import GravadorAudio

def texto_para_audio(texto):
    try:
        # Convertendo texto em fala com Google Text-to-Speech (gTTS)
        tts = gTTS(text=texto, lang='pt')
        
        # Usando um buffer de memória (sem salvar o arquivo)
        fp = io.BytesIO()
        tts.save(fp)
        fp.seek(0)

        # Inicializando o mixer do pygame
        pygame.mixer.init()
        
        # Carregando o áudio e tocando
        pygame.mixer.music.load(fp)
        pygame.mixer.music.play()

        # Aguarda até que a música termine para o programa não fechar imediatamente
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    
    except Exception as e:
        print(f"Erro ao usar gTTS: {e}")
        
        
pygame.init()

# Configurações
largura_tela = 480
altura_tela = 720

# Inicialização da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Meu Jogo Pygame")

# Carregando imagens
caminho_imagens = os.path.join("assets", "img")
steve_imagem = pygame.image.load(r'talkingCraft\assets\img\steve.png')
steve_imagem_phone = pygame.image.load(r'talkingCraft\assets\img\steve_phone.png')
fundo_imagem = pygame.image.load(r'talkingCraft\assets\img\sala.jpeg')
phone_image_front = pygame.image.load(r'talkingCraft\assets\img\phone-front.png')
icon_green_image = pygame.image.load(r'talkingCraft\assets\img\icon_green.png')
boca_aberta_imagem = pygame.image.load(r'talkingCraft\assets\img\boca_aberta.png')

# Carregando música de fundo e audios
pygame.mixer.music.load(r'talkingCraft\assets\audio\musica_fundo.mp3')
pygame.mixer.music.play(-1)  # -1 para loop infinito
pygame.mixer.music.set_volume(0.05)  # Configurando o volume da música para 50%

steve_speak = pygame.mixer.Sound(r'talkingCraft\assets\audio\song_steve.mp3')
chamada_phone = pygame.mixer.Sound(r'talkingCraft\assets\audio\chamada.mp3')
ligacao = pygame.mixer.Sound(r'talkingCraft\assets\audio\ligacao.mp3')
encerramento = pygame.mixer.Sound(r'talkingCraft\assets\audio\encerrando.mp3')
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
            # gravador.reproduzir() repetir fala do audio gravado
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

                    if random.choice([True, False]):
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
