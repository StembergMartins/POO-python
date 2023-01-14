class Caneta:

    def __init__(self, modelo = str, cor = str, ponta = float, carga = int, tampa = bool):
        self.modelo = modelo
        self.cor = cor
        self._ponta = ponta
        self.__carga = carga
        self.__tampa = tampa

    def escrever(self, texto):
        if self.__tampa:
            print("Error: Para escrever destampar a caneta! ")
            return
        elif self.__carga < 1:
            print("Error: Tinta insuficiente para escrever! ")
            return
            
        print(f"Caneta escreveu: {texto}")      

    def rabiscar(self):
        if self.__tampa:
            print("Error: Para rabiscar destampar a caneta! ")
            return
            
        print(f"Caneta rabiscou: qualquer coisa! ")

    def pintar(self):
        None
    
    def _tampar(self):
        if self.__tampa:
            print("Error: Caneta já tampada! ")
            return

        self.__tampa = True
        print("caneta tampada! ")
    
    def _destampar(self):
        if  not self.__tampa:
            print("Error: Caneta já destampada! ")
            return

        self.__tampa = False
        print("Caneta destampada! ")
