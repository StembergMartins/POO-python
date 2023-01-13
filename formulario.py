class Caneta:

    def __init__(self, modelo, cor, ponta = float, carga = int, tampa = bool):
        self.modelo = modelo
        self.cor = cor
        self._ponta = ponta
        self.__carga = carga
        self.__tampa = tampa

    def escrever(self, frase):
        if self.tampa:
            print(f"Para escrever com a caneta {self.modelo} deverá está sem tampa! ")
            return
        print(f"A caneta de modelo {self.modelo} escreveu em {self.cor} a frase: {frase}")

    def rabiscar(self):
        None

    def pintar(self):
        None
    
    def _tampar(self):
        None
    
    def _destampar(self):
        None
