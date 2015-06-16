# version : 1.1 revision
import time
from graph_base import adjacents, nodes

def dfs(graph):

  # hash mapeando vertices do grafo ja visitados
  visited = {}
  
  # array com as componentes
  # cada indice do array contem vertices + arestas da componente
  components_conex   = [] 

  for node in graph:
    if visited.get(node) == None:
      component = search(graph, node, visited)
      components_conex.append(component)
  return components_conex


def search(graph, nod, visited):
  # hash com vertices da componente conexa
  nodes_comp = {}

  # array com as arestas da componente
  edges_comp  = [] 

  component_conex  = []       
  component_conex.append(nodes_comp)
  component_conex.append(edges_comp)

  stack    = []     
  stack.append(nod) 

  while(len(stack) > 0):
    node = stack.pop()
    for node_adj in adjacents(node):
      if not nodes_comp.get(node_adj) and not visited.get(node_adj):
        stack.append(node_adj)
        edges_comp.append([node, node_adj])
    nodes_comp[node] = 1
    visited[node]  = 1

  return component_conex


ini = time.time()
components_conex = dfs(nodes())
fim = time.time()
print "Tempo de execucao: ", fim-ini
print "---------------------------------"
print "Numero de comp. conexas: ", len(components_conex)
print "---------------------------------"
for x in xrange(0, len(components_conex)):
  print "---------COMPONENTE-", x + 1
  print "-Qtde vertices-", len(components_conex[x][0])
  print "-Qtde arestas- ", len(components_conex[x][1])
