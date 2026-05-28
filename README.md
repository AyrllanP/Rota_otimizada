# FlyFood - Otimizador de Rotas (Caixeiro Viajante)

O programa lê uma matriz a partir de um arquivo `.txt`, onde o `R` representa o ponto inicial (restaurante/origem) e as outras letras representam pontos de passagem obrigatórios (entregas). O algoritmo calcula a melhor rota possível passando por todas as letras e retornando ao ponto `R` com a menor distância total.

## Tecnologias utilizadas

* **Python 3.11 / 3.12**
* **Itertools** (Biblioteca nativa para geração das permutações de caminhos)

## Funcionalidades

* **Leitura de Matriz:** Processa arquivos de texto estruturados em linhas e colunas para mapear as coordenadas dos pontos.
* **Cálculo de Distância de Manhattan:** Mede a distância entre os pontos com base em deslocamentos verticais e horizontais na matriz.
* **Força Bruta inteligente:** Gera todas as combinações de caminhos possíveis (permutações) que começam e terminam obrigatoriamente no ponto `R`.
* **Otimização:** Identifica e retorna o caminho exato que gera o menor desgaste/tempo de percurso.

## Exemplo de Entrada (txt)

```text
4 5
0 0 0 0 D
0 A 0 0 0
0 0 0 0 C
R 0 B 0 0
