from itertools import permutations


def obter_matriz_coordenadas(caminho_arquivo):
    coordenadas = []
    with open(caminho_arquivo, 'r') as arquivo:
        matriz_texto = arquivo.read()
    linhas = matriz_texto.split("\n")

    for linha in linhas:
        elementos_linha = [elemento for elemento in linha.split()]
        if elementos_linha:
            coordenadas.append(elementos_linha)

    elementos_matriz = coordenadas[1:]
    matriz_coordenadas = {}

    for i, linha in enumerate(elementos_matriz):
        for j, elemento in enumerate(linha):
            if elemento != '0':
                matriz_coordenadas[elemento] = (i, j)

    return matriz_coordenadas

def calcular_distancias_entre_pontos(coordenadas):
    distancias = {}
    pontos = list(coordenadas.keys())

    for ponto_origem in pontos:
        for ponto_destino in pontos:
            if ponto_origem == ponto_destino:
                continue
            dist_x = abs(coordenadas[ponto_origem][0] - coordenadas[ponto_destino][0])
            dist_y = abs(coordenadas[ponto_origem][1] - coordenadas[ponto_destino][1])
            distancias[ponto_origem + ponto_destino] = dist_x + dist_y

    return distancias

def gerar_permutacoes_caminhos(coordenadas):
    chaves_grafo = list(coordenadas.keys())
    chaves_sem_R = [chave for chave in chaves_grafo if chave != 'R']
    permutacoes_caminhos = ['R' + ''.join(p) + 'R' for p in permutations(chaves_sem_R)]
    return permutacoes_caminhos

def calcular_distancia_total_caminho(distancias, lista_caminhos):
    distancia_total_caminho = {}

    for caminho in lista_caminhos:
        distancia = 0
        for i in range(0, len(caminho) - 1):
            chave_procurar = caminho[i] + caminho[i + 1]
            distancia += distancias[chave_procurar]

        distancia_total_caminho[caminho] = distancia

    return distancia_total_caminho

caminho_arquivo = 'C:/Users/user/Desktop/FlyFood/logica/teste.txt'
coordenadas_matriz = obter_matriz_coordenadas(caminho_arquivo)
distancias_entre_pontos = calcular_distancias_entre_pontos(coordenadas_matriz)
permutacoes_caminhos = gerar_permutacoes_caminhos(coordenadas_matriz)
distancias_totais = calcular_distancia_total_caminho(distancias_entre_pontos, permutacoes_caminhos)

menor_chave_caminho = min(distancias_totais, key=distancias_totais.get)
menor_valor_caminho = distancias_totais[menor_chave_caminho]

print(f"Menor distância: {menor_valor_caminho} para o caminho {menor_chave_caminho}")
