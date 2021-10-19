from operator import attrgetter

#criando classe do vetor
class VetorOrdenado:
    def __init__(self): 
        
        
        self.adjacentes = []
        
    def inserir (self, adjacente):
        
        self.adjacentes.append(adjacente)
        self.adjacentes.sort(key=attrgetter("distanciaAestrela")) #realiza a ordenação do vetor de acordo com a distancia do objetivo
        
    
    def getPrimeiro(self):
        return self.adjacentes[0].cidade #buscar a cidade de menor custo
    
    def mostrar(self):
        #percorre as cidades do vetor
        for adjacente in self.adjacentes:
            
            print("Cidade: %s - Distancia: %s" % (adjacente.cidade.nome, adjacente.distanciaAestrela))
            
# from mapa import Mapa
# from adjacente import Adjacente
# mapa = Mapa()

# vetor = vetorOrdenado()
# vetor.inserir(Adjacente(mapa.guarapuava))
# vetor.inserir(Adjacente(mapa.pontaGrossa))
# vetor.inserir(Adjacente(mapa.patoBranco))

# vetor.mostrar()

# print ("Pirmeira cidade do vetor: ", vetor.getPrimeiro().nome)
            
        
        
        
        
        
        