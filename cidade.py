class Cidade: #criando classe
    def __init__(self, nome, distanciaObjetivo): #construtor da classe
        #atributos da classe
        self.nome = nome
        self.visitado = False
        self.adjacente = [] #lista das cidades relacionadas
        self.distanciaObjetivo = distanciaObjetivo
        
    #metodo para adicionar cidades adjacentes 
    def addCidadeAdjacente(self, cidade):
        
        self.adjacente.append(cidade)
            
#testando
#cidade = Cidade("Paranavaí")

#print (cidade.nome)
#print (cidade.visitado)
            
        


