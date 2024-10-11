# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:11:16 2024

@author: Kim Quyên
"""
import math
#a
def canbac(x,n):
    return n**(1/x)

#b
def so_dao(n):
    return str(n)[::-1]

#c
def sochinhphuong(n):
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n


#d
def songuyento(n):
    if n<=2:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True


#e
def tichsole(n):
    tich = 1
    m = 0
    while n>0:
        m = n % 10
        if m % 2 != 0:
            tich *= m
        n = n // 10
    return tich
 

#f
def tongnguyento(n):
    tong=1
    for i in range(2, n):
        tong += i
    return tong


#g
def tongsochinhphuong(n):
    tong = 0
    for i in range(1, n):
        if math.isqrt(i)**2 == i: 
            tong += i
    return tong

#h
def tonguocsoduong(n):
    tong = 0
    for i in range(1, n+1):
        if n%i==0:
            tong+=i
    return tong 

if __name__ == "__main__":
    print(canbac(2,3))
    print(so_dao(123))
    print(sochinhphuong(4))
    print(songuyento(13))
    print(tichsole(1235))
    print(tongnguyento(579))
    print(tongsochinhphuong(17))
    print(tonguocsoduong(12))
    

    
    
    
         



    


   

