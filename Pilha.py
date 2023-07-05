class Pilha:

    def __init__(self):
        self.__TAM_MAX = 10
        self.__valores = []
        self.__topo = -1

    def empty(self):
        return self.__topo == -1
    
    def push(self,valor):
        if (len(self.__valores) == self.__TAM_MAX):
            print("A pilha está cheia!!")
            return False
        self.__valores.insert(0,valor)
        self.__topo += 1
        #print("O valor",valor,"foi inserido!")
        return True
        
    def varios_push(self,*valores):
        for valor in valores:
            encheu = self.push(valor)
            if encheu is False:
                print("O valor",valor,"não pode ser inserido e nem os posteriores")
                break
    
    def push_pilha(self,pilha):
        for valor in pilha.__valores:
            encheu = self.push(valor)
            if encheu is False:
                print("O valor",valor,"não pode ser inserido e nem os posteriores")
                break
    
    def top(self):
        return self.__valores[0]
    
    def imprimir(self): 
        print(self.__valores)
        
    def pop(self):
        if self.__topo == -1:
            print("Não existem valores para serem removidos")
        else:
            self.__topo -= 1
            removido = self.__valores.pop(0)
            return removido
        
    def varios_pop(self, quant):
        self.__valores = self.__valores[quant:]
        print("Valores removidos com sucesso")
                  
    

        