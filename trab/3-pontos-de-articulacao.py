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
  for root in nodes():
    if visited.get(root):
      continue
    next_mark = 0
    points[root] = []
    qnt_root_childs = 0

    stack = [[None, root]]
    while len(stack) != 0:
      block = stack[-1]
      while block and len(block) == 1:
        node = block[0]
        if node is None:
          block = None
          break
        predecessor = previous.get(node)
        if node == root:
          if qnt_root_childs > 1: points[root].append(node)
        else:
          node_back_pre = MAGIC_WOW if back_pre.get(node) is None else back_pre[node]
          node_tree_low = MAGIC_WOW if tree_low.get(node) is None else tree_low[node]
          low[node] = min(pre[node], node_back_pre, node_tree_low)

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
      origin = block[0]

      if visited.get(node) and node != previous[origin]:
        if back_pre.get(origin) is None:
          back_pre[origin] = pre[node]
        else:
          back_pre[origin] = min(back_pre[origin], pre[node])

      if visited.get(node):
        continue

      predecessor = origin

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
