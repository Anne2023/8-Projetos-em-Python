# Projeto 3  - Chute um número
# Objetivo: Criar um algorítimo que gera um valor aleatório e eu tenho que ficar tentando o número até eu acertar
import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = False
    
    def Iniciar(self):
        layout = [
            [sg.Text('Seu Chute', size=(39,0))],
            [sg.Input(size=(18,0), key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(39,10))]
        ]
        self.janela = sg.Window('Chute o número', layout=layout)
        self.GerarNumeroAleatorio()
        
        while True:
            self.evento, self.valores = self.janela.Read()
            
            if self.evento == sg.WINDOW_CLOSED:
                break
                
            self.valor_do_chute = int(self.valores['ValorChute'])
            
            if self.valor_do_chute > self.valor_aleatorio:
                print('Chute um valor mais baixo!')
            elif self.valor_do_chute < self.valor_aleatorio:
                print('Chute um valor mais alto!')
            else:
                print('PARABÉNS VOCÊ ACERTOU!')
                break
                
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()
