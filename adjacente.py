class Adjacente: #criando a classe
    
    def __init__(self, cidade, distancia): #metodo construtor
       
        self.cidade = cidade #atributo
        self.distancia = distancia
        
        #f(n)= g(n) + h(n)
        self.distanciaAestrela = self.distancia + self.cidade.distanciaObjetivo