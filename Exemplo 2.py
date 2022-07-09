# -*- coding: utf-8 -*-
"""Trabalho2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dSNbGybbl4OGOUvVv_eB2hOUlmNTUGTS
"""

#1ºPasso: Importaremos as bibliotecas necessárias para os cálculos
import numpy as np
from numpy.linalg import det, inv
np.set_printoptions(precision = 4, suppress = True)

a1 = 1.0
a2 = 2.0
a3 = 4.0
a4 = 8.0
a5 = 16.0
a6 = 32.0

#2ºPasso: Colocaremos os valores da matriz, na função np.array, entretanto sem a coluna das respostas para que
#possa ser calculado a determinante

#Matriz sem coluna de respostas
A = np.array([[a1**5,a1**4,a1**3,a1**2,a1,1],[a2**5,a2**4,a2**3,a2**2,a2,1],[a3**5,a3**4,a3**3,a3**2,a3,1],[a4**5,a4**4,a4**3,a4**2,a4,1],[a5**5,a5**4,a5**3,a5**2,a5,1],[a6**5,a6**4,a6**3,a6**2,a6,1]])
A

#3ºPasso: Iremos calcular a determinante da matriz, já que para o sistema linear possuir uma solução
#necessitamos que a determinante seja diferente de 0

D = det(A)
D

#4ºPasso: Agora que vimos que possui uma solução, inserimos a coluna de respostas para 
#que possamos fazer o escalonamento.

#Matriz com colunas de Respostas
B = np.array([[a1**5,a1**4,a1**3,a1**2,a1,1,0],[a2**5,a2**4,a2**3,a2**2,a2,1,3.12],[a3**5,a3**4,a3**3,a3**2,a3,1,15.86],[a4**5,a4**4,a4**3,a4**2,a4,1,33.7],[a5**5,a5**4,a5**3,a5**2,a5,1,81.5],[a6**5,a6**4,a6**3,a6**2,a6,1,123]])
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
    #print(f"Coluna {coluna} alterada")
    #print(f"{matriz}")
    coluna=coluna+1

escalonamento(C, 6)
C
