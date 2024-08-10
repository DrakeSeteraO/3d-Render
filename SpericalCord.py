import math
class SpericalCord:
    
    def __init__(self, XCord, YCord, ZCord):
        self.XCord = float(XCord)
        self.YCord = float(YCord)
        self.ZCord = float(ZCord)
        
    def getRhoCord(self):
        self.rho = self.XCord * self.XCord + self.YCord * self.YCord + self.ZCord * self.ZCord
        self.rho = math.sqrt(self.rho)
        return self.rho
    
    def getThetaCord(self):
        if self.XCord > 0:
            self.theta = math.atan(self.YCord / self.XCord)
        elif self.XCord < 0:
            self.theta = math.atan(self.YCord / self.XCord) + math.pi
        elif self.XCord == 0:
            self.theta = math.pi / 2
        return self.theta
    
    def getTheeCord(self):
        self.thee =  math.acos(self.ZCord / self.rho)
        return self.thee
    
    def getSphericalCords(self):
        return str(self.getRhoCord()) + "," + str(self.getThetaCord()) + "," + str(self.getTheeCord())
    
    
class SphericalSquareCord:
    
    def __init__(self, Cord1X, Cord1Y, Cord1Z, distanceA, distanceB, dimensions ):
        self.Cord1X = float(Cord1X)
        self.Cord1Y = float(Cord1Y)
        self.Cord1Z = float(Cord1Z)
        self.distanceA = float(distanceA)
        self.distanceB = float(distanceB)
        self.dimensions = str(dimensions)
        
        if self.dimensions.upper() == "XY":
            self.Cord1 = SpericalCord(self.Cord1X, self.Cord1Y, self.Cord1Z)
            self.Cord2 = SpericalCord(self.Cord1X + self.distanceA, self.Cord1Y, self.Cord1Z)
            self.Cord3 = SpericalCord(self.Cord1X + self.distanceA, self.Cord1Y + self.distanceB, self.Cord1Z)
            self.Cord4 = SpericalCord(self.Cord1X, self.Cord1Y + self.distanceB, self.Cord1Z)
            
        elif self.dimensions.upper() == "YZ":
            self.Cord1 = SpericalCord(self.Cord1X, self.Cord1Y, self.Cord1Z)
            self.Cord2 = SpericalCord(self.Cord1X, self.Cord1Y + self.distanceA, self.Cord1Z)
            self.Cord3 = SpericalCord(self.Cord1X, self.Cord1Y + self.distanceA, self.Cord1Z + self.distanceB)
            self.Cord4 = SpericalCord(self.Cord1X, self.Cord1Y, self.Cord1Z + self.distanceB)
            
        elif self.dimensions.upper() == "XZ": 
            self.Cord1 = SpericalCord(self.Cord1X, self.Cord1Y, self.Cord1Z)
            self.Cord2 = SpericalCord(self.Cord1X + self.distanceA, self.Cord1Y, self.Cord1Z)
            self.Cord3 = SpericalCord(self.Cord1X + self.distanceA, self.Cord1Y, self.Cord1Z + self.distanceB)
            self.Cord4 = SpericalCord(self.Cord1X, self.Cord1Y, self.Cord1Z + self.distanceB)
            
    def getSphericalCords(self):
        return self.Cord1.getSphericalCords() + "/" + self.Cord2.getSphericalCords() + "\n" + self.Cord2.getSphericalCords() + "/" + self.Cord3.getSphericalCords() + "\n" + self.Cord3.getSphericalCords() + "/" + self.Cord4.getSphericalCords() + "\n" + self.Cord1.getSphericalCords() + "/" + self.Cord4.getSphericalCords()
    
    
class SphericalCubeCord:
    
    def cordsToLine(self, x1, y1, z1, x2, y2, z2):
        cord1 = SpericalCord(x1,y1,z1)
        cord2 = SpericalCord(x2, y2, z2) 
        return cord1.getSphericalCords() + "/" + cord2.getSphericalCords()
    
    def __init__(self, CordX, CordY, CordZ, distanceX, distanceY, distanceZ ):
        self.CordX = float(CordX)
        self.CordY = float(CordY)
        self.CordZ = float(CordZ)
        self.distanceX = float(distanceX)
        self.distanceY = float(distanceY)
        self.distanceZ = float(distanceZ)
        
        self.bottomSquare = SphericalSquareCord(self.CordX, self.CordY, self.CordZ, self.distanceX, self.distanceY, "XY")
        self.topSquare = SphericalSquareCord(self.CordX, self.CordY, self.CordZ + self.distanceZ, self.distanceX, self.distanceY, "XY")
        
        self.line1 = self.cordsToLine(self.CordX, self.CordY, self.CordZ, self.CordX, self.CordY, self.CordZ + self.distanceZ)
        self.line2 = self.cordsToLine(self.CordX + self.distanceX, self.CordY, self.CordZ, self.CordX + self.distanceX, self.CordY, self.CordZ + self.distanceZ)
        self.line3 = self.cordsToLine(self.CordX, self.CordY + self.distanceY, self.CordZ, self.CordX, self.CordY + self.distanceY, self.CordZ + self.distanceZ)
        self.line4 = self.cordsToLine(self.CordX + self.distanceX, self.CordY + self.distanceY, self.CordZ, self.CordX + self.distanceX, self.CordY + self.distanceY, self.CordZ + self.distanceZ)
    
    def getSphericalCords(self):
        return self.bottomSquare.getSphericalCords() + "\n" + self.topSquare.getSphericalCords() + "\n" + self.line1 + "\n" + self.line2 + "\n" + self.line3 + "\n" + self.line4 
