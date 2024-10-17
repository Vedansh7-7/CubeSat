# Libraries
import tkinter as tk

# Functions
def on_click():
    button.config(text= "NOK")

# Main skeleton structure
Main = tk.Tk()
Main.geometry("500x500")

# Widgets
button = tk.Button(Main, text="Quit", command = Main.destroy)
button.pack(side= tk.BOTTOM , anchor= 'e')  # "se" = south-east (bottom-right)

button2 = tk.Button(Main, text="OK", command = on_click, )
button2.pack(side= tk.BOTTOM , anchor='e')

# Loop()
Main.mainloop()
