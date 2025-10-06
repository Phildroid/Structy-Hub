def connected_components_count(graph):
  count = 0
  visited = set()
  for node in graph:
    if explore(graph, node, visited) == True:
      count += 1
  return count

def explore(graph, node, visited):
  if node in visited:
    return False
  visited.add(node)

  for neighbor in graph[node]:
    explore(graph, neighbor, visited)

  return True

