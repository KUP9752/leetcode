class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []
        
        
from collections import defaultdict 
from typing import Optional
class Solution:
  def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
    
    ## if we are not given a valid node exit early
    if not node:
      return None
    
    ## connected graph given node is always val == 1
    connections = {}
    toVisit = [node]
    seen = set()
    
    ## create adjacency list
    while toVisit:
      curr = toVisit.pop()
      
      if curr in seen:
        continue
      
      seen.add(curr)
      nIdxs = []
      for neighbour in curr.neighbors:
        nIdxs.append(neighbour.val)
        toVisit.append(neighbour)
      connections[curr.val] = nIdxs
    
    ## create new nodes and connect
    newNodes = defaultdict(lambda: None)
    
    def getNode(index: int) -> Node:
      if not newNodes[index]:
        newNodes[index] = Node(val = index)
      return newNodes[index]
        
    
    for i, ns in connections.items():
      curr = getNode(i)
      for n in ns:
        curr.neighbors.append(getNode(n))
        
    return getNode(1)
        
        
        
          
      