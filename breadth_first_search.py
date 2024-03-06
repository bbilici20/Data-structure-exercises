def level_order_traversal(root):
  result = ""
  #TODO: Write - Your - Code
  array_of_nodes=[]
  array_of_nodes.append(root)

  index=0
  while(index<len(array_of_nodes)):
    current=array_of_nodes[index]
    if(current.left):
      array_of_nodes.append(current.left)
    if(current.right):
      array_of_nodes.append(current.right)
    index +=1
   
  for node in array_of_nodes:
    result += str(node.data)+" "

  return result
