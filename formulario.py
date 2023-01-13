class Caneta:

    def __init__(self, modelo = str, cor = str, ponta = float, carga = int, tampa = bool):
        self.modelo = modelo
        self.cor = cor
        self._ponta = ponta
        self.__carga = carga
        self.__tampa = tampa

    def escrever(self, frase):
        None

    def rabiscar(self):
        None

    def pintar(self):
        None
    
    def _tampar(self):
        None
    
    def _destampar(self):
        None
