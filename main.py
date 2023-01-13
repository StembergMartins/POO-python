from pessoa import Pessoa
import os
from formulario import Caneta
os.system("cls")

p1 = Pessoa("stemberg", 28)
c1 = Caneta("Bic", "Azul", 0.5, 80, 1)

c1.escrever("olá mundo em POO!")


print(vars(c1))