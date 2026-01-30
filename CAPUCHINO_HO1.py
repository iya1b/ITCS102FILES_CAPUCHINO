def get_ave(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def compare(length, average, word):
    if average > length:
        print(f"The length of the word '{word}' is less than the average.")
    elif average < length:
        print(f"The length of the word '{word}' is greater than the average.")
    else:
        print(f"The length of the word '{word}' is equal to the average.")


word = input("Please enter a word --> ")
iya = len(word)

banana = []
for i in range(1, iya + 1):
    ask = int(input(f"Please enter a number {i}: "))
    banana.append(ask)

print(banana)
print(f"The length of the word you provided is {iya}")

ave = get_ave(banana)
print(f"The average of the numbers you provided is {ave}")

compare(iya, ave, word)
