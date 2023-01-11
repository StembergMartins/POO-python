class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} ainda está comendo!")
            return
        elif self.falando:
            print("pare de falar para comer")
            return 

        print(f"{self.nome} está comendo {alimento}.")
        self.comendo = True
    
    def parar_comer(self):
        if not self.comendo:
            print(f"É precisso que o {self.nome} coma alguma coisa para para de comer!")
            return

        self.comendo = False
        print(f"{self.nome} parou de comer!")
        
        

    def falar(self, texto):
        if self.comendo:
            print("pare de comer para falar!")
            return

        elif self.falando:
            print("não da para falar doi assunstos ao mesmo tempo!")
            return

        self.falando = True
        print(f"{self.nome} está dizendo {texto}")

    def parar_falar(self):
        if not self.falando:
            print("é precisso falar para terminas uma conversa!")
            return

        self.falando = False
        print(f"{self.nome} parou de falar!")



