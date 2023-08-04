text = ["яблуко", "груша", "слива", "абрикос", "вишня", "черешня", "персик", "калина"]  #field_of_miracles
import random
word = random.choice(text)
word = word.lower()
length_word = len(word)
word1 = ""
for i in word:
    i = "*"
    word1 = word1 + i
print(word, type(word), word1, type(word1))
number_of_attempts = input("Enter number of attempts word: ")

if number_of_attempts.isdigit():
    number_of_attempts = int(number_of_attempts)
    attempt_number = 0
    while attempt_number in range(0, number_of_attempts):
        if attempt_number in range(0, number_of_attempts):
            attempt = input("Enter word or letter : ")
            attempt = attempt.lower()
            length_attempt = len(attempt)
            if length_attempt > 1:
                if attempt == word:
                    print("Congratulations, you guessed the word")
                    exit()
                else:
                    attempt_number += 1
                    print(f"The word is not correct, {number_of_attempts - attempt_number} attempts left")
            elif length_attempt == 1:
                if attempt in word:
                    for i in range(0, length_word):
                        if attempt == word[i]:
                            word1 = word1[:i] + word[i] + word1[i+1:]
                            print(f"{word1}, {number_of_attempts - attempt_number} attempts left")
                else:
                    attempt_number += 1
                    print(f"There is no letter, {number_of_attempts - attempt_number} attempts left")

    print("You lose, game over , 0 attempts left")
else:
    print("Error when entering a number, game over")
