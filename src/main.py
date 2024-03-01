import pygame
import os

# Inicialização do Pygame
pygame.init()

# Configurações
largura_tela = 480
altura_tela = 720

# Inicialização da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Meu Jogo Pygame")

# Carregando imagens
caminho_imagens = os.path.join("assets\img")
jogador_imagem = pygame.image.load(os.path.join(caminho_imagens, "steve.png"))
fundo_imagem = pygame.image.load(os.path.join(caminho_imagens, "sala.jpeg"))
phone_image_front = pygame.image.load(os.path.join(caminho_imagens, "phone-front.png"))

icon_red_image = pygame.image.load(os.path.join(caminho_imagens, "icon_red.png"))
icon_green_image = pygame.image.load(os.path.join(caminho_imagens, "icon_green.png"))

# Carregando música de fundo
pygame.mixer.music.load(os.path.join("assets/audio", "musica_fundo.mp3"))
pygame.mixer.music.play(-1)  # -1 para loop infinito

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Lógica do jogo e desenho na tela aqui

    # Atualização da tela
    tela.blit(fundo_imagem, (0, 0))
    tela.blit(jogador_imagem, (largura_tela // 2 - jogador_imagem.get_width() // 2,
                                altura_tela // 2 - jogador_imagem.get_height() // 2))
    tela.blit(phone_image_front, (350, 450))
    tela.blit(icon_red_image, (220, 600))
    tela.blit(icon_green_image, (70, 600))

    pygame.display.flip()

# Finalização do Pygame
pygame.quit()
