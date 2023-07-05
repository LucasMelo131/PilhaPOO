from Pilha import Pilha

class Principal:

    #pilha1 = []

    def main(self):
        self.pilha1 = Pilha()
        self.pilha2 = Pilha()
        
        self.pilha1.push(1)
        self.pilha1.varios_push(2, 3, 4, 5, 6, 7)
        self.pilha1.imprimir()
        self.pilha1.varios_pop(3)
        self.pilha1.imprimir()


teste = Principal()
teste.main()