from Pilha import Pilha

class Principal:
  
    def __init__(self):
        self.__pilha1 = Pilha()
        #self.__pilha2 = Pilha()

    def main(self):
        #self.__pilha1 = Pilha()
        self.__pilha1.big_push(1,2,3,5,7,8,9,10,11,19,20)
        self.__pilha1.imprimir()

teste = Principal()
teste.main()
