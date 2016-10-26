# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 18:20:29 2016

@author: Caio Cid Santiago
"""
import numpy as np

#Função objetivo/

def f(t):
    return np.sin(t)

# Parâmetros do Algoritmo genético

sizePop = 100
maxGeneration = 1000
rtCross = 1
rtMut = 0.05
maxDem = 200 #Valor Máximo de demanda energética
limFunc = [0,maxDem] 
custos = [[0.5, 0, 5],[1, 6, 16], [2, 16, 23]] #[preço, começo, termino]
cargas = [[8,3],[7,2],[10,1],[0.5,12]]#[consumo, tempo]

# Criando População inicial

curPop = np.random.choice(np.arange(0,24,1),size=(len(cargas),100))
