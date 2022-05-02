class Computador:

    def __init__(self, processador, memoria_ram, placa_de_video, ligado=False):
        self.processador = processador
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
        self.ligado = ligado

    def ligar(self):
        if self.ligado == False:
            print('O computador ligou!')
            self.ligado = True
        elif self.ligado == True:
            print('O computador já esta ligado!')

    def desligar(self):
        if self.ligado == True:
            print('O computador desligou!')
            self.ligado = False
        elif self.ligado == False:
            print('O computador já está desligado!')

    def mostrar_config(self):
        print("----------------------------------------------------------------")
        print("O computador possui as seguintes configurações:")
        print(f"Processador: {self.processador}")
        print(f"Capacidade de Memória Ram: {self.memoria_ram}")
        print(f"Placa de Vídeo: {self.placa_de_video}")
        print("----------------------------------------------------------------")
