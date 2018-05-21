import numpy as np
import pandas as pd
nodes_dataset=[]
df_nodes = pd.read_csv('./data/nodes_dataset.csv', encoding='cp1252',sep=",")
df_edges = pd.read_csv('./data/edges_dataset.csv', encoding='cp1252',sep=",")
row = [[40,50.853947,4.31635,80.2301821824]]
row =
df = pd.DataFrame(row,index=None,columns=['node','x','y','pm'])
df = df_edges.append(df)
df.to_csv('./data/edges_dataset.csv', sep=',',index=None)
#print(df)
print(df)