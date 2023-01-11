from pessoa import Pessoa
import os
os.system("cls")

p1 = Pessoa("stemberg", 28)

p1.comer("lasanha")
p1.comer("chocolate")
p1.parar_comer()
p1.comer("chocolate")
p1.parar_comer()
print("1")
p1.parar_comer()
print("2")
p1.falar("olá mundo")
p1.comer("churrasco")
p1.falar("boa tarde")
print()
p1.parar_comer()
p1.falar("vamos a praia!")
p1.parar_falar()
p1.falar("vamos para churrascaria!")