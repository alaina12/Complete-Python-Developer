#This project will help you to convert the jpg images to png form 
#Importing all the neccessary modules

import sys
import os
from PIL import Image 

#getting the arguments from the user
JPG_folder = sys.argv[1]
PNG_folder = sys.argv[2]

#check if the png folder already exists
if os.path.exists(PNG_folder):
    pass 