class Pilha:

    #Construtor da classe pilha com os atributos privados
    def __init__(self):
        self.__TAM_MAX = 5
        self.__valores = []
        self.__topo = -1

    #Método que verifica se a pilha está vazia
    def vazia(self):
        return self.__topo == -1

    #Insere um valor no topo da pilha (retorna True caso consiga inserir)
    def push(self,valor):
        if self.__topo == self.__TAM_MAX - 1:
            return "Pilha cheia, o valor " + str(valor) + " não pode ser inserido"
        self.__valores.insert(0,valor)
        self.__topo += 1
        return None

    #Insere vários valores na pilha (um por um)
    def big_push(self,*valores):
        for valor in valores:
            if self.__topo == self.__TAM_MAX - 1:
                return "Pilha cheia, o valor " + str(valor) + " não pode ser inserido e nem os demais"
            self.__valores.insert(0,valor)
            self.__topo += 1
        return None

    #Empilhar uma pilha em outra (criamos uma cópia da pilha de origem
    #para respeitar o princípio de imutabilidade :) )

    def pilha_push(self,origem):
        #cria a copia de uma pilha p/ outra variavel
        def __copia(pilha):
            nova_pilha = Pilha()
            aux = []
            while not(pilha.vazia()):
                curr = pilha.pop()
                aux.insert(0,curr)
            for elem in aux:
                pilha.push(elem)
                nova_pilha.push(elem)
            return nova_pilha

        aux = __copia(origem)
        #empilha na pilha de destino
        while not aux.vazia():
            curr = aux.pop()
            if self.__topo == self.__TAM_MAX - 1:
                return "Pilha cheia, o valor " + str(curr) + " não pode ser inserido e nem os demais"
            self.__valores.insert(0,curr)
            self.__topo += 1
        return None

    #Remove o elemento do topo da pilha, se ela não estiver vazia
    def pop(self):
        if self.vazia():
            return "Nada para ser removido, a pilha está vazia"
        self.__topo -= 1
        removido = self.__valores.pop(0)
        return removido

    #Remove n elementos da pilha (especificado como parâmetro da função)
    #Se n > tam da pilha, esvazia a pilha
    def big_pop(self, quant):
        if self.vazia():
            return "Nada para ser removido"
        self.__valores = self.__valores[quant:]
        self.__topo -= quant
        if self.__topo < -1:
            self.__topo = -1

    #Retorna o topo da pilha
    def top(self):
        if self.vazia():
            return "está vazia"
        return self.__valores[0]
    
    def imprimir(self):
        print(self.__valores)
