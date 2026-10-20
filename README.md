# Resolução de Labirinto com Grafos (AED II)

Atividade desenvolvida para a disciplina de Algoritmos e Estruturas de Dados II (AED II) sob a orientação do Prof. Pablo De Chiaro.

## Sobre o Projeto
O objetivo deste projeto é representar um labirinto como um grafo e implementar três algoritmos clássicos de busca para encontrar um caminho da entrada (`I`) até a saída (`F`), comparando a eficiência e o comportamento de cada abordagem.

## Labirinto Desenvolvido
O labirinto utilizado possui dimensões de $10 \times 10$, contendo corredores livres (`.`), paredes (`#`), múltiplos caminhos alternativos de tamanhos diferentes e becos sem saída propositais para testar a robustez das buscas:

```text
I.#.......
.#.#.#####
.#.#.....#
.###.###.#
.....#...#
#.####.#.#
#......#.#
######.#.#
......#..F
##########
