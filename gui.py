# Import necessary modules
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from main import start_shiny_hunt

# Function to update the displayed images based on the selected Pokémon
def update_images(selected_pokemon):
    # Remove all existing image labels
    for label in image_labels:
        label.grid_forget()

    # Create a label for each selected Pokémon
    for i, pokemon in enumerate(selected_pokemon):
        # Open the corresponding image file and create a thumbnail
        image = Image.open(f"./Gen3ShinyEmerald/Shiny{pokemon}.png")
        image.thumbnail((150, 150))

        # Create a PhotoImage object from the thumbnail
        photo = ImageTk.PhotoImage(image)

        # Create a label widget with the PhotoImage object
        label = ttk.Label(images_frame, image=photo)
        label.image = photo

        # Add the label to the image frame in a 5-column grid
        label.grid(column=i % 5, row=i // 5)
        image_labels.append(label)

# Function to handle the listbox selection event
def on_select(event):
    # Get the selected indices and corresponding Pokémon names
    selected_indices = event.widget.curselection()
    selected_pokemon = [event.widget.get(i) for i in selected_indices]

    # Update the displayed images with the selected Pokémon
    update_images(selected_pokemon)

# Function to handle the "Start Hunting" button click event
def start_hunting():
    # Get the selected Pokémon names
    selected_pokemon = [listbox.get(i) for i in listbox.curselection()]

    # Print a message indicating the start of the shiny hunting process
    print(f"Starting shiny hunting for {', '.join(selected_pokemon)}")

    # Call the start_shiny_hunt function with the selected Pokémon names
    start_shiny_hunt(selected_pokemon)

# Create the main GUI window
app = tk.Tk()
app.title("Shiny Pokémon Hunter")

# Create a frame widget and add it to the main window
frame = ttk.Frame(app, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create a listbox widget and add it to the left column of the frame
listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE, exportselection=False)
listbox.grid(column=0, row=0)

# Get the names of all PNG files in the "./Gen3ShinyEmerald" directory
pokemon_names = [name[5:-4] for name in os.listdir("./Gen3ShinyEmerald") if name.endswith(".png")]

# Add the Pokémon names to the listbox widget
for pokemon in sorted(pokemon_names):
    listbox.insert(tk.END, pokemon)

# Register the on_select function as the event handler for listbox selection events
listbox.bind("<<ListboxSelect>>", on_select)

# Create a "Start Hunting" button and add it to the right column of the frame
start_button = ttk.Button(frame, text="Start Hunting", command=start_hunting)
start_button.grid(column=1, row=1)

# Create a frame widget to hold the image labels and add it to the right column of the frame
images_frame = ttk.Frame(frame, padding="10")
images_frame.grid(column=1, row=0)

# Create an empty list to hold the image labels
image_labels = []

# Start the main GUI loop
app.mainloop()
