from multimethod import overload #Usar o comando pip install multimethod no terminal

class Pilha:

    #Construtor da classe pilha com os atributos privados
    def __init__(self):
        self.__TAM_MAX = 10
        self.__valores = []
        self.__topo = -1

    #Método que verifica se a pilha está vazia
    def empty(self):
        return self.__topo == -1

    #Insere um valor no topo da pilha 
    @overload
    def push(self, valor):
        if self.__topo == self.__TAM_MAX - 1:
            return None
        self.__valores.insert(0, valor)
        self.__topo += 1
        return None

    #Insere vários valores na pilha (um por um)
    @overload
    def push(self,*valores):
        for valor in valores:
            if self.__topo == self.__TAM_MAX - 1:
                return None
            self.__valores.insert(0, valor)
            self.__topo += 1
        return None
    
    #Empilhar uma pilha em outra (criamos uma cópia da pilha de origem
    #para respeitar o princípio de imutabilidade :) )

    def pilha_push(self,origem):
        #cria a copia de uma pilha p/ outra variavel
         def __copia(pilha):
            nova_pilha = Pilha()
            temp = []
            while not(pilha.empty()):
                curr = pilha.pop()
                temp.insert(0,curr)
            for elem in temp:
                pilha.push(elem)
                nova_pilha.push(elem)
            return nova_pilha

         aux = __copia(origem)
        #empilha na pilha de destino
         while not aux.empty():
            if self.__topo == self.__TAM_MAX - 1:
                return None
            curr = aux.pop()
            self.__valores.insert(0, curr)
            self.__topo += 1
         return None

    #Remove o elemento do topo da pilha, se ela não estiver vazia
    @overload
    def pop(self):
        if self.empty():
            return None
        self.__topo -= 1
        removido = self.__valores.pop(0)
        return removido

    #Remove n elementos da pilha (especificado como parâmetro da função)
    #Se n > tam da pilha, esvazia a pilha
    @overload
    def pop(self,quant):
        if self.empty():
            return None
        self.__valores = self.__valores[quant:]
        self.__topo -= quant
        if self.__topo < -1:
            self.__topo = -1
        return None

    #Retorna o topo da pilha
    def top(self):
        if self.empty():
            return "Vazio"
        return self.__valores[0]