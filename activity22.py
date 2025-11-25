import random

print("WELCOME TO THE GUESSING GAME!")
print("==============================")

random_value = random.randint(1,10)
tries = 0
conti = True

while conti == True:
    num = eval(input("Hi there! Please guess a random number from 1-10 to win exciting prizes! --> "))

    tries += 1
    if num == random_value:
        print("WOW, YOU WON A BRAND NEW IPHONE 17 PRO BRAND NEW FULLY PAID!")
        print(f"The random value is {random_value}")
        break
    else:
        print("Sorry, You're wrong. Please try again. ")
        continue