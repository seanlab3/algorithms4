#!/usr/bin/env python3
"""
    module to operations with prime numbers
"""


# def check_prime(number):
#         """
#             it's not the best solution
#         """
#         special_non_primes = [0,1,2]
#         if number in special_non_primes[:2]:
#             return 2
#         elif number == special_non_primes[-1]:
#             return 3
#
#         return all([number % i for i in range(2, number)])
#
#
# def next_prime(value, factor=1, **kwargs):
#     value = factor * value
#     first_value_val = value
#
#     while not check_prime(value):
#         value += 1 if not ("desc" in kwargs.keys() and kwargs["desc"] is True) else -1
#
#     if value == first_value_val:
#         return next_prime(value + 1, **kwargs)
#     return value
from algorithms4.data_structures.hashing.number_theory import prime_numbers

alist=[]
n=int(input())
for i in range(2,n+1):
    if prime_numbers.check_prime(i):
        alist.append(i)
print(alist)
"""
def all(iterable): 
    for element in iterable: 
        if not element: 
            return False 
    return True

출처: https://codepractice.tistory.com/87 [코딩 연습]

"""
def check_prime2(number):
        """
            it's not the best solution
        """
        special_non_primes = [0,1,2]
        if number in special_non_primes[:2]:
            return 2
        elif number == special_non_primes[-1]:
            return 3

        return all([number % i for i in range(2, number)])
blist=[]
for i in range(2,n+1):
    if check_prime2(i):
        blist.append(i)
print(blist)
