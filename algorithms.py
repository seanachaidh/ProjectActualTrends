from graph import Graph
from weights import Weights
import heapq
import collections
import functools
import numpy as np
from collections import deque
from util import isParetoDominated

def is_pareto_efficient(costs):
    """
    :param costs: An (n_points, n_costs) array
    :return: A (n_points, ) boolean array, indicating whether each point is Pareto efficient
    """
    is_efficient = np.ones(costs.shape[0], dtype = bool)
    for i, c in enumerate(costs):
        if is_efficient[i]:
            is_efficient[is_efficient] = np.any(costs[is_efficient]<=c, axis=1)  # Remove dominated points
    return is_efficient

def multi_objective_dijkstra(graph, initial,final):
  #Visited nodes and distances so far
  visited = {initial:(0,0)}
  paretoFront = {(0,0) : (0,0)}
  T = []

  path = {}

  #Initialize label of initial node


 
  originLabel = [[0,0],None,None]

  #graph.get_node(initial).add_temp_label(originLabel)
  #graph.get_node(initial).add_perm_label(originLabel)


  tempLabels = {initial : originLabel}

  #Lexicographical order corresponds to the lowest first objectives
  lexicographicalOrder = {initial : 0}

  it=0
  while tempLabels and it < 8:

    
    #Find the lowest node according to a lexicographical order in the temporary set
    source = min(lexicographicalOrder, key=lexicographicalOrder.get)
    print("Node",source,lexicographicalOrder)
    #print(tempLabels)

    currentLabel = tempLabels[source]
    currentNode = graph.get_node(source)
  

    #Move label from temporal to perm and remove = make final ! 
    h = currentNode.add_perm_label(currentLabel)
    del lexicographicalOrder[source]
    del tempLabels[source]
    #print("temp",tempLabels)

    #Mark all the neighbors of the currentNode
    for neighbor in graph.edges[source]:
      
      neighborNode = graph.get_node(neighbor)
 
      #Get transition rewards
      distance, pollution = graph.get_rewards(source, neighbor)
      sourceDistance, sourcePollution = currentNode.permLabels[h][0]
      newReward = [sourceDistance+distance,sourcePollution+pollution]
      newLabel = [newReward,source,h]
      dominatedNodes = []
      

      #Determine if the solution is optimal by the temporary archive
      dominated = False
     
      for label in tempLabels:
        target = tempLabels[label][0]
        #print("neighbor",neighbor,newReward,target,isParetoDominated(newReward,target))
      #  if isParetoDominated(newReward,target) :
      #    dominatedNodes.append(label)
      
      dominated = len(dominatedNodes) > 0
      #print("neighbor",neighbor,newReward,dominated)

     
        

     
      
      #Determine dominance in permant archive of node
      for label in neighborNode.permLabels:
        target = neighborNode.permLabels[0]
        #dominated = isParetoDominated(newReward,label[0])
        #if dominated:
          #break
      
      if not dominated:
        #Store the label of vertex as temporary
        tempLabels[neighbor] = newLabel
        lexicographicalOrder[neighbor] = newLabel[0][0]
        neighborNode.add_perm_label(newLabel)
        print("adding",neighbor,newLabel,tempLabels)

      #Delete all the temporary labels dominated by label
      #for dom in dominatedNodes:
        #print("dom",dom,tempLabels)
        #del lexicographicalOrder[dom]
        #del tempLabels[dom]


    it += 1
    #print("after",tempLabels)
    #Remove current from temporary labels
  print("\n")
  for node in range(len(graph.nodes)):
    print("node",node," ",graph.nodes[node].permLabels)
      #tempLabels[neighborNode.nr] = newLabel
      #lexicographicalOrder[neighborNode.nr] = newReward[0]


      #Determine dominance of solution in contrast to the permanent archive
      #for solution in neighborNode.permLabels:
      #if solution == None:

        
          #lexicographicalOrder


        #isDominated = paretoDominated(newReward,solution[0])
        #print(isDominated)

      #Determine dominance

      #Store as temporary

      #Remove the dominated points
   
 







   



  return visited, path


def dijkstra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: 
      min_node = None
      for node in nodes:
          if node in visited:

              if min_node is None:
                  min_node = node
              elif visited[node] < visited[min_node]:
                  min_node = node
      print(node)
      if min_node is None:
            break
      print(min_node)
      nodes.remove(min_node)
      current_weight = visited[min_node]

      for edge in graph.edges[min_node]:
          weight = current_weight + graph.distances[(min_node, edge)]
          if edge not in visited or weight < visited[edge]:
              visited[edge] = weight
              path[edge] = min_node

  return visited, path

g = Graph()
g.add_nodes([i for i in range(6)])
g.add_edge(0, 1, 1,2)
g.add_edge(0, 2, 5,1)
g.add_edge(0, 3, 4,6)
g.add_edge(1, 3, 2,3)
g.add_edge(1, 2, 3,2)
g.add_edge(1, 4, 2,4)
g.add_edge(2, 5, 1,8)
g.add_edge(2, 4, 2,2)
g.add_edge(3, 5, 2,7)
g.add_edge(4, 5, 3,6)

multi_objective_dijkstra(g,0,4)

