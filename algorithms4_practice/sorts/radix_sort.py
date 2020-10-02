# def radix_sort(lst):
#     RADIX = 10
#     placement = 1
#
#     # get the maximum number
#     max_digit = max(lst)
#
#     while placement < max_digit:
#       # declare and initialize buckets
#       buckets = [list() for _ in range( RADIX )]
#
#       # split lst between lists
#       for i in lst:
#         tmp = int((i / placement) % RADIX)
#         buckets[tmp].append(i)
#
#       # empty lists into lst array
#       a = 0
#       for b in range( RADIX ):
#         buck = buckets[b]
#         for i in buck:
#           lst[a] = i
#           a += 1
#
#       # move to next
#       placement *= RADIX
from algorithms4.sorts import radix_sort
import random
unsorted=[random.randint(1,100) for i in range(100)]
radix_sort.radix_sort(unsorted)
print(unsorted)
