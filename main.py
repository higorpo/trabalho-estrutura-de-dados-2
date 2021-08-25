from nodo import Nodo

raiz = Nodo(15)
raiz.add(17)
raiz.add(19)
raiz.add(12)
raiz.add(26)
raiz.add(25)
raiz.add(33)
raiz.add(35)
raiz.add(38)


print(raiz.remover(33))
# print(raiz.remover(25))

# raiz.add(27)

raiz.printThree()
