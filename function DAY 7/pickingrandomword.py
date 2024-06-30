import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choices(word_list)
guess = input("guess the letter: ").lower()
for letter in chosen_word:
    if letter == guess:
        print("correct")
    else:
        print("wrong")