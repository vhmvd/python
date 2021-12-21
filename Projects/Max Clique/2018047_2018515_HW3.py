def max_sub_graph_finder(graph, itr):
  sub_graph = list()
  vertices = list(graph.keys())
  sub_graph.append(vertices[itr])
  for v in vertices:
    if v in sub_graph:
      continue
    next = True
    for u in sub_graph:
      if u in graph[v]:
        continue
      else:
        next = False
        break
    if next:
      sub_graph.append(v)
  return sub_graph

graph = dict()
with open("PPI-I.txt", "r") as file:
  for line in file:
    line = line.split("\t")
    if line[0] in graph:
      graph[line[0]].append(line[1])
    else:
      graph[line[0]] = [line[1]]
      
vertices = list(graph.keys())
maximum = -999
for itr in range(len(vertices)):
  clique = max_sub_graph_finder(graph,itr)
  if (len(clique) > maximum):
    maximum = len(clique)
    sub_graph = clique

print('Fully connected sub graph:', sub_graph)
print("Size:", len(sub_graph))