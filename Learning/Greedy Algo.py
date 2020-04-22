'''
def min_coins(cents):
    if cents < 1:
        return 0
    coins = [25, 10, 5, 1]
    num_of_coins = 0
    for coin in coins:
        num_of_coins += cents // coin
        cents = cents % coin
        if cents == 0:
            break
    return num_of_coins

print(min_coins(33))
'''

def min_coins(change,coins):
    if change < min(coins) or change % 1 != 0 or min(coins) < 1:
        raise ValueError("Invalid Input")
    elif change in coins:
        return 1
    else:
        min_val = change
        for coin in coins:
            if coin < change:
                cand_val = 1 + min_coins(change - coin, coins)
                min_val = min(min_val, cand_val)
        return min_val
print(min_coins(70,[25, 10, 1]))

'''
def coin_list(change,coins):
    mc = min_coins(change,coins)
    x = 0
    temp = abs(coins[1]*mc - change)
    for coin in coins:
        if abs(coin*mc - change) < temp:
            temp = abs(coins*mc change)
            if x != coin
                x = coin
                continue
            else 

'''
    
        
    
