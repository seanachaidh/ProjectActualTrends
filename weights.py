class Weights(object):

    def __init__(self, weight_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if weight_dict == None:
            weight_dict = {}
        self.weight_dict = weight_dict

    def keys(self):
        """ returns the vertices of a graph """
        return list(self.weight_dict.keys())

    def get_weight(self,source,target):
        """ weights associated with pair"""
        key = (source,target)
        if key not in self.weight_dict:
            return None
        return self.weight_dict[(source,target)]

    def add_weight(self,source,target,weight):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        key = (source,target)

        if key in self.weight_dict and weight < self.weight_dict[key]:
            self.weight_dict[key] = weight
        else:
            self.weight_dict[key] = weight



    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.weight_dict:
            for neighbour in self.weight_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.weight_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

w = {}

weights = Weights(w)
weights.add_weight(0, 1, 4)
weights.add_weight(0, 1, 3)

#print(weights.weight(0,1))

#print(weights.weight(0,1))
