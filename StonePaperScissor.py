import random

options = {"Paper" : 0, "Stone" : 1, "Scissor" : 2}
options1 = ["Stone", "Paper", "Scissor"]
Point = 0
Point1 = 0
print ("Welcome Player...")
while True :
    num = random.randint(0, 2)

    chosen = input("Enter your choice : ")
    com = options1[num]

    if options[chosen] == 0 :
        if options[com] == 1 :
            print("Computer Choosed : " + com)
            print("You Won!")
            Point += 1
        elif options[com] == 2 :
            print("Computer Choosed : " + com)
            print("Sorry! You Lose.")
            Point1 += 1
        elif options[com] == 0 :
            print("Computer Choosed : " + com)
            print("It is a Draw.")
    elif options[chosen] == 1 :
        if options[com] == 2 :
            print("Computer Choosed : " + com)
            print("You Won!")
            Point += 1
        elif options[com] == 0 :
            print("Computer Choosed : " + com)
            print("Sorry! You Lose.")
            Point1 += 1
        elif options[com] == 1 :
            print("Computer Choosed : " + com)
            print("It is a Draw.")
    elif options[chosen] == 2 :
        if options[com] == 0 :
            print("Computer Choosed : " + com)
            print("You Won!")
            Point += 1
        elif options[com] == 1 :
            print("Computer Choosed : " + com)
            print("Sorry! You Lose.")
            Point1 += 1
        elif options[com] == 2 :
            print("Computer Choosed : " + com)
            print("It is a Draw.")
    a = input("Do you want to play again? (y/n) : ")
               
    if a == "n" or a == "N" :
        print("Thank you!!")
        break

print("Your Point is : " + str(Point))
print("Computer point is : " + str(Point1))
input()
exit
