# Import Modules
from tkinter import *

# Create root Window
root = Tk();

# Title Bar for Window
root.title("Character Sheet")

# Defualt Window size
w = 1280;
h = 720;

# Add creation location for the window
#grab window size
scWidth = root.winfo_screenmmwidth;
scLength = root.winfo_screenheight;

# Set position of window
xOrigin = (scWidth/2) - (w/2);
yOrigin = (scLength/2) - (h/2);

# Set size and position of window
root.geometry('%dx%d+%d+%d' % (w, h, xOrigin, yOrigin))

# start the window
root.mainloop();