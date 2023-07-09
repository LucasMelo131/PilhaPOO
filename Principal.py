from Pilha import Pilha

class Principal:
  
    def __init__(self):
        self.__pilha1 = Pilha()
        self.__pilha2 = Pilha()

    def main(self):
        #self.__pilha1 = Pilha()
        self.__pilha2.big_push(1,2,3,5)
        self.__pilha1.pilha_push(self.__pilha2)
        #self.__pilha1.imprimir()
        #self.__pilha2.imprimir()

teste = Principal()
teste.main()
