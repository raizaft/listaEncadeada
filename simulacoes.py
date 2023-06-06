from listaEncadeada import Lista
import random

def concatena(l1,l2):
    l = Lista()
    for i in range(l1.tamanho()):
        carga = (l1.removeInicio())
        l.insereFim(carga)
    for i in range(l2.tamanho()):
        carga = (l2.removeInicio())
        l.insereFim(carga)
    return l

def inverso(l1,l2):
    for i in range(l2.tamanho()):
        carga = (l2.removeInicio())
        l1.insereInicio(carga)
    return l1

l1 = Lista()
# l2 = Lista()
# l3 = Lista()
# l4 = Lista()

for i in range(10):
    l1.insereFim(random.randint(1, 50))

# for i in range(15):
#     l2.insereFim(random.randint(1, 50))

print(l1)
# print(l2)

# l3 = concatena(l1,l2)
# l3.insereFim(1)
# l3.insereFim(2)
# l3.insereFim(3)
# l3.insereFim(4)
# print(l3)

# inverso(l4,l3)
# print(l4)

print(l1.maiores(15))