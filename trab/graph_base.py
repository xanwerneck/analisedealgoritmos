from permutation_non_recursive import _nodes

BOARD_SIZE = 3
NUMBER_SIZE = BOARD_SIZE**2-1

graph = {}

def nodes():
  return _nodes()

def adjacents(state):
  if graph.get(state) is None:
    graph[state] = _adjacents(state)
  return graph[state]

def find_empty(state):
  i = NUMBER_SIZE
  while state % 10 != 0:
    state = state / 10
    i -= 1
  return (i%BOARD_SIZE, i/BOARD_SIZE)

def switch(state, pos1, pos2):
  base1 = 10 ** (NUMBER_SIZE - pos1[0] - pos1[1]*BOARD_SIZE)
  base2 = 10 ** (NUMBER_SIZE - pos2[0] - pos2[1]*BOARD_SIZE)
  digit1 = (state / base1) % 10
  digit2 = (state / base2) % 10
  state += base1 * (digit2 - digit1) + base2 * (digit1 - digit2)
  return state

def printNodes(nodes):
  NODES_PER_LINE = 8
  initial_size = len(nodes)
  while len(nodes) != 0:
    nodes_in_line = min(NODES_PER_LINE,len(nodes))
    for i in reversed(range(0,3)): 
      nodes_pieces = []
      nodes_pieces.append("-> " if i == 1 and len(nodes) != initial_size else "   ")
      for j in xrange(0,nodes_in_line):
        node = nodes[j]
        piece_pow = 10**(i*BOARD_SIZE)
        piece = node / piece_pow
        piece_str = str(piece)
        if piece < 100: piece_str = "0" + piece_str
        nodes_pieces.append(piece_str)
        nodes[j] = node - piece * piece_pow
      nodes_pieces.append(" ->" if i == 1 and len(nodes) > nodes_in_line else "   ")
      print "  ".join(nodes_pieces)
    nodes = nodes[nodes_in_line:]
    print
    print


def _adjacents(state):
  empty_pos = find_empty(state)

  adjacents = []
  for i in range(0,4):
    x = empty_pos[0] + (i     / 2) * (-1)**i
    y = empty_pos[1] + ((3-i) / 2) * (-1)**i
    if 0 <= x <= BOARD_SIZE-1 and 0 <= y <= BOARD_SIZE-1:
      new_state = switch(state, empty_pos, (x,y))
      adjacents.append(new_state)
  return adjacents
