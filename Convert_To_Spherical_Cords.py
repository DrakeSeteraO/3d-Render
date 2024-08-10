from SpericalCord import SpericalCord,SphericalSquareCord,SphericalCubeCord

fileName = input("What file would you like to change? ")

try:

    file = open(fileName, "at")

    addAnother = True
    while addAnother == True:
        User_input = input("\nWould you like to add another coordinate?\nNo: N\nLine: L\nSquare: S\nCube: C\n")
        if User_input.upper() == "N":
            addAnother = False
        elif User_input.upper() == "L":
            
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
            
        elif User_input.upper() == "S":
            
            validInput = False
            while validInput == False:
                input1 = input("\nPlease provide a corner of the square in x,y,z form: ")
                cord1 = input1.split(",")
                
                if len(cord1) >= 3:
                    validInput = True
            
            validInput = False
            while validInput == False:
                input2 = input("\nPlease provide a distance from the corner in x,y,z form: ")
                cord2 = input2.split(",")
                
                if len(cord2) >= 3:
                    validInput = True
            
            if float(cord2[0]) > 0:
                if float(cord2[1]) > 0:
                    square = SphericalSquareCord(float(cord1[0]), float(cord1[1]), float(cord1[2]), float(cord2[0]), float(cord2[1]), "xy")
                elif float(cord2[2]) > 0:
                    square = SphericalSquareCord(float(cord1[0]), float(cord1[1]), float(cord1[2]), float(cord2[0]), float(cord2[2]), "xz")
                else:
                    print("There was an error")
            elif float(cord2[1]) > 0:
                if float(cord2[2]) > 0:
                    square = SphericalSquareCord(float(cord1[0]), float(cord1[1]), float(cord1[2]), float(cord2[1]), float(cord2[2]), "yz")
                else:
                    print("There was an error")
            
            file.write(square.getSphericalCords() + "\n")
            
        elif User_input.upper() == "C":
            
            validInput = False
            while validInput == False:
                input1 = input("\nPlease provide a corner of the cube in x,y,z form: ")
                cord1 = input1.split(",")
                
                if len(cord1) >= 3:
                    validInput = True
            
            validInput = False
            while validInput == False:
                input2 = input("\nPlease provide a distance from the corner in x,y,z form: ")
                cord2 = input2.split(",")
                
                if len(cord2) >= 3:
                    validInput = True
            
            cube = SphericalCubeCord(float(cord1[0]),float(cord1[1]),float(cord1[2]),float(cord2[0]),float(cord2[1]),float(cord2[2]))
            file.write(cube.getSphericalCords() + "\n")
            
        else:
            print("\nThere was an error please try again")

    file.close()

except:
    print("There was an error with the file\n")

