import numpy as np
import pandas as pd

#importante ter as bibliotecas: numpy, pandas e xlwt

scores = {'Match': 3 , 'Missmatch': -1, 'Gap': -2}
vertical, horizontal = 'CGCCCUGGUUCAUAUAAUAUUCCAAAGGAGCAUAUGGACUCAGCAUUGCGGGGGUCGAGUAUAUAGUAAGAAAGGGGUCCGAUUCCGAGCUUCUUAGAUUGUUUGUUCUAAUGGCUCAAUGUCCGACCCGGUGCGUCAGAGUGCAGUCCAUAUCAUGAGCCAAAGGCCACGCCAAUGAUGGCCUCACCCCACCUACUGUC', 'CGCCCUGGUUCAUAUUCCAAAGGAGCAUAUGGACUCAGCAUUGCGGGGGUCGAGUAUAUAGUAAGAAAGGGGUCCGAUUAAAUUCCGAGCUUCUUAGGCUAGAUUCGAUUGUUUGCAUUGUUCUAAUGGCUCA'
#vertical, horizontal = 'ACGC' , 'TCG'
caminho = []

#funcoes de salvar no arquivo e tratamento de strings ----------------------
def salvarResultados(matriz, alinhamento):
    global caminho

    dados = pd.DataFrame(data=matriz)
    dados.to_excel('tabela_do_alinhamento.xls', index = False)

    with open('alinhamento.txt', 'w') as arquivo:
        arquivo.write('Alinhamento:\n')
        arquivo.write(alinhamento[0]+'\n')
        arquivo.write(alinhamento[1]+'\n')
        arquivo.write('Score: '+str (matriz[0][len(horizontal) + 1]))

    return


#funcoes do algoritmo -------------------------------------------------------
def gerarMatriz(linha, coluna,matriz):
    matriz = np.zeros((linha,coluna), dtype=int)
    count = -2
    
    #colocando os valores dos gaps na vertical do zero
    for i in range(linha-3,-1,-1):
        matriz[i][1] = str(count)
        count = count - 2
    #colocando os valores dos gaps na horizontal do zero
    count = - 2
    for i in range(coluna - 2):
        matriz[linha - 2][i+2] = str(count)
        count = count - 2

    matriz = matriz.astype(str)

    #colocando a cadeia na vertical
    matriz[linha - 2][0] = 'U'
    for i in range(linha-2):
        matriz[i][0] = vertical[linha - 3 - i]

    #colocando a cadeia na horizontal
    matriz[linha - 1][1] = 'U'
    count = 0
    for i in range(2,coluna,1):
        matriz[linha - 1][i] = horizontal[count]
        count+=1

    return matriz

def valorMax(linha, coluna,matriz):
    global caminho

    esquerda = int(matriz[linha][coluna - 1]) + int(matriz[linha][coluna]) + scores['Gap']
    baixo = int(matriz[linha + 1][coluna]) + int(matriz[linha][coluna]) + scores['Gap']
    diagonal = 0
    if(matriz[linha][0] == matriz[len(vertical) + 1][coluna]):
        diagonal= int(matriz[linha + 1][coluna - 1]) + int(matriz[linha][coluna]) + scores['Match']
    else:
        diagonal  = int(matriz[linha + 1][coluna - 1]) + int(matriz[linha][coluna]) + scores['Missmatch']
    

    maior = max(esquerda,baixo,diagonal)

    if(maior == diagonal):
        caminho.append([linha,coluna,'diagonal'])
    elif(maior == esquerda):
        caminho.append([linha,coluna,'esquerda'])
    else:
        caminho.append([linha,coluna,'baixo'])

    return maior
    
def swGlobal(matriz):
    for linha in range(len(vertical) - 1, -1, -1):
        for coluna in range(2, len(horizontal) + 2, 1):
            matriz[linha][coluna] = valorMax(linha, coluna, matriz)
            
    return matriz

def atualizarDirecao(linha, coluna):
    global caminho

    #for decrescente pois as celulas perto do ponto incial estao no fim da lista
    if( linha <= (len(vertical)//2) - 2 ):
        for celula in range(len(caminho), 0, 1):
            if( caminho [celula] [0] == linha and  caminho [celula] [1] == coluna):
                return caminho [celula] [2]
    else:
        #for crescente pois estamos procurando posicoes longe do ponto inicial que consequentemente esta no incio da lista
        for celula in range(len(caminho)):
            if( caminho [celula] [0] == linha and  caminho [celula] [1] == coluna):
                return caminho [celula] [2]

    return None

def backTracing(matriz):
    global caminho
    alinhamento = ['','']

    linha,coluna,direcao = caminho[len(caminho) - 1]
    
    while(True):
        if(direcao == None):
            return [ alinhamento[0][::-1] , alinhamento[1][::-1] ]
        elif(direcao == 'diagonal'):
            alinhamento[0] +=  matriz [linha] [0] 
            alinhamento[1] +=  matriz [len(vertical) + 1] [coluna] 
            linha+=1
            coluna-=1
            direcao = atualizarDirecao(linha, coluna)
        elif(direcao == 'esquerda'):
            alinhamento[0] += '-'  
            alinhamento[1] += matriz [len(vertical) + 1] [coluna] 
            coluna-=1
            direcao = atualizarDirecao(linha, coluna)
        else: #baixo
            alinhamento[0] += matriz [linha] [0]
            alinhamento[1] += '-' 
            linha+=1
            direcao = atualizarDirecao(linha, coluna)

        
def main():
    matriz = []
    alinhamento = []

    matriz = gerarMatriz(len(vertical) + 2, len(horizontal) + 2, matriz)
    matriz = swGlobal(matriz)
    alinhamento = backTracing(matriz)
    salvarResultados(matriz, alinhamento)

main()