from PIL import Image
from UpdateScreen import UpdateScreen
from PixelMath import PixelMath
from time import perf_counter

pixelWidth = int(input("what would you like the image width to be? "))
pixelHeight = int(input("what would you like the image height to be? "))

POV = float(input("What would you like your FOV to be? "))

fileName = input("What file would you like to view? ")

# Start timer
start_time = perf_counter()
try:
    screen = UpdateScreen(pixelWidth, pixelHeight, POV, fileName)
except:
    file = open(fileName, "at")
    file.close()


screen.displayScreen()

# Time program took to run
passed_time = (perf_counter() - start_time) * 1000
print(f"It took {passed_time} ms")