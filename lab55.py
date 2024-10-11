# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:35:48 2024

@author: Kim Quyên
"""

def chu_vi_hcn(dai, rong):
    return 2 * (dai + rong)

def dien_tich_hcn(dai, rong):
    return dai * rong

def ve_hinh_chu_nhat(dai, rong):
    for _ in range(rong):
        print('*' * dai)
        
if __name__ == '__main__':
    print("Chu vi la:", chu_vi_hcn(5,3))
    print("Dien tich la:", dien_tich_hcn(5,3))
    ve_hinh_chu_nhat(5,3)
    