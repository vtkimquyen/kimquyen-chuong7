# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:03:10 2024

@author: Kim Quyên
"""

def ktr_so(x):
    if x<0 and x%2!=0:
        return -1

    elif x>0 and x%2 ==0:
        return 1
    return 0
if __name__=="__main__":
    print(ktr_so(2))