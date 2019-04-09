def jumpingOnClouds(c):
    no_of_jumps = 0
    # reduced_size = n % 2
    i = 2 
    while i < n-1:
        cloud = c[i]
        if cloud == 0:
            no_of_jumps += 1 #jump 2 i = 4
            diff = n-i 
            if diff > n-2:
                i += 2
            i-=1
        elif cloud == 1:
            i = i-1
            no_of_jumps += 1
            diff = n-i
            if diff > n-2:
                i+=2
            else:
                i-=1
    return no_of_jumps
n = int(input())
c = list(map(int, input().rstrip().split()))
result = jumpingOnClouds(c)
print(result)