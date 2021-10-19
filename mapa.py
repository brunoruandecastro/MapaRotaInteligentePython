from cidade import Cidade #importando a classe Cidade
from adjacente import Adjacente #importando a classe Adjacente

class Mapa: #criando a classe Mapa

    #criando cada uma das classes
    fozDoIguacu = Cidade ("Foz do Iguaçu", 534)
    cascavel = Cidade ("Cascavel", 424)
    patoBranco = Cidade ("Pato Branco", 351)
    campoMourao = Cidade ("Campo Mourão", 350)
    maringa = Cidade ("Maringá", 350)
    londrina = Cidade ("Londrina", 303)
    guarapuava = Cidade ("Guarapuava", 219)
    pontaGrossa = Cidade ("Ponta Grossa", 97)
    irati = Cidade ("Irati", 138)
    uniaoDaVitoria = Cidade ("União da Vitoria", 202)
    curitiba = Cidade ("Curitiba", 0)
    
    #Criando as ligações entre as classes (ida e volta)
    
    fozDoIguacu.addCidadeAdjacente(Adjacente(cascavel, 144)) #criando um objeto da classe adjacente
    fozDoIguacu.addCidadeAdjacente(Adjacente(patoBranco, 337))
    
    cascavel.addCidadeAdjacente(Adjacente(fozDoIguacu, 146))
    cascavel.addCidadeAdjacente(Adjacente(campoMourao, 172))
    cascavel.addCidadeAdjacente(Adjacente(uniaoDaVitoria, 408))
    cascavel.addCidadeAdjacente(Adjacente(guarapuava, 242))
    
    patoBranco.addCidadeAdjacente(Adjacente(fozDoIguacu, 337))
    patoBranco.addCidadeAdjacente(Adjacente(guarapuava, 188))
    
    campoMourao.addCidadeAdjacente(Adjacente(cascavel, 179))
    campoMourao.addCidadeAdjacente(Adjacente(maringa, 97))
    campoMourao.addCidadeAdjacente(Adjacente(guarapuava, 206))

    maringa.addCidadeAdjacente(Adjacente(campoMourao, 96))
    maringa.addCidadeAdjacente(Adjacente(londrina, 112))
    
    londrina.addCidadeAdjacente(Adjacente(maringa, 118))
    londrina.addCidadeAdjacente(Adjacente(guarapuava, 319))
    londrina.addCidadeAdjacente(Adjacente(pontaGrossa, 290))

    pontaGrossa.addCidadeAdjacente(Adjacente(londrina, 290))
    pontaGrossa.addCidadeAdjacente(Adjacente(guarapuava, 163))
    pontaGrossa.addCidadeAdjacente(Adjacente(curitiba, 117))
    
    guarapuava.addCidadeAdjacente(Adjacente(pontaGrossa, 163))
    guarapuava.addCidadeAdjacente(Adjacente(campoMourao, 206))
    guarapuava.addCidadeAdjacente(Adjacente(londrina, 319))
    guarapuava.addCidadeAdjacente(Adjacente(cascavel, 242))
    guarapuava.addCidadeAdjacente(Adjacente(irati, 104))
    guarapuava.addCidadeAdjacente(Adjacente(patoBranco, 188))
    
    curitiba.addCidadeAdjacente(Adjacente(pontaGrossa, 115))
    curitiba.addCidadeAdjacente(Adjacente(irati, 156))
    curitiba.addCidadeAdjacente(Adjacente(uniaoDaVitoria, 241))
    
    
    irati.addCidadeAdjacente(Adjacente(curitiba, 146))
    irati.addCidadeAdjacente(Adjacente(uniaoDaVitoria, 122))
    irati.addCidadeAdjacente(Adjacente(guarapuava, 104))
    
    uniaoDaVitoria.addCidadeAdjacente(Adjacente(curitiba, 241))
    uniaoDaVitoria.addCidadeAdjacente(Adjacente(irati, 122))
    uniaoDaVitoria.addCidadeAdjacente(Adjacente(cascavel, 408))

#mapa = Mapa()

#print ("Nome da cidade:", mapa.cascavel.nome)
#print ("Cidade foi visitada?", mapa.cascavel.visitado)

#for adjacente in mapa.cascavel.adjacente:
 #   print(adjacente.cidade.nome)