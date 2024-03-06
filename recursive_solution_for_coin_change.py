
def solve_coin_change(denominations, amount):
  list_of_coin_lists=[]
  length=len(denominations)
  list_of_coins=[0]*length

  def change_calculator(amount,list_of_coins):
    if(amount==0):
      if list_of_coins not in list_of_coin_lists:
        list_of_coin_lists.append(list(list_of_coins))
        return
    elif(amount<0):
      list_of_coins=[0]*length
      return
    else:
      for i in range(length):
        list_of_coins[i]+=1
        change_calculator(amount-denominations[i],list(list_of_coins))

  change_calculator(amount,list_of_coins)
  
  return len(list_of_coin_lists)
