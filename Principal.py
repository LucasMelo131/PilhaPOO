from Pilha import Pilha

class Principal:

    def main(self):
        self.pilha1 = Pilha()
        
        self.pilha1.varios_push(10, 20, 30)
        self.pilha1.imprimir()
        self.pilha1.varios_pop(2)
        print(self.pilha1.top())


teste = Principal()
teste.main()