# def sum_to(n:int) -> int:
#     return ((n)*(n+1))//2


print(all(sum(range(1, n+1)) == n * (n+1) // 2 for n in range(1, 101)))