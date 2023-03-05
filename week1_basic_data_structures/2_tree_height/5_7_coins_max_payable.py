def highest_not_payable(number):
    assert(number > 11)
    if number % 5 == 0:
            return [5] * (number//5)
    if number % 7 == 0:
            return [7] * (number//5)
    coins = highest_not_payable(number-5)
    coins.append(5)
    return coins
    
    