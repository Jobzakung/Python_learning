import math as match
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))

if(a == 0):
    print("หาผลลัพธ์ไม่ได้")
else:
    result = (b ** 2) - (4 * a * c)
    if(result < 0):
        print("ไม่ใช่เลขจำนวนจริง")
    else:
        print("ผลลัพธ์การหาค่าสมการเชิงเส้น คือ")
        x1 = (-b + match.sqrt(result)) / (2 * a)
        x2 = (-b - match.sqrt(result)) / (2 * a)
        print(f"x1 += {x1}, x2 -= {x2}")