# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 07:50:31 2021

@author: user
"""
import Graph_data
def find_all_paths(graph, start, destination, path=[]):
        if start not in graph:
            return []
        path = path + [start]
        if start == destination:
            return [path]
        all_paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(Graph_data.Places_graph, node, destination, path)
                for newpath in newpaths:
                    all_paths.append(newpath)
        return all_paths     
    
paths=find_all_paths(Places_graph.graph,'Rama Lake','Abottabad')
for path in paths:
    print(path)
