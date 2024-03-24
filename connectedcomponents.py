# -*- coding: utf-8 -*-
"""ConnectedComponents.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13wIoGtD-69NVDqOOyadaXoVywCuTiPg6
"""

def dfs(graph, node, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, component)

def connected_components(graph):
    visited = {node: False for node in graph}
    components = []
    for node in graph:
        if not visited[node]:
            component = []
            dfs(graph, node, visited, component)
            components.append(component)
    return components

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'F'],
    'C': ['A', 'F'],
    'D': ['B', 'E'],
    'E': ['D', 'C', 'F'],
    'F': ['B', 'C', 'E']
}

print(connected_components(graph))