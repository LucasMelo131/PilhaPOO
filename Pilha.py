from copy import deepcopy

class Pilha:

    #Construtor da classe pilha com os atributos privados
    def __init__(self):
        self.__TAM_MAX = 10
        self.__valores = []
        self.__topo = -1

    #Método que verifica se a pilha está vazia
    def empty(self):
        return self.__topo == -1
    
    #Insere um valor no topo da pilha (retorna True caso consiga inserir)
    def push(self,valor):
        if (len(self.__valores) == self.__TAM_MAX):
            return "Pilha cheia, o valor " + str(valor) + " não pode ser inserido"
        self.__valores.insert(0,valor)
        self.__topo += 1
        #print("O valor",valor,"foi inserido!")
        return True

    #Insere vários valores na pilha (um por um)
    def big_push(self,*valores):
        for valor in valores:
            encheu = self.push(valor)
            if encheu is not True:
                print("O valor",valor,"não pode ser inserido e nem os posteriores")
                break
    
    #Remove o elemento do topo da pilha, se ela não estiver vazia
    def pop(self):
        if self.empty():
            return "Nada para ser removido, a pilha está vazia"
        self.__topo -= 1
        removido = self.__valores.pop(0)
        return removido
    
    #Remove n elementos da pilha (especificado como parâmetro da função)
    #Se n > tam da pilha, esvazia a pilha
    def big_pop(self, quant):
        if self.empty():
            return "Nada para ser removido"
        self.__valores = self.__valores[quant:]
        self.__topo -= quant
        if self.__topo < -1:
            self.__topo = -1
    
    #Retorna o topo da pilha
    def top(self):
        return self.__valores[0]
    
    def imprimir(self):
        print(self.__valores)