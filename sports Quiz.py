print("Welcome to my computer quiz bud!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play:) ")
score = 0

answer = input("When Michael Jordan retired in 2003, how many NBA Championships did he win?? ")
if answer == "6":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How old was Tiger Woods when he won the Masters? ")
if answer == "21":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer= input("How many SuperBowls has Tom Brady won? ")
if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which NBA team has the most NBA Finals appearances?")
if answer== "Lakers":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + "questions correct!")
print("You got " + str((score / 4) * 100) + "%.")

