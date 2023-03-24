import random

num_digest = 3
max_guess = 10


def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    SecretNum = ""
    for i in range(num_digest):
        SecretNum = SecretNum + str(numbers[i])
    return SecretNum


def getClues(guess, SecretNum):
    if guess == SecretNum:
        return "Побда!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == SecretNum[i]:
            clues.append("Горячо")
        elif guess[i] in SecretNum:
            clues.append("Тепло")

    if len(clues) == 0:
        return "Холодно"

    clues.sort()
    return " ".join(clues)


def isOnlyDigits(num):
    if num == "":
        return False

    if i in num:
        if i not in "0 1 2 3 4 5 6 7 8 9".split():
            return False

    return True


print(f"Я загадал {num_digest} значное число")
print(f"У тебя {max_guess} попыток")

while True:
    SecretNum = getSecretNum()
    guessesTaken = 1
    while guessesTaken <= max_guess:
        guess = ""

        while len(guess) != num_digest or not isOnlyDigits(guess):
            print(f"Попыток №{guessesTaken}")
            guess = input()
        print(getClues(guess, SecretNum))
        guessesTaken = guessesTaken + 1

        if guess == SecretNum:
            break

        if guessesTaken > max_guess:
            print(f"Попытки закончились. Я загадал чилсо {SecretNum}")

    print("Хотите сыграть еще раз? (да или нет)")
    if not input().lower().startwith("д"):
        break