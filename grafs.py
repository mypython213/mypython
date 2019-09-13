if 0:
    m_set = set([3,2,1, 2])    # сортировка и удаление дублей

    from typing import Set, Tuple, List
    class Graf:
        def __init__(self, name = ''):
            # self.name = name
            self.edges: Set[Tuple[str, str]] = set()
            self.nodes: Set[str] = set()

        def add_node(self, node:str) -> None:
            self.nodes.add(node)

        def add_edge(self, edge:Tuple[str, str]) -> None:
            self.edges.add(edge)

        def get_neighbours(self, node:str) -> Set[str]:
            neighbours = set()
            for i in self.edges:
                if i[0] == node:
                    neighbours.add(i[1])
                if i[1] == node:
                    neighbours.add(i[0])
            return neighbours

        def __str__(self):
            # return (str (self.nodes ))
            s = str(self.nodes)
            s = s + '\n'+ str (self.edges )
            return s
            # return (str (self.nodes + str( self.edges)))

        def breadth_first_walk(self, start_node:str, end_node:str) -> List[str]:
            visited = set()
            queue = set(start_node)
            while queue:
                visiting = queue.pop()
                nei = self.get_neighbours(visiting)
                visited.add(visiting)
                for node in nei:
                    if node not in visited:
                        queue.add(node)

            return visited

        def depth_first_walk(self, start_node:str, visited = set()) -> Set[str]:
            visited.add(start_node)
            for i in self.get_neighbours(start_node):
                if i not in visited:
                    self.depth_first_walk(i, visited)
            return visited

    g =  Graf()
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_edge(('A', 'B'))
    g.add_edge(('A', 'C'))
    g.add_edge(('B', 'D'))
    print(g)
    print(g.get_neighbours('A'))
    print(g.breadth_first_walk('A','D'))
    print(g.depth_first_walk('A'))



import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_node('A', data={"name": "Node A"})
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_edge('A', 'B')
G.add_edge('A', 'C')
print(G.nodes)
print(G["A"])
nx.draw_networkx (G)
plt.show()

print(nx.neighbors('A'))
print(list(nx.shortest_path(G, 'A')))


import os
print (isinstance('ssss', G))
