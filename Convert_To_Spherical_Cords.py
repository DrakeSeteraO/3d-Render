from SpericalCord import SpericalCord

fileName = input("What file would you like to change? ")
try:
    file = open(fileName, "at")

    addAnother = True
    while addAnother == True:
        User_input = input("\nWould you like to add another coordinate? (y/n)")
        if User_input.upper() == "N":
            addAnother = False
        elif User_input.upper() == "Y":
            
            validInput = False
            while validInput == False:
                input1 = input("\nPlease provide a x,y,z cord: ")
                cord1 = input1.split(",")
                
                if len(cord1) >= 3:
                    validInput = True
            
            validInput = False
            while validInput == False:
                input2 = input("\nPlease provide a x,y,z cord that the previous one is connected to: ")
                cord2 = input2.split(",")
                
                if len(cord2) >= 3:
                    validInput = True
            
            
            SCord1 = SpericalCord(cord1[0], cord1[1], cord1[2])
            SCord2 = SpericalCord(cord2[0], cord2[1], cord2[2])
            
            file.write(SCord1.getSphericalCords() + "/" + SCord2.getSphericalCords() + "\n")
            
        else:
            print("\nThere was an error please try again")

    file.close()
except:
    print("There was an error with the file\n")
