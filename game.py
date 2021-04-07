import random #imports needed libraries (I think)
GuessingList = ["bobgood","waterbottle","dishwasher","flashlight","somethingCool"]
GuessingRC = random.choice(GuessingList)
Lives = 16
Guessed = False
while Guessed == False:
    print("Enter a guess:")
    userinput = input()
    GuessingRC = GuessingRC.upper()
    if GuessingRC.find(str(userinput.upper())) == -1:
        Lives = Lives - 1
        print("WRONG")
        print("You Have " + str(Lives) + " Guesses Left")
        if Lives == 0:
            print("You lost")
            Guessed = True
    else:
        if userinput.upper() == GuessingRC.upper():
            print("You just won the game!")
            Guessed = True
        else:
            print("Looks like you got something right!")
            print("Errr... Its not exact though. Try guessing.")
