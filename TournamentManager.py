ADMINUsr = "ADMIN"
ADMINPdw = "676767"

allParticipant = [[],
                  []] 

yellowPart = [[],
              []]

redPart = [[],
           []]

greenPart = [[],
             []]

bluePart = [[],
            []]

print("1. Register Participant")
print("2. Record Event Result")
print("3. Search Participant")
print("4. Display Event Result")
print("5. Display Hour Leaderboard")
print("6. Display tournament Statistics ")
print("7. Update Results [ADMIN]")
print("8. Export Final Report")
print("9. Exit")

def register():
    print("---------Participant Registeration Portal---------")
    name = input("Participant Name:")
    #House Selection
    print(" House Selection \n1. Red\n2. Green\n3. Blue\n4. Yellow")
    while True:
        house = int(input("Select House:"))

        if house == 1:
             house = "Red"
             break
        elif house == 2:
             house = "Green"
             break
        elif house == 3:
             house = "Blue"
             break
        elif house == 4:
             house = "Yellow"
             break
        else:
             print("Invalid Response")

    while True: 
        yeargroup = int(input("Input Yeargroup (7 - 13):"))
        if yeargroup >= 7 and yeargroup <= 13 :
             break

        else: 
             print("Invalid Year Group.")


        

    
    



def adminLogin ():
        tries = 3
        for i in range(tries):
            print("Admin Login Portal")
            AdminUser = input("Username:")
            AdminPassword = input("Password:")
            if AdminPassword == ADMINPdw and AdminUser == ADMINUsr:
                print("Login Sucessful")
                break

            else:
                print("User or Password incorrect")
                print(f"{tries - 1} trials left")
                tries = tries -1

        print("Too Many Failed Attempts")




      
# userSelection = int(input("Menu Selection:"))

register()
