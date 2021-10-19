from vetorOrdenado import VetorOrdenado


class Gulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False
        
    def buscar(self, atual): #cidade atual como parametro
    
        print ("\nAtual: %s" % (atual.nome))
        atual.vistiado = True
        
        if atual == self.objetivo:
            self.achou = True 
            print ("\n Chegamos no objetivo!")
            
        else:
            self.fronteira = VetorOrdenado()
            
            for adjacente in atual.adjacente:
                
                if adjacente.cidade.visitado == False:
                    adjacente.cidade.visitado == True #marcado como visitado
                    self.fronteira.inserir(adjacente) #adiciono adjacente ao vetor
                    
            self.fronteira.mostrar()
            
            if self.fronteira.getPrimeiro() != None: #se nao estiver vazio
            
            #chama a nova cidade a ser expandida
                Gulosa.buscar(self, self.fronteira.getPrimeiro())

from mapa import Mapa
mapa = Mapa()

gulosa = Gulosa(mapa.curitiba)
gulosa.buscar(mapa.fozDoIguacu)
                
            
                
        