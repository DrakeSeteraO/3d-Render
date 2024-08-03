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
    
    def __init__(self, Cord1A, Cord1B, distanceA, distanceB ):
        self.Cord1A = float(Cord1A)
        self.Cord1B = float(Cord1B)
        self.distanceA = float(distanceA)
        self.distanceB = float(distanceB)
