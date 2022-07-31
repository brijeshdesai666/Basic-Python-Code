num = 5
l1 = [1,2,3,4,5,6,7,8,9,10]
l1.reverse()
for i in range(1,11):
    A = (f"{num} X {l1[i-1]} = {num*l1[i-1]}")
    print(A)