# Import Modules
import tkinter as tk

# Create root Window
root = tk.Tk();

# Title Bar for Window
root.title("Character Sheet");

width = 1280; # Width 
height = 720; # Height
 
screen_width = root.winfo_screenwidth();  # Width of the screen
screen_height = root.winfo_screenheight(); # Height of the screen
 
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2);
y = (screen_height/2) - (height/2);
 
root.geometry('%dx%d+%d+%d' % (w, h, x, y));

# start the window
root.mainloop();