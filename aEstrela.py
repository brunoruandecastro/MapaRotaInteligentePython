from vetorOrdenado import VetorOrdenado

class Aestrela:
    
    def __init__(self, objetivo):
        
        self.objetivo = objetivo
        self.achou = False
        
    def buscar(self, atual):
        print("\nAtual %s" % (atual.nome))
        atual.visitado = True
        
        if atual == self.objetivo:
            self.achou = True
            print("\nObjetivo encontrado!")
        else:
            self.fronteira = VetorOrdenado()
     
            #percorre as cidades
            for adjacente in atual.adjacente:
                if adjacente.cidade.visitado == False:
                    adjacente.cidade.visitado == True
                    #adiciono o adjacente ao vetor
                    self.fronteira.inserir(adjacente)
                    
                    
            self.fronteira.mostrar()
            
            if self.fronteira.getPrimeiro() != None:
                Aestrela.buscar(self, self.fronteira.getPrimeiro())
                
from mapa import Mapa
mapa = Mapa()

aestrela = Aestrela(mapa.curitiba)
aestrela.buscar (mapa.fozDoIguacu)
                
                
            