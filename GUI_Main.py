# Libraries
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Functions

# Function to validate login credentials
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Simple hardcoded credentials for demonstration
    if username == "admin" and password == "password123":
        messagebox.showinfo("Login", "Login Successful!")
        login_frame.grid_forget()
        show_frame(main_Frame)
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

def on_click():
    if button2['text'] == "OK":
        button2.config(text="NOK")
    else:
        button2.config(text="OK")

# Main skeleton structure
Main = tk.Tk()
Main.geometry("500x500")
Main.grid_columnconfigure(0, weight=1)  # Configure main window's single column to expand
Main.grid_rowconfigure(0, weight=1)     # Configure main window's single row to expand

# --- Frames ---
login_frame = tk.Frame(Main, bg='#1C191C')
main_Frame = tk.Frame(Main, bg="Black")

# Place both frames on top of each other
for frame in (login_frame, main_Frame):
    frame.grid(row=0, column=0, sticky='nsew')

# --- Login Frame ---
login_frame.grid_columnconfigure(0, weight=1)  # Make widgets centered
login_label = tk.Label(login_frame, text="Login Page", font=('Helvetica', 18), bg='lightblue')
login_label.grid(row=0, column=0, pady=20)

# Username entry
username_label = tk.Label(login_frame, text="Username:", bg='lightblue')
username_label.grid(row=1, column=0, pady=5)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=2, column=0, pady=5)

# Password entry
password_label = tk.Label(login_frame, text="Password:", bg='lightblue')
password_label.grid(row=3, column=0, pady=5)
password_entry = tk.Entry(login_frame, show="*")  # Hide password input
password_entry.grid(row=4, column=0, pady=5)

# Login button
login_button = tk.Button(login_frame, text="Login", command=login)
login_button.grid(row=5, column=0, pady=20)

# --- Main Frame ---
main_Frame.grid_columnconfigure(0, weight=1)  # Centering content in main frame
main_Frame.grid_rowconfigure(0, weight=1)

# Left Frame inside main window
Frame1 = tk.Frame(main_Frame, bg="black", highlightbackground="red", highlightthickness=2, bd=5, relief="flat", padx=10, pady=10, width=90, height=500)
Frame1.grid(row=0, column=0, sticky='nsw')  # Place on the left with sticky

# Control Buttons
button2 = ttk.Button(main_Frame, text="OK", command=on_click)
button2.grid(row=1, column=0, sticky='e', pady=10, padx=10)

button = ttk.Button(main_Frame, text="Quit", command=Main.destroy)
button.grid(row=2, column=0, sticky='e', pady=10, padx=10)

# Show the login frame initially
show_frame(login_frame)

# Loop()
Main.mainloop()
