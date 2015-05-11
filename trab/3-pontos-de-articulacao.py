from graph_base import adjacents, nodes
BIG_NUMBER = 9900000000

class graph_articulation_points:
  def __init__(self):
    self.visited = {}
    self.pre = {}
    self.back_pre = {}
    self.tree_low = {}
    self.child_low = {}
    self.low = {}
    self.previous = {}
    self.points = {}

    # component states
    self.root = None
    self.qnt_root_childs = 0
    self.next_pre = 0

  def get_all(self):
    for root in nodes():
      if self.visited.get(root):
        continue
      self.root = root
      self.next_pre = 0
      self.points[self.root] = []
      self.qnt_root_childs = 0
 
      # Stack of nodes to be visited and their respectives fathers in DFS tree
      # [[father1, node1, node2, node3], [father2, node4, node5, node6]]
      self.stack = [[None, self.root]]
      while len(self.stack) != 0:
        block = self.stack[-1]
        while block and len(block) == 1: # only left the father on the block
          node = block[0]
          if node is None: # DFS is over
            block = None
            break

          self._visit_back(node)

          self.stack.pop()
          block = self.stack[-1] if len(self.stack) > 0 else None

        if block is None: break

        node = block.pop()
        origin = block[0]
        if self.visited.get(node):
          self._set_min_back_edges_pre_to(origin, node)
          continue

        predecessor = origin
        self._visit(node, predecessor)

    return self.points

  def _visit(self, node, predecessor):
    self.visited[node] = True
    self.pre[node] = self.next_pre
    self.next_pre += 1
    self.previous[node] = predecessor
    if predecessor == self.root:
      self.qnt_root_childs += 1

    new_block = [node]
    for adjacent in adjacents(node):
      new_block.append(adjacent)
    self.stack.append(new_block)


  def _visit_back(self,node):
    predecessor = self.previous.get(node)
    if node == self.root:
      if self.qnt_root_childs > 1: self.points[self.root].append(node)
    else:
      node_back_pre = BIG_NUMBER if self.back_pre.get(node) is None else self.back_pre[node]
      node_tree_low = BIG_NUMBER if self.tree_low.get(node) is None else self.tree_low[node]
      self.low[node] = min(self.pre[node], node_back_pre, node_tree_low)

      self._set_min_tree_low_to(predecessor, node)
      self._set_max_adjacents_low_to(predecessor, node)

      if self.child_low.get(node) and self.child_low[node] >= self.pre[node]: self.points[self.root].append(node)

  def _set_min_back_edges_pre_to(self, node, adjacent):
    predecessor = self.previous[node] 
    if adjacent == predecessor: return # predecessor isn't a back edge

    if self.back_pre.get(node) is None:
      self.back_pre[node] = self.pre[adjacent]
    else:
      self.back_pre[node] = min(self.back_pre[node], self.pre[adjacent])

  def _set_min_tree_low_to(self, node, successor):
    if self.tree_low.get(node) is None:
      self.tree_low[node] = self.low[successor]
    else:
      self.tree_low[node] = min(self.tree_low[node], self.low[successor])

  def _set_max_adjacents_low_to(self, node, successor):
    if self.child_low.get(node) is None:
      self.child_low[node] = self.low[successor]
    else:
      self.child_low[node] = max(self.child_low[node], self.low[successor])
  

articulations = graph_articulation_points().get_all()
print "Articulation points per component: " + str(articulations);
