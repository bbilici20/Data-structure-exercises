class Node:
  def __init__(self, d):
    self.data = d
    self.neighbors = []

def clone(root):
  all_nodes=[]
  index=0
  current=root
  nodes=dict()
  nodes[current]=Node(current.data)
  all_nodes.append(current)

#put all the original nodes in a list and their copies in a dictionary
  while(index<len(all_nodes)):
    current=all_nodes[index]
    for node in current.neighbors:
      if nodes.get(node)==None:
        new_node=Node(node.data)
        new_node.neighbors=[]
        all_nodes.append(node)
        nodes[node]=new_node
    index+=1

  index=0
  current=root
  while(index<len(all_nodes)):
    current=all_nodes[index]
    for node in current.neighbors:
      nodes[current].neighbors.append(nodes[node])
    index+=1
  
  
  return nodes[root]    # return root
