def is_bst(root):
  
  if(root==None):
    return 1
  
  array_of_nodes=[]
  array_of_limits=[]
  array_of_nodes.append(root)
  array_of_limits.append(root.data)
  index=0

  if(root.left):
    if(root.left.data>root.data):
      return 0
    else:
      array_of_nodes.append(root.left)
      array_of_limits.append(root.data)

  if(root.right):
    if(root.right.data<root.data):
      return 0
    else:
      array_of_nodes.append(root.right)
      array_of_limits.append(root.data)  
  if(len(array_of_nodes)>1):
    index +=1
 
  while(index<len(array_of_nodes)):
    current=array_of_nodes[index]

    if(array_of_limits[index]>current.data):
      if(current.left): 
        if(current.left.data<current.data): #if a node is the left child of a left child node, just check if the value is smaller than its parent.
          array_of_nodes.append(current.left)
          array_of_limits.append(current.data)
        else:
          return 0
      if(current.right):
        if((current.right.data>current.data) and (current.right.data<array_of_limits[index])): #if a node is the right child of a left child node, check if the value is between the two parent nodes
          array_of_nodes.append(current.right)
          array_of_limits.append(current.data)
        else:
          return 0
    elif(array_of_limits[index]<current.data):
      if(current.left):
        if((current.left.data<current.data)and(current.left.data>array_of_limits[index])): #if a node is the left child of a right child node, check if the value is between the two parent nodes
          array_of_nodes.append(current.left)
          array_of_limits.append(current.data)
        else:
          return 0
      if(current.right):
        if(current.right.data>current.data): #if a node is the right child of a right child node, just check if the value is bigger than its parent.
          array_of_nodes.append(current.right)
          array_of_limits.append(current.data)
        else:
          return 0
    index +=1
    
    #the algorithm uses the correctness of the base case.

  return 1
