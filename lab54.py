# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:28:24 2024

@author: Kim Quyên
"""

def fib(n):
    a,b = 0,1
    while a<n:
        print(a, end='\t')
        a, b = b, a+b
if __name__ == "__main__":
    print(fib(1000))

    