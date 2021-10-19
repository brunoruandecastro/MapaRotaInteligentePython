class Pilha:
    def __init__(self): #construtor da classe
        #vetor de cidades
        self.cidades = []
        
    #metodo para empilhar adiciona uma cidade na pilha
    def empilhar (self, cidade):
        self.cidades.append(cidade)
        
    
    def desempilhar(self):
        if not Pilha.pilhaVazia(self): #verifica se a pilha não está vazia
            return self.cidades.pop (-1) #retorna a cidade tirada da pilha / os ultimos são os primeiros
        
        else:
            print("A pilha já está vazia.")
            return None
        
        
    def getTopo(self):
        return self.cidades[-1]
    
    def pilhaVazia (self):
        return len(self.cidades) == 0
    
    
# from mapa import Mapa

# mapa = Mapa()


# pilha = Pilha()

# pilha.empilhar(mapa.fozDoIguacu)
# pilha.empilhar(mapa.guarapuava)
# pilha.empilhar(mapa.irati)
# pilha.empilhar(mapa.cascavel)

# print ("Está no topo da pilha: ", pilha.getTopo().nome)

# print ("Desempilhando . . .")
# pilha.desempilhar()
# pilha.desempilhar()
# pilha.desempilhar()

# print("Está no topo da pilha, agora: ", pilha.getTopo().nome)