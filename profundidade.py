from pilha import Pilha

class Profundidade:
    #construtor da classe / Cidade de inicio e cidade objetivo
    def __init__(self,inicio, objetivo):
        
        #atributos
        self.inicio = inicio
        self.inicio.visitado = True #marcada como visitada
        
        self.objetivo = objetivo
        
        self.fronteira = Pilha() #armazena as cidades ao redor
        self.fronteira.empilhar (inicio) #impilha as cidades de inicio
        
        self.achou = False
        
    
    def buscar (self):
        #busca a cidade do topo da pilha
        topo = self.fronteira.getTopo()
        print ("\nTopo da pilha: ", topo.nome)
        
        if topo == self.objetivo: #verifica se é a cidade objetivo
            self.achou = True
            
        else: #se não achou executa a busca
            for adjacente in topo.adjacente:
                if self.achou == False :
                    print("Já foi visitado?", adjacente.cidade.nome)
                    
                    if adjacente.cidade.visitado == False:
                        #marca como visitada
                        adjacente.cidade.visitado = True
                        #empilha a cidade
                        self.fronteira.empilhar(adjacente.cidade)
                        
                        #chama novamente o método buscar
                        Profundidade.buscar(self)
                        
    #após encontrar a cidade objetivo, desempilha todas
        print ("Desempilhou: ", self.fronteira.desempilhar().nome)
    
from mapa import Mapa

mapa = Mapa()
profundidade = Profundidade(mapa.fozDoIguacu, mapa.curitiba)

profundidade.buscar()
    
    
                        
        
        
        

















