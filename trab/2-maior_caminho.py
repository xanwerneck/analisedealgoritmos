from graph_base import adjacents, find_empty, switch

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
    path.insert(0, node)
    node = visited[node]

  return path

path = longest_path_to(123456780)
print len(path) - 1
print path

#          123
#          456
#          780
#    
#    123         123
#    450         456
#    786         708
# 
# 123   120   123   122
# 405   453   406   456
# 786   786   758   078
