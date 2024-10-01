import random

def geracao_matriz (linhas, n_buracos, n_tesouros ):

    #criação da matriz

    celula = [[None for i in range (linhas)] for j in range (linhas)]

    #atribuição de buracos ("B") 

    buracos = 0
    while buracos < n_buracos:
        i = random.randint(0, linhas-1)
        j = random.randint(0, linhas-1)

        if celula[i][j] == "B":
            continue
        if celula[i][j] is None:
            celula[i][j] = "B"
            buracos += 1


    #Criação tesouros
    tesouros = 0
    while tesouros < n_tesouros:
        i = random.randint(0, linhas-1)
        j = random.randint(0,linhas-1)

        if celula[i][j] == "B" or celula[i][j] == "T":
            continue
        else: celula[i][j] = "T"
        tesouros += 1
        
        #colocar número de tesouros ao redor da célula

    for i in range (linhas):
        for j in range (linhas):
            if celula[i][j] is None:
                buracos_proximos = 0
                if i-1 >= linhas and celula[i-1][j] == "B":
                    buracos_proximos += 1
                if j-1 >= linhas and celula [i][j-1] == "B":
                    buracos_proximos += 1
                if i+1 < linhas and celula[i+1][j] == "B":
                    buracos_proximos += 1
                if j+1 < linhas and celula[i][j+1] == "B":
                    buracos_proximos += 1
                celula[i][j] = buracos_proximos
    return(celula)

