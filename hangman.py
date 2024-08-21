word = ['c', 'o', 'd', 'e']

guessed = [ ]

incorrect = 0

guessedcorrectly = 1

correct = False

length = len(word)

print(f"this word has {length} letters")

while correct == False:
    guess = input("guess a letter: ")
    if guessedcorrectly == length:
        correct = True
        break
    elif incorrect == 7:
        print("he died rip :( the word was: code")
        exit()
    elif guess in guessed:
        print("you already guessed this letter!")
    elif guess in word:
        guessed.append(guess)
        num = word.index(guess) + 1
        guessedcorrectly = guessedcorrectly + 1
        print(f"{guess} is letter {num}")
        print(f"letters guessed: {guessed}")
    else:
        guessed.append(guess)
        print(f"that letter isn't in the word")
        print(f"letters guessed: {guessed}")
        incorrect = incorrect + 1
        
if correct == True:
    print("you guessed the word! :)")
