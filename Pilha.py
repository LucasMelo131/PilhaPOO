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
        if len(self.__valores) == self.__TAM_MAX:
            return "Pilha cheia, o valor " + str(valor) + " não pode ser inserido"
        self.__valores.insert(0,valor)
        self.__topo += 1
        return True

    #Insere vários valores na pilha (um por um)
    def big_push(self,*valores):
        for valor in valores:
            nao_encheu = self.push(valor)
            if nao_encheu is not True:
                print("O valor",valor,"não pode ser inserido e nem os posteriores")
                break

    #Empilhar uma pilha em outra (criamos uma cópia da pilha de origem
    #para respeitar o princípio de imutabilidade :) )

    def pilha_push(self,origem):
        #cria a copia de uma pilha p/ outra variavel
        def __copia(pilha):
            new_pilha = Pilha()
            temp = []
            while not pilha.empty():
                elem = pilha.pop()
                temp.append(elem)
            for obj in temp:
                new_pilha.push(obj)
            del temp
            return new_pilha
        aux = __copia(origem)
        #empilha na pilha de destino
        while not aux.empty():
            curr = aux.pop()
            nao_encheu = self.push(curr)
            if nao_encheu is not True:
                print("O valor",curr,"não pode ser inserido e nem os posteriores")
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
