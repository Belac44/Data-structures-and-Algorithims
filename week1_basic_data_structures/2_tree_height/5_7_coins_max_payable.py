# def highest_not_payable(number):
#     assert(number > 5 and number != 23)
#     if number % 5 == 0:
#             return [5] * (number//5)
#     if number % 7 == 0:
#             return [7] * (number//5)
#     coins = highest_not_payable(number-5)
#     coins.append(5)
#     return coins
    

# print(highest_not_payable(23))

n = 10000

def divisible(n: int) -> bool:
    # excluded
    if n in [1, 2, 3, 4, 6, 8, 9]:
        return False
    # base cases
    elif n == 5 or n ==7 or n == 12:
        return True
    # recursive call
    else: 
        return divisible(n - 5) or divisible(n - 7)


def loop_and_check(n: int) -> None:
    # loop through each integer till givin max n
    undivisible_list = list()
    for i in range(10, n + 1):
        # call the recursive function
        if not divisible(i):
            undivisible_list.append(i)
    print(undivisible_list) # print the whole list
    print(undivisible_list[-1]) # print the last item, the largest undivisible number
            
loop_and_check(n)