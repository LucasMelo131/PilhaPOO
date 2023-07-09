from Pilha import Pilha

class Principal:
  
    def __init__(self):
        self.__pilha1 = Pilha()
        self.__pilha2 = Pilha()

    def teste(self):
        self.__pilha1.push(10)
        self.__pilha1.big_push(20,30)
        #self.__pilha1.pop()
        #self.__pilha1.pop()
        self.__pilha1.big_pop(2)
        topo = self.__pilha1.top()
        print("O topo da pilha é :",topo)

    def outro_teste(self):
        self.__pilha2.big_push(1,2,3,4,5,6)
        print("O topo da pilha 2 é :",self.__pilha2.top())
        self.__pilha1.pilha_push(self.__pilha2)
        print("O topo da pilha 2 após o empilhamento é :",self.__pilha2.top())
        print("O topo da pilha 1 após o empilhamento é :",self.__pilha1.top())
        self.__pilha1.big_pop(3)
        print("O topo da pilha 1 após as remoções é:",self.__pilha1.top())
        self.__pilha1.big_pop(2)
        print("A pilha",self.__pilha1.top())


teste = Principal()
teste.teste()
print("------------------------------------------")
teste.outro_teste()
