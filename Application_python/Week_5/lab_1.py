def count_up():
    x1, x2 = 0, 0
    a = [0, 0, 0, 0]
    for i in range(6):
        x1 += 1
        a.insert(0, x1)
        a.pop()
        print(a, "Press Time : ", x1)
def count_down():
    x1, x2 = 0, 5
    a = [5, 4, 3, 2]
    x1 += 1
    x2 -= 1
    a.insert(3, )
    a.pop()
    print(a, "Press Time : ", x1)
count_down()