import tkinter as tk
from tkinter import messagebox

def ins(name, phone):
    lb.insert(tk.END, f"{name}: {phone}")

def button_click_1():
    input_dialog = InputDialog(root)
    root.wait_window(input_dialog.top)
    if input_dialog.result:
        name, phone = input_dialog.result
        ins(name, phone)

def button_click_2():
    print("Delete Data")
    remove_data()

def button_click_3():
    print("Edit Data")
    edit_data()

def edit_data():
    selected_index = lb.curselection()
    if selected_index:
        index = selected_index[0]
        text = lb.get(index)
        name, phone = text.split(": ")
        lb.delete(index)
        input_dialog = InputDialog(root, name, phone)
        root.wait_window(input_dialog.top)
        if input_dialog.result:
            new_name, new_phone = input_dialog.result
            lb.insert(index, f"{new_name}: {new_phone}")

def remove_data():
    selected_index = lb.curselection()
    if selected_index:
        index = selected_index[0]
        lb.delete(index)

class InputDialog:
    def __init__(self, parent, name="", phone=""):
        self.top = tk.Toplevel(parent)
        self.top.geometry("300x150")
        self.result = None

        tk.Label(self.top, text="Name:").pack()
        self.entry_name = tk.Entry(self.top)
        self.entry_name.pack()
        self.entry_name.insert(0, name)

        tk.Label(self.top, text="Phone:").pack()
        self.entry_phone = tk.Entry(self.top)
        self.entry_phone.pack()
        self.entry_phone.insert(0, phone)

        tk.Button(self.top, text="OK", command=self.ok).pack()

    def ok(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        self.result = (name, phone)
        self.top.destroy()

root = tk.Tk()
root.geometry("600x200")

f1 = tk.Frame(root)
f1.pack(fill=tk.BOTH, expand=1)
tk.Grid.columnconfigure(f1, 0, weight=2)
tk.Grid.columnconfigure(f1, 1, weight=2)
tk.Grid.rowconfigure(f1, 0, weight=1)

lb = tk.Listbox(f1, width=50)
lb.grid(row=0, column=0, columnspan=2, sticky="nsew")

f2 = tk.Frame(f1)
tk.Grid.columnconfigure(f2, 0, weight=1)
tk.Grid.columnconfigure(f2, 1, weight=1)
tk.Grid.columnconfigure(f2, 2, weight=1)
tk.Grid.rowconfigure(f2, 0, weight=1)
tk.Grid.rowconfigure(f2, 1, weight=1)
tk.Grid.rowconfigure(f2, 2, weight=1)
f2.grid(row=0, column=2, sticky="nsew")

button1 = tk.Button(f2, text="INSERT", bg="yellow", command=button_click_1)
button1.grid(row=0, column=0, sticky="nsew")

button2 = tk.Button(f2, text="DELETE", bg="yellow", command=button_click_2)
button2.grid(row=1, column=0, sticky="nsew")

button3 = tk.Button(f2, text="EDIT", bg="yellow", command=button_click_3)
button3.grid(row=2, column=0, sticky="nsew")

root.mainloop()
