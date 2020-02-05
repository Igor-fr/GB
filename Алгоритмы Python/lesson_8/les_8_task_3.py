# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
#
# Примечания:
# Граф должен храниться в виде списка смежности
# Генерация графа выполняется в отдельной функции, которая принимает на вход число вершин

import random

# Логика получения списка смежности: для каждой вершины случайным образом определяем количество врешин, к которым
# от нее будут идти ребра, причем от первой (0) вершины ребра идут до каждой веришны, иначе могут появиться вершины,
# к которым невозможно прийти. Затем случайно наполняем список вершин для выбранной вершины, проверяем чтобы вершины
# не повторялись и чтобы не попала наполняемая вершина, так как петель в графе быть не должно.

def generate_graph(N):
    graph = []
    for i in range(N):
        vertexes = []
        if i == 0:
            graph.append([_ for _ in range(1, N)])
            continue
        count_edges = random.randint(1, N - 1)
        while len(vertexes) != count_edges:
            vertex = random.randint(0, N - 1)
            if vertex != i and (vertex not in vertexes):
                vertexes.append(vertex)
        graph.append(sorted(vertexes))
    return graph


def dfs(graph, start):

    is_visited = [False for _ in range(len(graph))]

    def _dfs_find(vertex):
        for ver in graph[vertex]:
            if not is_visited[ver]:
                print(ver)
                is_visited[ver] = True
                _dfs_find(ver)

    is_visited[start] = True
    _dfs_find(start)


graph = generate_graph(int(input("Введите количество вершин в графе: ")))
print(*graph, sep = '\n')
dfs(graph, int(input("Выберите, с какой вершины начать: ")))