from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} está comendo e não pode falar!')
            return
        if self.falando:
            print(f'{self.nome} já está falando sobre algo!')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if self.falando:
            print(f"{self.nome} encerrou sua fala!")
            self.falando = False
            return


    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} ja está comendo!')
            return

        if self.falando:
            print (f'{self.nome} está falando, não pode comer agora!')
            return
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não esta comendo")
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade




