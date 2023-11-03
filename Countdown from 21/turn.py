def play_human_turn(n):
    # 1. prompt user for their move
    while True:
        coins_to_be_taken = int(input('Enter the number of coins you want to remove(You have to remove 1-3) '))
        if 1<=coins_to_be_taken <=3 and coins_to_be_taken<=n:
    # 2. output number of coins after user's move
            return n-coins_to_be_taken
        else:
            print("Sorry, you can only remove 1,2,3 coins and not more than what's available")
            
    # 3. If the human wins, indicate that and return 0
    # You must implement this function
    pass

def play_computer_turn(n):
    import random
    if n % 4!=0:
        coins_to_be_taken = n%4
    else:
        coins_to_be_taken = random.randint(1, min(3,n))
    # 1. Make computer move
    print('The computer removes ' +  str(coins_to_be_taken) + ' coins ' )
    return n - coins_to_be_taken
    # 2. If computer wins, indicate that and return 0
    # 3. return number of coins remaining
    # You must implement this function 
    pass
