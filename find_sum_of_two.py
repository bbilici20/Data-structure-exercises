def find_sum_of_two(A, val):
 #TODO: Write - Your - Code
 difference = set()
 for a in A:
      difference.add(val-a)
 print(difference)
 for a in A:
      if a in difference:
          if (val % a !=0):
           return True
      
 return False;
