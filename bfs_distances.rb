def distances_from(node, g)
  visited = {}
  to_visit = [node]
  layer = 0
  layers = [1]
  distances = {}
  while !to_visit.empty?
    visiting = to_visit.pop

    if !visited[visiting]
      visited[visiting] = true

      distances[visiting] = layer

      adjacents = g[visiting] || []
      layers.insert 0, 0
      adjacents.each do |n|
        layers[0] += 1
        to_visit.insert(0, n)
      end
    end

    layers[-1] -= 1
    if layers[-1] == 0
      layers.pop
      layer += 1
    end
  end
  distances
end

graph = {
  0 => [2, 3],
  1 => [2],
  2 => [1, 3],
  3 => [0]
}

p distances_from(0, graph)
