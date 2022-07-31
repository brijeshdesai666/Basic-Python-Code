num = int(input("Enter the number to choice multipication table\n"))
sem = int(input("Enter the number, how to long multication table\n"))


# num = 5
l1 = []

for i in range(1,sem +1):
         l1.append(i)
l1.reverse()


for s in range(sem):
    print(f"{num} X {l1[s]} = {num*l1[s]}")
