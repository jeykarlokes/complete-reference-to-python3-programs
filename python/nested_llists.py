cricket = [["shewagh","sachin","dhoni"],["nehra","i sharma ","rp singh"],["vvs laxman","dravid ","raina"]]
print(cricket)
for outer in cricket:
    for inner in outer:
        print(inner)

#nestedlist_comprehension
cricket = [[print(inner) for inner in outer] for outer in cricket]
nums = [[1,2,3],[4,5,6],[7,8,9,10]]
nums = [[print(inner) for inner in outer] for outer in nums ]
board = [[("X",num)if num %2 == 0 else ("O",num) for num in range(1,5)] for v in range(1,8)]


