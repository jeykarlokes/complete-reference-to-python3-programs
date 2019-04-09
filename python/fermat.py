a = int(input())
prime_no = int(input("enter prime "))

def fermat(a,n):
    power_result =  pow(a,n)
    second_result = power_result-a
    final_reuslt = second_result % n
    print(final_reuslt)
fermat(a,prime_no)

