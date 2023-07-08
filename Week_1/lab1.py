def buyStamp(): # สร้างฟังก์ชัน buyStamp()
    income = int(input("Input your money: ")) # รับค่าเงินที่มี
    stamp = int(input("Input the number of stamps you want to buy: "))     # รับค่าจำนวนสแตมป์ที่ต้องการซื้อ
    totalStamp = stamp * 25     # คำนวณราคาสแตมป์ทั้งหมด
    print("รวมเป็นเงิน", totalStamp, "บาท")     # แสดงผลราคาสแตมป์ทั้งหมด
    result = income - totalStamp # คำนวณเงินทอน
    if result < 0: # ถ้าเงินทอนน้อยกว่า 0
        print("เงินไม่พอ ซื้อได้", income // 25, "ดวง เป็นเงิน", (income // 25) * 25, "บาท") # แสดงผลเงินที่ซื้อได้
        if income - (((income // 25) * 25) < 0): # ถ้าเงินที่มีน้อยกว่าราคาสแตมป์ที่ซื้อได้
            print("ไม่มีเงินทอน\nไม่มีทิปให้พนักงาน") # แสดงผล
    elif result > 0: # ถ้าเงินทอนมากกว่า 0
        print("ได้เงินทอนมาเป็น") # แสดงผล
        for bath in [500, 100, 50, 20, 10]: # วนลูปเงินทอน
            if result >= bath: # ถ้าเงินทอนมากกว่าหรือเท่ากับเงินที่ต้องการ
                count = result // bath # หาจำนวนธนบัตรที่ต้องใช้
                print("ธนบัตรใบละ ", bath, " x ", count) # แสดงผล
                result -= count * bath # คำนวณเงินทอนที่เหลือ
        if result > 0: # ถ้าเงินทอนมากกว่า 0
             print("ให้ทิปพนักงาน", result, "บาท") # แสดงผล
        else: # ถ้าเงินทอนน้อยกว่า 0
            print("ไม่มีทิปให้พนักงาน") # แสดงผล
    else: # ถ้าเงินทอนเท่ากับ 0
        print("ไม่มีทิปให้พนักงาน") # แสดงผล

buyStamp()
