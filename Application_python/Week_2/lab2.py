# a = [1, 3, 2]
# for i in a:
#     print(i, end = " ")

#b = range(10, 0, -1)
# for i in b:
#     print(i)

num = input("Enter a number: ")
while num != 0:
    for i in range(1, 13):
        print(f"{num} x {i} = {int(num) * i}")
    num = input("Enter a number: ")