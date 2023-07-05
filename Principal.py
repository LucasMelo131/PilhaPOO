from Pilha import Pilha

class Principal:

    #pilha1 = []

    def main(self):
        self.pilha1 = Pilha()
        self.pilha2 = Pilha()
        
        self.pilha1.push({"Joao": 1})
        print(self.pilha1.top())
        self.pilha1.push({"José": 2,"Maria": 3})
        #self.pilha1.push("Maria")
        self.pilha2.varios_push({"José": 2,"Maria": 3},{"Joao": 1})
        self.pilha1.push_pilha(self.pilha2)
        print(self.pilha1.top())
        self.pilha1.imprimir()


teste = Principal()
teste.main()