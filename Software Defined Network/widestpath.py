import collections
import math



class Graph:
  def __init__(self):
    self.vertices = set()

    # makes the default value for all vertices an empty list
    self.edges = collections.defaultdict(list)
    self.weights = {}

  def add_vertex(self, value):
    self.vertices.add(value)
  
  def remove_vertex(self,value):
    if value in self.vertices:
      self.vertices.remove(value)

  def add_edge(self, from_vertex, to_vertex, distance):
    if from_vertex == to_vertex: pass  # no cycles allowed
    self.edges[from_vertex].append(to_vertex)
    self.weights[(from_vertex, to_vertex)] = distance
  
  def remove_edge(self,value):
    if value in self.edges:
      self.edges.pop(value)
    for i in self.edges:
      if value in self.edges[i]:
        self.edges[i].remove(value)
  
  def __str__(self):
    string = "Vertices: " + str(self.vertices) + "\n"
    string += "Edges: " + str(self.edges) + "\n"
    string += "Weights: " + str(self.weights)
    return string
 
  def remove_link(self, value1, value2):
    for i in self.edges:
      if value2 in self.edges[value1]:
        self.edges[value1].remove(value2)
      if value1 in self.edges[value2]:
        self.edges[value2].remove(value1)




def dijkstra(graph, start):
  # initializations
  S = set()

  # delta represents the length shortest distance paths from start -> v, for v in delta. 
  # We initialize it so that every vertex has a path of infinity
  delta = dict.fromkeys(list(graph.vertices), float('-inf'))
  previous = dict.fromkeys(list(graph.vertices), None)

  # then we set the path length of the start vertex to 0
  delta[start] = float('inf')

  # while there exists a vertex v not in S
  while S != graph.vertices:
    # let v be the closest vertex that has not been visited...it will begin at 'start'
    v = max((set(delta.keys())- S), key=delta.get)

    # for each neighbor of v not in S
    for neighbor in set(graph.edges[v]) - S:
      #new_path = delta[v] + graph.weights[v,neighbor]
      npath = min(delta[v], graph.weights[v,neighbor])
      new_path = max(delta[neighbor], npath)

      # is the new path from neighbor through 
      if new_path > delta[neighbor]:
        # since it's optimal, update the shortest path for neighbor
        delta[neighbor] = new_path

        # set the previous vertex of neighbor to v
        previous[neighbor] = v


    S.add(v)

  return (delta, previous)

def widest_path(graph, start, end):
  delta, previous = dijkstra(graph, start)
  
  path = []
  vertex = end

  while vertex is not None:
    path.append(vertex)
    vertex = previous[vertex]

  path.reverse()
  return path






