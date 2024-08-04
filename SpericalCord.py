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
        if self.XCord >= 0:
            self.theta = math.atan(self.YCord / self.XCord)
        elif self.XCord < 0:
            self.theta = math.atan(self.YCord / self.XCord) + math.pi
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
    
    

        
    
