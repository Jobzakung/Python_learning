from tkinter import *
import tkinter as tk
import random
import time

life = 3
secret_number = ''
secret_number_list = []
key = []


def generate_number():
    global life, secret_number, secret_number_list
    life = 3
    secret_number = str(random.randint(1000, 9999))

    secret_number_list.clear()  # clear list
    key.clear()  # clear list

    for i in secret_number:
        if i not in secret_number_list:
            secret_number_list.append(i)

    print("secret_number:", secret_number)
    print("secret_number_list:", secret_number_list)
    print("len:", len(secret_number_list))


def Stage1():
    global life, secret_number, secret_number_list
    c = 1
    count = 0
    while True:
        data = textCheck.get()
        if len(data) != 3:
            result_text["text"] = "Please enter only 3-digit number"
            print("Please enter only 3-digit number")
            return
        count += 1

        for i in secret_number_list:
            for j in data:
                if i == j:
                    if i not in key:
                        key.append(i)
                        c += 1
        print("key:", key, "secret_number_list:", secret_number_list)
        if len(key) == len(secret_number_list):
            result_text["text"] = "Congratulations! You guessed the correct number!"
            print("Congratulations! You guessed the correct number!")
            life += 3
            print("life final:", life)
            label_life["text"] = "Life: " + str(life)
            textCheck.delete(0, END)  # Clear the text in the entry widget
            exec_Button["command"] = Stage2
            # play_Stage2()
            break
        else:
            life -= 1
            print("life final:", life)
            label_life["text"] = "Life: " + str(life)
            break


def Stage2():
    global life, secret_number, secret_number_list, key
    count = 0
    data = textCheck.get()
    if len(data) != 4:
        result_text["text"] = "Please enter only 4-digit number"
        print("Please enter only a 4-digit number")
        return
    count += 1

    if int(data) == int(secret_number):
        result_text["text"] = "Congratulations! You guessed the correct number!"
        print("Congratulations! You guessed the correct number!")
        print("life final:", life)
        time.sleep(10)
        windows.destroy()
        return  # Exit the function and end the game
    else:
        life -= 1
        print("life final:", life)
        label_life["text"] = "Life: " + str(life)
        result = abs(int(data) - int(secret_number))
        if life == 0:
            result_text["text"] = "Game Over! You have run out of lives."
            result_text["text"] = "The correct number was:", secret_number
            print("Game Over! You have run out of lives.")
            print("The correct number was:", secret_number)
        elif count > 3:
            print(
                "Game Hint: You have exceeded the allowed number of guesses. Try to guess smarter!")
        elif result <= 10:
            print("You are getting close!")
        elif int(data) < int(secret_number):
            print("Your guess is too small.")
        elif int(data) > int(secret_number):
            print("Your guess is too high.")



windows = tk.Tk()
windows.geometry("350x450")
windows.title("Guess the number")

Title = tk.Label(windows, text="Guess the number")
Title.pack()

textCheck = tk.Entry(windows)
textCheck.pack()

exec_Button = tk.Button(windows, text="Exec", command=Stage1)
exec_Button.pack()

label_life = tk.Label(windows, text="Life: " + str(life))
label_life.pack()

generate_button = tk.Button(
    windows, text="Generate Number", command=generate_number)
generate_button.pack()

result_text = tk.Label(windows, text="")
result_text.pack()

tk.mainloop()
