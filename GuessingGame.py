Secret_Word = "Predators"
Guess = ""
Guess_Count = 0
Guess_Limit = 5
Out_Of_Guesses = False

Hint = print("Flesh eating animals.")

while Guess != Secret_Word and not(Out_Of_Guesses):
    if Guess_Count < Guess_Limit:
        Guess = input("Enter the secret word: ")
        Guess_Count += 1


    else:
        Out_Of_Guesses = True

if Out_Of_Guesses:
    print("Out of Guess, YOU LOOSE!")

else:
    print("YOU WIN!")
