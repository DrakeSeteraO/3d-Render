from PixelMath import PixelMath
from PIL import Image, ImageDraw

class UpdateScreen:
    def getSphericalCords(self, fileName):
        self.file = open(fileName, "rt")
        self.fileLine = []
        
        for i in self.file:
           self.fileLine.append(i)
        self.file.close()
        
        self.sphericalCord1 = []
        self.sphericalCord2 = []
        
        for n in self.fileLine:
            parts = n.split("/")
            self.sphericalCord1.append(parts[0])
            self.sphericalCord2.append(parts[1])
          
            
    def getIndividualSphericalCords(self):
        self.rhoCord1 = []
        self.thetaCord1 = []
        self.theeCord1 = []
        
        for u in self.sphericalCord1:
            parts = u.split(",")
            self.rhoCord1.append(parts[0])
            self.thetaCord1.append(parts[1])
            self.theeCord1.append(parts[2])
        
        self.rhoCord2 = []
        self.thetaCord2 = []
        self.theeCord2 = []
        
        for v in self.sphericalCord2:
            parts = v.split(",")
            self.rhoCord2.append(parts[0])
            self.thetaCord2.append(parts[1])
            self.theeCord2.append(parts[2])
            
            
    def getScreenCords(self):
        self.screenCords1 = []
        self.screenCords2 = []
        
        i = 0
        while i < len(self.thetaCord1):
            self.screenCords1.append(self.ScreenMath.getScreenCords(self.thetaCord1[i], self.theeCord1[i]))
            self.screenCords2.append(self.ScreenMath.getScreenCords(self.thetaCord2[i], self.theeCord2[i]))
            i += 1
            
        
    def __init__(self, pixelWidth, pixelHeight, POV, fileName):
        self.screenPixelWidth = pixelWidth
        self.screenPixelHeight = pixelHeight
        self.POV = POV
        self.fileName = fileName
        
        self.ScreenMath = PixelMath(pixelWidth, pixelHeight, POV)
        self.getSphericalCords(fileName)
        self.getIndividualSphericalCords()
        self.getScreenCords()
        
        
    def setTheta(self, newTheta):
        self.ScreenMath.setCenterTheta(newTheta)
        self.getScreenCords()
        
        
    def setThee(self, newThee):
        self.ScreenMath.setCenterThee(newThee)  
        self.getScreenCords()  
    
      
    def addTheta(self, addTheta):
          self.ScreenMath.addCenterTheta(addTheta)
          self.getScreenCords()
          
          
    def addThee(self, addThee):
          self.ScreenMath.addCenterThee(addThee)
          self.getScreenCords()
          
          
    def getPixelCords(self, theta, thee):
        return self.ScreenMath.getScreenCords( theta, thee)
    
    
    def renderLines(self):
        i = 0
        
        while i < len(self.screenCords1):
            
            parts1 = self.screenCords1[i].split(",")
            parts2 = self.screenCords2[i].split(",")
            
            if float(parts1[0]) >= 0 and float(parts1[1]) >= 0 and float(parts2[0]) >= 0 and float(parts2[1]) >= 0 and float(parts1[0]) < self.screenPixelWidth and float(parts1[1]) < self.screenPixelHeight and float(parts2[0]) < self.screenPixelWidth and float(parts2[1]) < self.screenPixelHeight:
                self.draw.line([(int(parts1[0]),int(parts1[1])), (int(parts2[0]),int(parts2[1]))], fill = 255, width = 1)
                
            i += 1
    
    
    def displayScreen(self):
        self.getScreenCords()
        self.image = Image.new(mode = "1", size = (self.screenPixelWidth, self.screenPixelHeight))
        self.draw = ImageDraw.Draw(self.image)
        
        self.renderLines()
        self.image.show()

