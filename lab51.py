# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:04:42 2024

@author: Kim Quyên
"""

def ktra_gtri():
    gtri = input("Nhap gia tri:")
    if gtri.replace('.', '',1).replace('-','',1).isdigit():
        gtri=float(gtri)
    if -89 <= gtri <= 90:
        return gtri
    print("khong hop le. nhap lai")
    return ktra_gtri()
if __name__=="__main__":
    print(ktra_gtri())
    
    