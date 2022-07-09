# Escalonamento de Matrizes

O escalonamento de matrizes é um procedimento algébrico que podemos utilizar para resolver sistemas lineares onde o número de equações não é, necessariamente, igual ao número de incógnitas.
Resolver um sistema linear significa encontrar os valores das incógnitas que satisfazem todas as equações simultaneamente.

## Como utilizar



### 📋 Pré-requisitos

Para utilizar a função de escalonamento, é necessário que seja importado as bibliotecas numpy e numpy.linalg

```
import numpy as np
from numpy.linalg import det, inv
```

Também é necessário que a determinante da matriz seja diferente de 0, para isso utilize a função "det" na matriz

```
#Matriz exemplo
A = np.array([[0.5235**3,0.5235**2,0.5235,1],[0.7853**3,0.7853**2,0.7853,1],[1.0471**3,1.0471**2,1.0471,1],[1.5707**3,1.5707**2,1.5707,1]])
D = det(A)
D
```

### 🔧 Aplicação

Existem duas formas para utilizar a função:

A primeira forma é alterando uma coluna de cada vez, para isso você irá primeiro transformar em 1 a diagonal principal da sua coluna, chamando a função "F_UM": 

```
def F_UM(matriz, coluna):
  matriz[[coluna]] = matriz[[coluna]]*(1/(matriz[[coluna],[coluna]]))
  
F_UM(matriz, coluna)
```
E depois chamando a função "F_ZERO", para transformar o resto da coluna em zero:

```
def F_ZERO(matriz, coluna, tamanho):
  i=0
  while(i<tamanho):
    if (i==coluna):
      i=i+1
    else:
      matriz[[i]] = matriz[[i]] + matriz[[coluna]]*(matriz[[i],[coluna]]*-1)
      i=i+1

F_ZERO(matriz, coluna, tamanho)
```
E repita esse processo até terminar.

E a segunda forma seria utilizando as duas funções juntas, em uma só:

```
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

escalonamento(matriz, tamanho)
```

## ⚙️ Exemplos para teste

### 1 Exemplo: Projete um método para aproximar sen x por um polinômio cúbico no intervalo 0 ≤ x ≤ π/2.

### 2 Exemplo: A força de sustentação da asa de um projeto de aeronave é medida em várias velocidades, como segue:

Velocidade (30m/s)	         1	  2	       4	     8	     16	     32
Força de sustentação 50 kgf	0	  3,12	  15,86	  33,7	   81,5	   123,0
	        
Encontre um polinômio interpolador de grau 5 que modela os dados e use seu polinômio para estimar a força de sustentação a 600 m/s.

## 📦 Desenvolvimento

Essa função é útil para a automatização do processo de interpolação linear

## 🛠️ Construído com

* [Colaboratory](https://colab.research.google.com/drive/1LpF3ZLrJKF1VI2nRso7uGYIH1o73EvwW) - Ferramenta utilizada

## ✒️ Autores

Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início

* **João Bernardo Del Rio** - *Desenvolvedor* - [JheyBi](https://github.com/JheyBi)
