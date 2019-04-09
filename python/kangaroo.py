# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# # Complete the Kangaroo function below.
# def Kangaroo(x1, v1, x2, v2):
#     if (x1 >=0 and x2>=0) and (x1<=10000 and x2<=10000):
#         if (v1 >=1 and v2>=1) and (v1<=10000 and v2<=10000):
#             x1 = x1 + v1 # 3 6 9 12
#             x2 = x2 + v2 # 6 8 10 12
#             if x1 == x2:
#                 print("YES")
#             else:
#                 while x1!=x2:
#                     x1 = x1 + v1 # 3 6 9 12
#                     x2 = x2 + v2 # 6 8 10 12
#                     if x1 == x2:
#                         print("YES")
#                         breaK
                    
                    
#                 else:
#                     print("NO")
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # if (x1 >=0 and x2>=0) and (x1<=10000 and x2<=10000):
    #     if (v1 >=1 and v2>=1) and (v1<=10000 and v2<=10000):
    #         if v2 > v1 and x2 > x1:
    #             print("NO")
    #         elif v1 > v2 and x1 > x2 :
    #             print("NO")
    #         else:#21,6,47,3
    #             for i in range(v1+v2):
    #                 x1 = x1 + v1
    #                 x2 = x2 + v2
    #                 if x1 == x2:
    #                     print("YES")
    #                 else: 
    #                     print("NO")
    #                     breaK


    
# #27,30,33,36,39,42
# #50,53,56,59,62,63


# x1V1X2V2 = input().split()
# x1 = int(x1V1X2V2[0])
# v1 = int(x1V1X2V2[1])
# x2 = int(x1V1X2V2[2])
# v2 = int(x1V1X2V2[3])

# result = Kangaroo(x1, v1, x2, v2)
