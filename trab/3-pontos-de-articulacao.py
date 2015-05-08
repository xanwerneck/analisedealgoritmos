from graph_base import adjacents, nodes

def articulation_points():
  visited = {}
  pre = {}
  pos = {}
  in_cicle = {}
  for state in nodes():
    if visited.get(state):
      continue
    print "componente"
    next_mark = 0

    stack = [[None, state]]
    while len(stack) != 0:
      block = stack[-1]
      while block and len(block) == 1:
        pos[block[0]] = next_mark
        next_mark += 1
        stack.pop()
        block = stack[-1] if len(stack) > 0 else None

      if block is None: break

      node = block.pop()
      if visited.get(node): continue

      visited[node] = True
      pre[node] = next_mark
      next_mark += 1
      block = [node]
      for adjacent in adjacents(node):
        block.append(adjacent)
      stack.append(block)
  print pre
  print pos

print articulation_points()
#       
#       .
#     . . . .
#     .     . .
#   . .     .
#     . . . .
#         .
#
