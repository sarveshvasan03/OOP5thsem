#Write a function called hexagon_area that takes the length of a side of a 
#regular hexagon as a parameter and returns the area of the hexagon
import numpy as np
def hexagon_area(side):
  area=np.sqrt(3)*(3/2)*side**2;
  return area;
a=int(input("Enter the side length of hexagon: "))
hexagon_area(a)
