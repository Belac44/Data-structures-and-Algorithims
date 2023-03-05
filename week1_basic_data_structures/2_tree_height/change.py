def change(amount):
    assert(amount >= 8)
    if amount == 8:
        return [3,5]
    elif amount == 9:
        return [3,3,3]
    elif amount == 10:
        return [5,5]
    
    coins = change(amount-3)
    coins.append(3)
    return coins

print(change(21))