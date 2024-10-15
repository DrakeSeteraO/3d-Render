import math

class PixelMath:
    def convertDegreesToRadians(self, degrees):
        return degrees / 180 * math.pi
    
    
    def createList(self, pixelAmount, startValue, endValue):
        increment = (endValue - startValue) / pixelAmount
        list = [startValue]
        
        currentValue = startValue
        while currentValue <= endValue:
            currentValue += increment
            list.append(currentValue)
        
        return list
           
    
    def updateTheta(self):
        self.leftRadian = (self.centerTheta) + self.radianHalfPOV
        self.rightRadian = (self.centerTheta) - self.radianHalfPOV
        self.thetaList = self.createList(self.screenPixelWidth, self.rightRadian, self.leftRadian)
        
        
    def updateThee(self):
        self.downRadian = (self.centerThee) + self.radianHalfPOV
        self.upRadian = (self.centerThee) - self.radianHalfPOV
        self.theeList = self.createList(self.screenPixelHeight, self.upRadian, self.downRadian)
    
    
    def __init__(self, pixelWidth, pixelHeight, POV):
        self.screenPixelWidth = pixelWidth
        self.screenPixelHeight = pixelHeight
        self.POV = POV
        
        self.halfPOV = self.POV / 2
        self.radianHalfPOV = self.convertDegreesToRadians(self.halfPOV)
        
        self.centerTheta = math.pi / 2
        self.updateTheta()
    
        self.centerThee = math.pi / 2
        self.updateThee()
        
        
        
    def getThetaList(self):
        return self.thetaList
    
    
    def getTheeList(self):
        return self.theeList
    
    
    def findLocation(self, list, angle):
        middle = int(len(list) / 2)
        pixelFound = False
        foundValue = 0
        distance = int(middle / 2)
        try:
            runAmount = 0
            while pixelFound == False:
                # print(middle)
                if runAmount >= 50:
                    pixelFound = True
                    foundValue = -1
                
                if list[middle] <= float(angle) and list[middle + 1] >= float(angle):
                    foundValue = middle
                    pixelFound = True
                    # print("Yes!")
                
                elif middle >= len(list) or middle < 0:
                    foundValue = -1
                    pixelFound = True
                    # print("Out of bounds")
                        
                elif list[middle] <= float(angle):
                    middle += distance
                    distance = int(distance / 2)
                    # print("too small")
                    
                elif list[middle] >= float(angle):
                    middle -= distance
                    distance = int(distance / 2)
                    # print("too big")
                
                if distance <= 0:
                    distance = 1
                    
                runAmount += 1    
        except:
            print("There was a problem")
            foundValue = -1
            
        return foundValue
      
    
    def getScreenCords(self, theta, thee):
        thetaPixel = self.findLocation(self.thetaList, theta)
        thetaPixel = self.screenPixelWidth - thetaPixel
        theePixel = self.findLocation(self.theeList, thee)
        return str(thetaPixel) + "," + str(theePixel)
        
    
    def setCenterTheta(self, newTheta):
        self.centerTheta = newTheta % (2 * math.pi) 
        self.updateTheta()  
        
        
    def setCenterThee(self, newThee):
        self.centerThee = newThee % (2 * math.pi)
        self.updateThee() 
        
        
    def addCenterTheta(self, addTheta):
        self.centerTheta += addTheta
        self.centerTheta = self.centerTheta % (2 * math.pi)
        
        self.updateTheta() 
        
        
    def addCenterThee(self, addThee):
        self.centerThee += addThee
        self.centerThee = self.centerThee % (2 * math.pi)
        
        self.updateThee() 