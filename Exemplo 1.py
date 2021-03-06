# -*- coding: utf-8 -*-
"""Trabalho1_Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LpF3ZLrJKF1VI2nRso7uGYIH1o73EvwW
"""

#1ºPasso: Importaremos as bibliotecas necessárias para os cálculos
import numpy as np
from numpy.linalg import det, inv

#2ºPasso: Colocaremos os valores da matriz, na função np.array, entretanto sem a coluna das respostas para que
#possa ser calculado a determinante

#Matriz sem coluna de respostas
A = np.array([[0.5235**3,0.5235**2,0.5235,1],[0.7853**3,0.7853**2,0.7853,1],[1.0471**3,1.0471**2,1.0471,1],[1.5707**3,1.5707**2,1.5707,1]])
A.round(4)

#3ºPasso: Iremos calcular a determinante da matriz, já que para o sistema linear possuir uma solução
#necessitamos que a determinante seja diferente de 0

D = det(A)
D

#4ºPasso: Agora que vimos que possui uma solução, inserimos a coluna de respostas para 
#que possamos fazer o escalonamento.

#Matriz com colunas de Respostas
B = np.array ([[0.5235**3,0.5235**2,0.5235,1,0.5],[0.7853**3,0.7853**2,0.7853,1,0.7071],[1.0471**3,1.0471**2,1.0471,1,0.866],[1.5707**3,1.5707**2,1.5707,1,1]])
C = B.copy()
C.round(4)

#Função para transformar em 1 a diagonal principal
def F_UM(matriz, coluna):
  matriz[[coluna]] = matriz[[coluna]]*(1/(matriz[[coluna],[coluna]]))

#Função para transformar as colunas em 0
def F_ZERO(matriz, coluna, tamanho):
  i=0
  while(i<tamanho):
    if (i==coluna):
      i=i+1
    else:
      matriz[[i]] = matriz[[i]] + matriz[[coluna]]*(matriz[[i],[coluna]]*-1)
      i=i+1

#Junção das duas funções para o escalonamento completo
def escalonamento(matriz, tamanho):
  coluna=0
  
  while(coluna<tamanho):
    matriz[[coluna]] = matriz[[coluna]]*(1/(matriz[[coluna],[coluna]]))
    i=0
    while(i<tamanho):
      if (i==coluna):
        i=i+1
      else:
        matriz[[i]] = matriz[[i]] + matriz[[coluna]]*(matriz[[i],[coluna]]*-1)
        i=i+1
    print(f"Coluna {coluna} alterada")
    print(f"{matriz}")
    coluna=coluna+1

escalonamento(C, 4)
C
