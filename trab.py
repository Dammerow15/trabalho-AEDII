import heapq

# labirinto
labirinto = [
    "I.#.......",
    ".#.#.#####",
    ".#.#.....#",
    ".###.###.#",
    ".....#...#",
    "#.####.#.#",
    "#......#.#",
    "######.#.#",
    "......#..F",
    "##########"
]

DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)] # Cima, Direita, Baixo, Esquerda

def achar(lab, letra):
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if lab[i][j] == letra:
                return (i, j)
    return None

def livre(lab, i, j):
    if i < 0 or i >= len(lab) or j < 0 or j >= len(lab[0]):
        return False
    if lab[i][j] == '#':
        return False
    return True

def montar_grafo(lab):
    grafo = {}
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if lab[i][j] == '#':
                continue
            vizinhos = []
            for d in DIRECOES:
                ni, nj = i + d[0], j + d[1]
                if livre(lab, ni, nj):
                    vizinhos.append((ni, nj))
            grafo[(i, j)] = vizinhos
    return grafo

def reconstruir(veio_de, inicio, saida):
    atual = saida
    caminho = []
    while atual != inicio:
        if atual not in veio_de:
            return []
        caminho.append(atual)
        atual = veio_de[atual]
    caminho.append(inicio)
    caminho.reverse()
    return caminho

# 1. BFS 
def bfs(grafo, inicio, saida):
    fila = [inicio]
    visitados = [inicio]
    veio_de = {}
    casas_visitadas = []
    
    while len(fila) > 0:
        atual = fila.pop(0)
        casas_visitadas.append(atual)
        if atual == saida:
            break
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.append(vizinho)
                veio_de[vizinho] = atual
                fila.append(vizinho)
                
    return reconstruir(veio_de, inicio, saida), casas_visitadas

# 2. DFS 
def dfs(grafo, inicio, saida):
    pilha = [inicio]
    visitados = []
    veio_de = {}
    casas_visitadas = []
    
    while len(pilha) > 0:
        atual = pilha.pop()
        if atual not in visitados:
            visitados.append(atual)
            casas_visitadas.append(atual)
            if atual == saida:
                break
            vizinhos = grafo[atual]
            i = len(vizinhos) - 1
            while i >= 0:
                vizinho = vizinhos[i]
                if vizinho not in visitados:
                    veio_de[vizinho] = atual
                    pilha.append(vizinho)
                i -= 1
                
    return reconstruir(veio_de, inicio, saida), casas_visitadas

#  Busca 
def gulosa(grafo, inicio, saida):
    def heuristica(v):
        return abs(v[0] - saida[0]) + abs(v[1] - saida[1])

    fila_prioridade = [(heuristica(inicio), inicio)]
    visitados = []
    veio_de = {}
    casas_visitadas = []
    
    while len(fila_prioridade) > 0:
        _, atual = heapq.heappop(fila_prioridade)
        
        if atual in visitados:
            continue
            
        visitados.append(atual)
        casas_visitadas.append(atual)
        
        if atual == saida:
            break
            
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                if vizinho not in veio_de:
                    veio_de[vizinho] = atual
                    heapq.heappush(fila_prioridade, (heuristica(vizinho), vizinho))
                
    return reconstruir(veio_de, inicio, saida), casas_visitadas

def desenhar(lab, caminho):
    grade = [list(linha) for linha in lab]
    for passo in caminho:
        i, j = passo
        if grade[i][j] == '.':
            grade[i][j] = '*'
    for linha in grade:
        print("".join(linha))
    print("-" * 20)

#  EXECUÇÃO
inicio = achar(labirinto, 'I')
saida = achar(labirinto, 'F')
grafo = montar_grafo(labirinto)

c_bfs, v_bfs = bfs(grafo, inicio, saida)
c_dfs, v_dfs = dfs(grafo, inicio, saida)
c_gulosa, v_gulosa = gulosa(grafo, inicio, saida)

print("--- VISUALIZAÇÃO BFS ---")
desenhar(labirinto, c_bfs)

print("--- VISUALIZAÇÃO DFS ---")
desenhar(labirinto, c_dfs)

print("--- VISUALIZAÇÃO GULOSA ---")
desenhar(labirinto, c_gulosa)

# Tabela Comparativa Automática
print("\n" + "="*45)
print(f"{'Algoritmo':<12} | {'Tamanho Caminho':<16} | {'Casas Visitadas':<15}")
print("="*45)
print(f"{'BFS':<12} | {len(c_bfs):<16} | {len(v_bfs):<15}")
print(f"{'DFS':<12} | {len(c_dfs):<16} | {len(v_dfs):<15}")
print(f"{'Gulosa':<12} | {len(c_gulosa):<16} | {len(v_gulosa):<15}")
print("="*45)