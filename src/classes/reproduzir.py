import pyaudio

class GravadorAudio:
    def __init__(self, taxa_amostragem=44100, chunk=1024, formato=pyaudio.paInt16, canais=1):
        self.taxa_amostragem = taxa_amostragem
        self.chunk = chunk
        self.formato = formato
        self.canais = canais
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.gravando = False

    def iniciar_gravacao(self):
        if not self.gravando:
            self.stream = self.p.open(format=self.formato,
                                      channels=self.canais,
                                      rate=self.taxa_amostragem,
                                      input=True,
                                      frames_per_buffer=self.chunk)
            print("Gravando...")
            self.gravando = True

    def gravar_frame(self):
        if self.gravando:
            dados = self.stream.read(self.chunk)
            self.frames.append(dados)

    def encerrar(self):
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()
        print("Gravação concluída.")

    def reproduzir(self):
        audio_gravado = b''.join(self.frames)
        # Inicializa uma nova instância PyAudio
        p = pyaudio.PyAudio()

        # Abre um novo stream de áudio para reprodução
        stream = p.open(format=p.get_format_from_width(2),
                        channels=1,
                        rate=self.taxa_amostragem,
                        output=True)

        print("Reproduzindo...")

        # Escreve os dados do áudio gravado no stream de reprodução
        stream.write(audio_gravado)

        print("Reprodução concluída.")

        # Encerra o stream de reprodução e termina a interface PyAudio
        stream.stop_stream()
        stream.close()
        p.terminate()

# Exemplo de uso
if __name__ == "__main__":
    gravador = GravadorAudio()
    gravador.iniciar_gravacao()
    # Simule a gravação de alguns frames
    for _ in range(10):
        gravador.gravar_frame()
    gravador.encerrar()
    gravador.reproduzir()
