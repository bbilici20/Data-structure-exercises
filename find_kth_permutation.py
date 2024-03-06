def find_kth_permutation(v, k, result):
  k=k-1
  result=[0]*len(v)
  if len(v)==0:
    return v

  length=len(v)
  how_many=1
  for i in range(1,length+1):
    how_many*=i
  

  left=length
  index=0
   
  while left>0: 
    result[index]= v[int(k / (how_many/left))]
    print(result)
    v.remove(v[int(k / (how_many/left))])
    k=k%(how_many/left)
    how_many=how_many/left
    left-=1
    index+=1
  
  result_number=0
  for i in range(length):
    result_number+=result[length-i-1]*10**i
  
  return result_number
