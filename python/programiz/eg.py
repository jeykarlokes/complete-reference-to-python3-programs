#!/bin/python3

import math
import os
import random
import re
import sys

#1 2 3
#1 2 3
#1 2 3

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    sum_r1 = []
    sum_r2 = []
    sum_r3 =[]
    sumr1 =0
    sumr2 = 0
    sumr3 = 0
    c1 = []
    c2 = []
    c3 = []
    c1_sum = 0
    c2_sum =0
    c3_sum = 0
    l_dsum = []
    r_dsum = []

    
    
    difference  = []
    for i in range(3):
        for j in range(3):
            if i==0:
                sum_r1.append(s[i][j])
            elif i ==1:
                sum_r2.append(s[i][j])
            else:
                sum_r3.append(s[i][j])
            if i ==0 and j ==0:
                l_dsum.append(s[i][j])
            elif i ==1 and j == 1:
                l_dsum.append(s[i][j])
            elif i ==2 and j == 2:
                l_dsum.append(s[i][j])
            if i == 2 and j == 0:
                r_dsum.append(s[i][j])
            elif i == 1 and j ==1 :
                r_dsum.append(s[i][j])
            elif i == 0 and j == 2:
                r_dsum.append(s[i][j])
    for i in range(3):
        for j in range(3):
            if j==0:
                c1.append(s[i][j])
            elif j ==1:
                c2.append(s[i][j])
            else:
                c3.append(s[i][j])
    left_sum = sum(l_dsum)
    right_sum = sum(r_dsum)
    for i in range(3):
        sumr1 = sumr1+ sum_r1[i]
        sumr2 = sumr2 + sum_r2[i]
        sumr3 = sumr3 + sum_r3[i]
        c1_sum+= c1[i]
        c2_sum+= c2[i]
        c3_sum+= c3[i]

    # print(c1_sum,c2_sum,c3_sum)
    if sumr1!=15 and c1_sum!=15:
        diff =15- sumr1
        c_diff = 15- c1_sum
        difference.append(abs(c_diff))
        difference.append(abs(diff))
    if sumr2!=15 and c2_sum!=15:
        diff =15- sumr2
        c_diff = 15-c2_sum
        difference.append(abs(c_diff))

        difference.append(abs(diff))
    if sumr3!=15 and c3_sum!=15:
        diff =15- sumr3
        c_diff = 15-c3_sum
        
        # print(diff)
        difference.append(abs(c_diff))
        difference.append(abs(diff))
    # print(sumr1,sumr2,sumr3)
    total_diff =  0
    print(difference)
    print(sum(difference))
        

# s = []
# for _ in range(3):
#     s.append(list(map(int, input().rstrip().split())))
s = []
for _ in range(3):
    elements = input().rstrip().split()
    list(elements)
    a = []
    s1 = all([a.append(int(num))  for num in elements if int(num) <=9 and int(num)>=1])
    s.append(a)

result = formingMagicSquare(s)
