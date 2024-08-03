from PIL import Image
from UpdateScreen import UpdateScreen
from PixelMath import PixelMath
import math

pixelWidth = int(input("what would you like the image width to be? "))
pixelHeight = int(input("what would you like the image height to be? "))

POV = float(input("What would you like your POV to be? "))

fileName = input("What file would you like to view? ")

screen = UpdateScreen(pixelWidth, pixelHeight, POV, fileName)


screen.displayScreen()



