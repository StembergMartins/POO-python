class Caneta:

    def __init__(self, modelo, cor, ponta = float, carga = int, tampa = bool):
        self.modelo = modelo
        self.cor = cor
        self.ponta = ponta
        self.carga = carga
        self.tampa = tampa

    def escrever(self, frase):
        if self.tampa:
            print(f"Para escrever com a caneta {self.modelo} deverá está sem tampa! ")
            return
        print(f"A caneta de modelo {self.modelo} escreveu em {self.cor} a frase: {frase}")

    def remover_tampa(self):
        if not self.tampa:
            print("A caneta já está sem tampa!!! ")
            return
        self.tampa = False
        print("A tampa da caneta foi removida")
