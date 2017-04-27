# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 18:20:29 2016

@author: Caio Cid Santiago
"""
import numpy as np

#Funções objetivos

## Custo Minimo
def f(cargas, custos, curPop):
    curAptidao = np.zeros(len(curPop))
    for t in range (0,24):
        
        for m in range(0, len(custos)):
            if custos[m][1]>t and custos[m][2]<t:
                custoAtual = custos[m][0]
                    
        for i in range(0,len(curPop)):       
            for j in range(0, len(cargas)):
                if t >= curPop[i][j] and t< curPop[i][j] + cargas[j][1]:
                    curAptidao[i] = curAptidao[i] + cargas[j][0]*custoAtual 
                
    return curAptidao

# Seleção

def selec(pop, custos, cargas):
    interPop = np.zeros(len(pop))
    curAptidao = f(cargas, custos, pop)
    bestGen = [0,curAptidao[0]]
    
    for i in range(0,len(pop)):
        if bestGen[1]>curAptidao[i]:
            bestGen[1] = curAptidao[i]
            bestGen[0] = i
    
    interPop[0] = pop[bestGen[0]]
    
    for i in range(1,len(pop)):
        m = np.random.randint(0,high=len(pop))
        n = np.random.randint(0,high=len(pop))
        
        if curAptidao[m] > curAptidao[n] :
            interPop[i] = pop[n]
        else:
            interPop[i] = pop[m]
    
    return interPop

# Crossover

#def cross(pop, rtCross):

        
# Parâmetros do Algoritmo genético

sizePop = 100
maxGeneration = 1000
rtCross = 1
rtMut = 0.05
maxDem = 200 #Demanda maxima contratada 
custos = [[0.5, 0, 5],[1, 6, 16], [2, 16, 23]] #[preço, começo, termino]
cargas = [[8,8],[7,8],[10,10],[0.5,1]] #[consumo, picoconsumo]
user = [[[1],14,23], [[1,1,2], 14,23], [[2], 14,23], [[1,3], 14,23]] #[ [tempos], inicio minimo, termino maximo]


# Criando População inicial

#curPop = np.random.choice(np.arange(0,24,1),size=(sizePop, len(cargas)))
curPop = np.zeros(sizePop, len(cargas))
curPop = curPop.tolist()

# As etapas das cargas sempre sao em blocos? 
for i in range(0, sizePop):
    curPop[0] = 
    
