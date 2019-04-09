A = []
N = int(input("enter N"))
M = int(input("enter M "))
n  =0
def MaxProductNaive(A):
    product = 0
    for i in range(n):
        for j in range(i+1,n):
            product = max(product,A[i].A[j])
        return producSt
def MaxProductFast(A):
    index1 = 0
    for i in range(2,n):
        if A[i] > A[index1]:
            index1=i
        if index1 ==1 :
            index2= 2
        else:
            index2 ==1
        for i in range(n):
            if A[i] != A[index1] and A[i] > A[index2]:
                index2 =i
        return A[index1],A[index2]
def stressTEst(N,M):
    while True:
        A = []
        if N >2:
            if n >= 2 and n < N:
                n = int(input())
                for i in  range(0,n):
                    var = int(input("enter "))
                    A.append(var)
                print(A)
            print(A)
        result1 = MaxProductNaive(A)
        result2 = MaxProductFast(A)
        if result1 == result2:
            print("OK")
        else:
                print("Wrong answer",result1,result2)
s = stressTEst(2,9)
print(s)