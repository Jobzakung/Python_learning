import tkinter as tk


def todo():
    T1.delete("0.1", tk.END)
    data = E1.get()
    if (int(data) == 0):
        root.destroy()
    else:
        # T1.insert(tk.END, f"Test : {data}\n")
        for i in range(1, 13):
            T1.insert(tk.END, f"{data} x {i} = {int(data) * i}\n")


root = tk.Tk()
root.geometry("250x450")
L1 = tk.Label(root, text="Table of Formula")
L1.pack()
L2 = tk.Label(root, text="ระบุแม่ที่ต้องการแสดง")
L2.pack()
E1 = tk.Entry(root)
E1.pack()
B1 = tk.Button(root, text="Exec", command=todo)
B1.pack()
T1 = tk.Text(root, width=40, height=15)
T1.pack()

tk.mainloop()
