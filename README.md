# TalkingCraft

Jogo interativo feito em **Python** com **Pygame**. O jogador interage com o personagem **Steve**, atendendo ou recusando ligações. O jogo usa **gTTS** para converter texto em fala e **PyAudio** para gravação de áudio.

## Funcionalidades

- Interação com o personagem Steve
- Gravação e reprodução de áudio
- Texto para fala com **gTTS**
- Música de fundo ambiente

## Tecnologias

- **Pygame**: Para a criação do jogo.
- **gTTS**: Para gerar fala a partir de texto.
- **PyAudio**: Para gravação e reprodução de áudio.

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/meu-jogo-pygame.git
    cd meu-jogo-pygame
    ```

2. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/Mac
    venv\Scripts\activate     # No Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Execute o jogo:

    ```bash
    python main.py
    ```

## Como Jogar

1. Clique no ícone verde para tentar atender a ligação.
2. Se atender, Steve gravará e reproduzirá um áudio.
3. Se não atender, Steve dirá *"não vou atender!"*.

## Licença

Este projeto está licenciado sob a **MIT License**.
