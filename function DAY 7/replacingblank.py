import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f'Pssst, the solution is {chosen_word}.')
display = []
for _ in range(word_length):
    display += "_"
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for postion in range(word_length):
        letter = chosen_word[postion]
        if letter == guess:
            display[postion] = letter
    print(display)
    
    if "_" in display:
        end_of_game = True
        print("you win")