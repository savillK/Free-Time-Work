answer = "lion king"
guesses = []
lives = 6
showcase = "_" * len(answer)
showcase = list(showcase)

for element in range(len(answer)):
    if answer[element] == " ":
        showcase[element] = " "

while 1:
    print((" ").join(showcase))
    print("Already Guessed Letters: " + str((", ").join(guesses)))
    print("Guess a letter")
    guess = input().lower()
    #if letter has already been guessed
    if guess in guesses:
print("Already guessed")
    #if letter has not been guessed
    else:
    #if letter is in solution
    if guess in answer:
        print("Correct")
        guesses.append(guess)
        indexes = []
        for i in range(len(answer)):
            if answer[i] == guess:
                indexes.append(i)
                    for i in indexes:
                        showcase[i] = guess
                            if "_" not in showcase:
                                print("You guessed it!")
                                break
                            #if guess is incorrect
else:
    guesses.append(guess)
    lives -= 1
        print("Incorrect")
        if lives < 0:
        print("you lose")
        break
            else:
                print(str(lives) + " lives left\n")
