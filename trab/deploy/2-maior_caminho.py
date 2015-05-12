import time
from graph_base import adjacents, find_empty, switch, printNodes

def longest_path_to(state):
  queue = [state]
  visited = dict([(state, 1)]) # predecessor do root eh 1 (poderia ser qualquer coisa)
  farthest = None
  while len(queue) > 0:
    predecessor = queue.pop()

    for node in adjacents(predecessor):
      if not visited.get(node):
        queue.insert(0, node)
        visited[node] = predecessor
        farthest = node

  node = farthest
  path = []
  while node != 1:
    path.append(node)
    node = visited[node]

  return path

ini = time.time()

path = longest_path_to(123456780)

fim = time.time()
print "Tempo de execucao: ", fim-ini

print "--------------Quantidade de arestas-" + str(len(path) - 1)
print "--------------Jogadas-"
printNodes(path)
