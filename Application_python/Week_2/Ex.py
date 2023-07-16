import random

life = 3
secret_number = ''
secret_number_list = []
key = []


def generate_number():
    global life, secret_number, secret_number_list
    life = 3
    secret_number = str(random.randint(1000, 9999))

    secret_number_list.clear() # clear list
    key.clear() # clear list

    for i in secret_number:
        if i not in secret_number_list:
            secret_number_list.append(i)

    print("secret_number:", secret_number)
    print("secret_number_list:", secret_number_list)
    print("len:", len(secret_number_list))


def play_Stage1():
    global life, secret_number, secret_number_list, key

    count_key = 1
    count = 0

    while True:
        data = input("Enter your guess (3-digit number): ")
        if len(data) > 3:
            print("Please enter only 3-digit number")
            continue
        count += 1

        for i in secret_number_list:
            for j in data:
                if i == j:
                    if i not in key:
                        key.append(i)
                        count_key += 1
        if len(key) == len(secret_number_list):
            print("Congratulations! You guessed the correct number!")
            life += 3
            print("life final:", life)
            play_Stage2()
            break
        else:
            life -= 1
            print("life final:", life)



def play_Stage2():
    global life, secret_number, secret_number_list, key
    count = 0
    print("Now playing Stage 2:\n")
    print("secret_number:", secret_number)
    print("secret_number_list:", secret_number_list)
    print("len:", len(secret_number_list))
    
    while True:
        data = input("Enter your guess (4-digit number): ")
        if len(data) != 4:
            print("Please enter only a 4-digit number")
            continue
        count += 1

        if int(data) == int(secret_number):
            print("Congratulations! You guessed the correct number!")
            print("life final:", life)
            break
        else:
            life -= 1
            print("life final:", life)
            result = abs(int(data) - int(secret_number))
            if life == 0:
                print("Game Over! You have run out of lives.")
                print("The correct number was:", secret_number)
                break
            elif count > 3:
                print("Game Hint: You have exceeded the allowed number of guesses. Try to guess smarter!")
            elif result <= 10:
                print("You are getting close!")
            elif int(data) < int(secret_number):
                print("Your guess is too small.")
            elif int(data) > int(secret_number):
                print("Your guess is too high.")


generate_number()
play_Stage1()