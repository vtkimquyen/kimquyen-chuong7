# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:48:23 2024

@author: Kim Quyên
"""
#a
def tinhtong(n):
    tong=0
    for i in range(1, n+1):
        tong += i
    return tong
print(tinhtong(5))

#b
def tinhtong(n):
    tong=0
    for i in range(1, n+1):
        tong += i**2
    return tong
print(tinhtong(3))

#c
def tinhtong(n):
    tong=0
    for i in range(1, n+1):
        tong += 1/i
    return tong
print(tinhtong(5))

#d
def tonggiaithua(n):
    tong=0
    for i in range(1, n+1):
        m=1
        for j in range(1, i+1):
            m *= j
        tong += m
    return tong
print(tonggiaithua(5))

#e
def tinhtich(n):
    tich=1
    for i in range(1, n+1):
        tich *= i
    return tich
print(tinhtich(3))
