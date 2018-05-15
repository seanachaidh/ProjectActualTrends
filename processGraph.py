import pandas as pd
from graph import Graph

g = Graph()
#Read data
nodes = pd.read_csv('./data/nodes_dataset.csv', encoding='cp1252',sep=",")

#Add nodes to graph
for i in range(len(nodes)):
  x=nodes['x'][i]
  y=nodes['y'][i]
  n=nodes['node'][i]
  pm=nodes['pm'][i]
  g.add_node(n,x,y,pm)

#Add edges to graph
