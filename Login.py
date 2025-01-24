import customtkinter as ctk
from Main import main
import PIL
# from PIL import Image, ImageTk
from tkinter import messagebox
# from aise_hi import AudioApp


# Set the theme and appearance mode for customtkinter
ctk.set_appearance_mode("dark")  # Options: "dark", "light", or "system"
ctk.set_default_color_theme("dark-blue")  # Default color theme

# File path to the Credentials.txt file
cred_path = 'Credentials.txt'

# Initialize variables to store values
U = ""
P = ""

# Open the file and read the content
with open(cred_path, 'r') as file:
    for line in file:
        # Split the line at '=' and strip extra spaces
        key, value = line.strip().split('=')
        key = key.strip()
        value = value.strip()

        # Assign values to the appropriate variables
        if key == 'U':
            U = value
        elif key == 'P':
            P = value

# Functions
def login():
    username = user_entry.get()
    password = user_entry1.get()

    if username == U and password == P:
        messagebox.showinfo("Login", "Login Successful!")
        Login.destroy()  # Close the login window
        main()
    else:
        messagebox.showerror("Login", "Invalid Username or Password")


# Initialize main application window
Login = ctk.CTk()
Login.title("Login Window")
Login.geometry("900x600") 
Login.configure(fg_color="#000000")

image = PIL.Image.open(r"Logo\bg.png")
background_image = ctk.CTkImage(image, size=(500, 500))

def bg_resizer(e):
    if e.widget is Login:
        i = ctk.CTkImage(image, size=(e.width, e.height))
        bg_lbl.configure(text="", image=i)

# Create a bg label
bg_lbl = ctk.CTkLabel(Login, text="", image=background_image)
bg_lbl.place(x=0, y=0)

Login.bind("<Configure>", bg_resizer)

# Create a frame to hold the login components
frame = ctk.CTkFrame(Login, fg_color="#1E1E1E", width=513, height=270, corner_radius= 12)
frame.pack(padx=10, pady=10)
frame.pack_propagate(False)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Label for the "LOGIN" title
label = ctk.CTkLabel(frame, text="LOGIN", text_color='#844A84', font=ctk.CTkFont(family="Inter", size=25, weight="normal"))
label.pack(pady=15)

# Username label and entry field
user_label = ctk.CTkLabel(frame, text="USERNAME:", text_color="#844A84", font=ctk.CTkFont(family="Inter", size=12, weight="normal"))
user_label.pack(anchor='w', padx=20, pady=(10, 5))

user_entry = ctk.CTkEntry(frame, fg_color="#2C2A2C", text_color="white", placeholder_text="Enter Username")
user_entry.pack(fill='x', padx=20, pady=(0, 10))

user_label1 = ctk.CTkLabel(frame, text="PASSWORD:", text_color="#844A84", font=ctk.CTkFont(family="Inter", size=12, weight="normal"))
user_label1.pack(anchor='w', padx=20, pady=(10, 5))

user_entry1 = ctk.CTkEntry(frame, fg_color="#2C2A2C", text_color="white", placeholder_text="Enter password",show= "₪")
user_entry1.pack(fill='x', padx=20, pady=(0, 10))

# Button to enter
button = ctk.CTkButton(
    frame,
    text="VERIFY", # Function to call on click
    fg_color="#844A84",           # Button background color
    text_color="#1C191C",           # Button text color
    hover_color="#616f7d"   ,      # Color when hovered over
    width=513, height=25, command= login
)
button.pack(anchor='s', side= ctk.BOTTOM)
# Start the main event loop
Login.mainloop()



