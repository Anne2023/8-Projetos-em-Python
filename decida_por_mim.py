# Decida por mim
# Faça uma pergunta para o programa e ele terá que  te dar uma resposta
import random


class DecidaPorMIm:
    def __init___(self):
        self.resposta = [
            'Com certeza, você deve fazer isso!'
            'Não sei, você que sabe!'
            'Nãofaz isso não!'
            'Achoque esta na hora certa1'
        ]

    def Iniciar(self):
        input ("Faça sua pergunta:   ")
        print (random.choice(self.resposta))

decida = DecidaPorMIm()
decida.Iniciar()        