import tkinter as tk
from PIL import Image, ImageTk

# create the main window
root = tk.Tk()
root.geometry("500x500")
root.title("Pokemon Shiny Sprites")
root.resizable(False, False)

# load the images
bulbasaur_image = Image.open("./Gen3ShinyEmerald/ShinyBulbasaur.png")
zubat_image = Image.open("./Gen3ShinyEmerald/ShinyZubat.png")

# create the ImageTk objects
bulbasaur_photo = ImageTk.PhotoImage(bulbasaur_image)
zubat_photo = ImageTk.PhotoImage(zubat_image)

# create a canvas to display the images
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# display the first image (Bulbasaur)
canvas.create_image(250, 250, image=bulbasaur_photo)

# function to switch between images
def switch_image():
    current_image = canvas.itemcget(canvas.find_all()[0], "image")
    if current_image == str(bulbasaur_photo):
        canvas.itemconfig(canvas.find_all()[0], image=zubat_photo)
    else:
        canvas.itemconfig(canvas.find_all()[0], image=bulbasaur_photo)

# create a button to switch between images
switch_button = tk.Button(root, text="Switch Image", command=switch_image)
switch_button.pack()
switch_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# start the main event loop
root.mainloop()
