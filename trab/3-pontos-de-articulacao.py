from graph_base import adjacents, nodes
MAGIC_WOW = 9900000000

def articulation_points():
  visited = {}
  pre = {}
  back_pre = {}
  tree_low = {}
  child_low = {}
  low = {}
  previous = {}
  points = {}
  qnt_root_childs = 0
  for root in nodes():
    if visited.get(root):
      continue
    print "componente"
    next_mark = 0
    points[root] = []

    stack = [[None, root]]
    while len(stack) != 0:
      block = stack[-1]
      while block and len(block) == 1:
        node = block[0]
        if node is None:
          block = None
          break
        predecessor = previous.get(node)
        if predecessor is None: # eh root
          if qnt_root_childs > 1: points[root].append(node)
        else:
          low[node] = min(back_pre[node], tree_low.get(node) or MAGIC_WOW, pre[node])

          if tree_low.get(predecessor) is None:
            tree_low[predecessor] = low[node]
          else:
            tree_low[predecessor] = min(tree_low[predecessor], low[node])

          if child_low.get(predecessor) is None:
            child_low[predecessor] = low[node]
          else:
            child_low[predecessor] = max(child_low[predecessor], low[node])

          if child_low.get(node) and child_low[node] >= pre[node]: points[root].append(node)

        stack.pop()
        block = stack[-1] if len(stack) > 0 else None

      if block is None: break

      node = block.pop()
      predecessor = block[0]
      if visited.get(node):
        if back_pre.get(predecessor) is None:
          back_pre[predecessor] = pre[node]
        else:
          back_pre[predecessor] = min(back_pre[predecessor], pre[node])
        continue

      visited[node] = True
      pre[node] = next_mark
      next_mark += 1
      previous[node] = predecessor
      if predecessor == root:
        qnt_root_childs += 1

      new_block = [node]
      for adjacent in adjacents(node):
        new_block.append(adjacent)
      stack.append(new_block)
  return points

print articulation_points()
#       
#       .
#     . . . .
#     .     . .
#   . .     .
#     . . . .
#         .
#
