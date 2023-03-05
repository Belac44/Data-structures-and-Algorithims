# python3

import sys
import threading


def compute_height(n, parents):
   head_value = parents.index(-1)
#  direct_children_of_head_number = parents.occurence(head_value)
   while True:
    indexes = []
    for i in parents:
        if i == head_value:
            indexes.append(parents.index(i))

    for index in indexes:
         head_value = parents[index]
       
       
           
def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
