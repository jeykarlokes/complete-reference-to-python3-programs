# rev = []
# addr = []
n =3
# for reve in range(n-1,-1,-1):
#     rev.append(reve)
# for vals in range(0,n):
#     addr.append(vals)
# print(rev,addr)



# arr =[]
# final_arr = []
# sum = 0
# for i in rev:
#     for j in addr:
        
#         if i + j == n: 
#             total = sum + arr[i][j]
#             print(total)
#             final_arr.append(total)
#         else:
#             break
# print(final_arr)








# # 1,2,3
# # 1,2,3
# # 1,2,3

# #3,1 2,2 1,3





# Complete the diagonalDifference function below.
right_sum = 0
left_sum = 0
arr= [[1,2,3],[4,5,6],[7,8,9]]

def diagonalDifference(arr):
    result = []
    left_right = []
    right_left = []
    rev = []
    forward = []

    for values in range(n):
        for j in range(n):
            if values == j:
                left_right.append(arr[values][j])
            else:
                break
    for reve in range(n-1,-1,-1):
        rev.append(reve)
    for values in range(n):
        forward.append(values)
    for i in rev:
        for j in forward:
            if i+j == n:
                right_left.append(arr[i][j])
            else:
                break
    
    global left_sum 
    global right_sum
    for i in left_right:
         left_sum =  i
    for j in right_left:
         right_sum +=j
    
    print(left_sum)
    print(right_sum)
        
    summer = left_sum-right_sum
    print(summer)
        
print(diagonalDifference(arr))
""""