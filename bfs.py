# -*- coding: utf-8 -*-
"""BFS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sxcQfzdz1lymnCeoc0VNInU9geVugW7u
"""

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'F'],
    'C': ['F'],
    'D': ['E'],
    'E': ['C', 'F'],
    'F': ['B']
}

visited = []

def dfs(graph, start):
  if start not in visited:
    visited.append(start)
  for node in graph.get(start, []):
    if node not in visited:
      visited.append(node)
      dfs(graph, node)

  return visited

print(dfs(graph, 'A'))