from graph_base import adjacents, nodes

def articulation_points():
  for state in nodes():
    if visited.get(state):
      continue
    print "componente"
    visited = dict([(state,True)])
    pre = {}
    pos = {}

    stack = [state]
    while len(stack) != 0:
      node = stack.pop()
      for adjacent in adjacents(node):
        if visited.get(adjacent):
          continue
        visited[adjacent] = True
        stack.append(adjacent)

print articulation_points()
