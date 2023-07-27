from tkinter import *
from tkinter import messagebox
import random

rand = str(random.randint(1000, 9999))
c, x, cxd, user_hp, n = 0, 0, 0, 3, 1
strnum, randbackup = '', rand
stage, stage2 = False, False

print(f'Random 4 digit: {rand}')

def playnumber():
    global rand, c, x, cxd, user_hp, n, strnum, randbackup, stage, stage2
    
    if len(Et1.get()) == 3 and stage == False:
        for i in Et1.get():
            for j in rand:
                if i == j:
                    c += 1
                    cxd += 1
        
        if cxd != 0:
            if c == 4:
                strnum = Et1.get() if x == 0 else strnum + Et1.get()
                Texexd.config(state='normal')
                Texexd.delete(1.0, END)
                Texexd.insert(END, f'0000-9999 พบเลขปริศนาครบแล้ว [{strnum.replace("", " ")}]\nคุณได้พลังเพิ่มอีก 3 หน่วย')
                Texexd.config(state=DISABLED)
                numrandxd.config(text="พบเลขปริศนาครบแล้ว [" + strnum.replace("", " ") + "]")
                messagebox.showinfo('message', f'0000-9999 พบเลขปริศนาครบแล้ว [{strnum.replace("", " ")}]\nคุณได้พลังเพิ่มอีก 3 หน่วย')
                user_hp += 3
                u_hp.config(text="HP: " + str(user_hp))
                stage = True
                Et1.delete(0, END)
            else:
                strnum += Et1.get()
                Texexd.config(state='normal')
                Texexd.insert(END, f'ผลการทายคือ {Et1.get()} คงเหลือเลขปริศนา {len(rand) - c} หลัก\n')
                Texexd.config(state=DISABLED)
                messagebox.showinfo('message', f'ผลการทายคือ {Et1.get()} คงเหลือเลขปริศนา {len(rand) - c}')
                rand = [i for i in rand if i not in Et1.get()]
                rand = ''.join(rand)
                Et1.delete(0, END)
        else:
            user_hp -= 1
            u_hp.config(text="HP: " + str(user_hp))
            messagebox.showerror('message', f'คุณเดาผิด คุณเหลือพลังชีวิตอีก {user_hp} หน่วย')
            Et1.delete(0, END)
        if user_hp == 0:
            messagebox.showinfo('message', f'คุณเดาผิดเกิน 3 ครั้ง คุณแพ้แล้ว\nเลขปริศนาคือ {randbackup}')
            Et1.delete(0, END)
            window.destroy()
        cxd = 0
        x += 1
    else:
        messagebox.showinfo('Error', 'กรุณากรอกตัวเลขให้ครบ 3 หลัก')
        Et1.delete(0, END)
    
    if stage:
        stageLabel.config(text="Stage 2")
        btn.config(command=playnumber2)
        
        
def playnumber2():
    global rand, c, x, cxd, user_hp, n, strnum, randbackup, stage, stage2
    numxd = int(Et1.get())
    strnum = int(randbackup)
    
    if numxd < 9999:
        if numxd > strnum:
            setTextxd(f'ทายครั้ง {n} มากไปครับ')
            user_hp -= 1
            u_hp.config(text="HP: " + str(user_hp))
            Et1.delete(0, END)
            NBnumbers = numxd - strnum
            if NBnumbers < 10:
                messagebox.showinfo('message', 'ใกล้เคียงแล้ว')
        elif numxd < strnum:
            setTextxd(f'ทายครั้ง {n} น้อยไปครับ')
            user_hp -= 1
            u_hp.config(text="HP: " + str(user_hp))
            Et1.delete(0, END)
            NBnumbers = strnum - numxd
            if NBnumbers < 10:
                messagebox.showinfo('message', 'ใกล้เคียงแล้ว')
        else:
            setTextxd(f'ทายครั้ง {n} {numxd} ขอแสดงความยินดี คุณพบรหัสปริศนาจากการทายครั้งที่ {n}')
            messagebox.showinfo('message', f'ทายครั้ง {n} {numxd} ขอแสดงความยินดี คุณพบรหัสปริศนาจากการทายครั้งที่ {n}')
            window.destroy()
        if user_hp == 0:
            print('Game Over')
            messagebox.showinfo('message', f'Game Over\nเลขปริศนาคือ {randbackup}')
            window.destroy()
        n += 1

def setTextxd(text):
    global rand, c, x, cxd, user_hp, n, strnum, randbackup, stage, stage2
    Texexd.config(state='normal')
    Texexd.delete(1.0, END)
    Texexd.insert(END, text)
    Texexd.config(state=DISABLED)

window = Tk()
Labelheader = Label(window)
Labelheader.pack(side=TOP, fill=X)
mneulist = Frame(window, relief=RAISED, borderwidth=5, padx=10, pady=10, background='gray')
mneulist.pack(side=TOP, fill=X)
stageLabel = Label(mneulist, text="Stage: 1", fg='black', font=("Arial Bold", 20), borderwidth=5, relief=RAISED, padx=10, pady=10)
stageLabel.pack(side=LEFT, fill=X, expand=True, padx=10)

u_hp = Label(mneulist, text="HP: " + str(user_hp), fg='black', font=("Arial Bold", 20), borderwidth=5, relief=RAISED, padx=10, pady=10)
u_hp.pack(side=LEFT, fill=X, expand=True, padx=10)
numrandxd = Label(mneulist, text="เลขปริศนาที่ครบแล้ว: ", fg='black', font=("Arial Bold", 20), borderwidth=5, relief=RAISED, padx=10, pady=10)
numrandxd.pack(side=LEFT, fill=X, expand=True, padx=10)
content = Frame(window, relief=RAISED, borderwidth=5, padx=10, pady=10, background='gray')
content.pack(side=LEFT, fill=X, expand=True)
Et1 = Entry(content, width=50, relief=SUNKEN, borderwidth=5, font=("Arial Bold", 20), justify=CENTER)
Et1.grid(column=0, row=0, padx=10, pady=10)
btn = Button(content, text="Click", bg='green', fg='white', font=("Arial Bold", 20), borderwidth=5, relief=RAISED, command=playnumber)
btn.grid(column=1, row=0, padx=10, pady=10)
Labelfram = LabelFrame(content, text="Message", font=("Arial Bold", 20), borderwidth=5, relief=RAISED, padx=10, pady=10, background='gray')
Labelfram.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky=N+S+E+W)
Texexd = Text(Labelfram, height=10, width=50, relief=SUNKEN, borderwidth=5, font=("Arial Bold", 15), state=DISABLED)
Texexd.pack(side=LEFT, fill=X, expand=True)
window.mainloop()
