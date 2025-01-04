import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
from aise_hi import AudioApp

# Set the theme and appearance mode for customtkinter
ctk.set_appearance_mode("dark")  # Options: "dark", "light", or "system"
ctk.set_default_color_theme("dark-blue")  # Default color theme

# Functions
def login():
    username = user_entry.get()
    password = user_entry1.get()

    # Simple hardcoded credentials for demonstration
    if username == "a" and password == "a":
        messagebox.showinfo("Login", "Login Successful!")
        main(Login=Login)
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

# Initialize main application window
Login = ctk.CTk()
Login.title("Login Window")
Login.geometry("900x600")
Login.configure(fg_color="#000000")

# Create a frame to hold the login components
frame = ctk.CTkFrame(Login, fg_color="#1E1E1E", width=513, height=270, corner_radius=12)
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

user_entry1 = ctk.CTkEntry(frame, fg_color="#2C2A2C", text_color="white", placeholder_text="Enter password", show="₪")
user_entry1.pack(fill='x', padx=20, pady=(0, 10))

# Button to verify login
button = ctk.CTkButton(
    frame,
    text="VERIFY",
    fg_color="#844A84",
    text_color="#1C191C",
    hover_color="#616f7d",
    width=513, height=25,
    command=login
)
button.pack(anchor='s', side=ctk.BOTTOM)

# Function for main window after login
def main(Login):
    Login.destroy()
    root = ctk.CTk()
    root.title("Main page")
    root.geometry("900x600")

    # Define frame visibility states
    frame_states = {
        "frame1": True,
        "frame2": False,
        "frame3": False,
        "frame4": False,
        "frame5": False,
        "frame6": False,
        "frame7": False
    }

    default_button_color = "transparent"
    selected_button_color = "#844A84"

    iframe = ctk.CTkFrame(root, width=55, height=395)
    iframe.pack(padx=10, pady=10, side="left", fill="y")
    iframe.pack_propagate(False)

    mframe = ctk.CTkFrame(root, width=848, height=395)
    mframe.pack(pady=10, padx=10, fill='both', expand=True)
    mframe.pack_propagate(False)

    tabview = ctk.CTkTabview(mframe)
    tabview.pack(fill='both', expand=True)

    otab = tabview.add("OVERVIEW")
    dtab = tabview.add("Data Sheet")
    tabview.set("OVERVIEW")

    def toggle_frame(frame, frame_name, clicked_button):
        if frame_states[frame_name]:
            frame.place_forget()
            frame_states[frame_name] = False
        else:
            for f in all_frames:
                f.place_forget()
            frame.place(x=0, y=0, relwidth=1, relheight=1)
            frame_states[frame_name] = True

        for button in all_buttons:
            button.configure(fg_color=default_button_color)
        clicked_button.configure(fg_color=selected_button_color)

    frame1 = ctk.CTkFrame(mframe, width=848, height=395, bg_color="black")
    AudioApp(frame1)

    image = Image.open("cubesatIMG.jpg")
    image = image.resize((848, 395))
    image_tk = ImageTk.PhotoImage(image)
    image_label = ctk.CTkLabel(frame1, image=image_tk)
    image_label.pack(pady=20)
    image_label.image = image_tk

    frame2 = ctk.CTkFrame(mframe, width=848, height=395, bg_color="blue")
    frame3 = ctk.CTkFrame(mframe, width=848, height=395, bg_color="black")
    frame4 = ctk.CTkFrame(mframe, width=848, height=395)
    frame5 = ctk.CTkFrame(mframe, width=848, height=395, bg_color="black")
    frame6 = ctk.CTkFrame(mframe, width=848, height=395, bg_color="green")
    frame7 = ctk.CTkFrame(mframe, width=848, height=395, bg_color="green")

    all_frames = [frame1, frame2, frame3, frame4, frame5, frame6, frame7]

    label1 = ctk.CTkLabel(frame1, text="Frame 1", font=ctk.CTkFont(family="Inter", size=30, weight="normal"))
    label1.pack(pady=20)

    label2 = ctk.CTkLabel(frame2, text="Frame 2", font=ctk.CTkFont(family="Inter", size=30, weight="normal"))
    label2.pack(pady=20)

    label3 = ctk.CTkLabel(frame3, text="Frame 3", font=ctk.CTkFont(family="Inter", size=30, weight="normal"))
    label3.pack(pady=20)

    label4 = ctk.CTkLabel(frame4, text="Frame 4", font=ctk.CTkFont(family="Inter", size=30, weight="normal"))
    label4.pack(pady=20)

    label5 = ctk.CTkLabel(frame5, text="Frame 5", font=ctk.CTkFont(family="Inter", size=30, weight="normal"))
    label5.pack(pady=20)

    label6 = ctk.CTkLabel(frame6, text="Frame 6", font=ctk.CTkFont(family="Inter", size=30, weight="normal"))
    label6.pack(pady=20)

    label7 = ctk.CTkLabel(frame7, text="Frame 7", font=ctk.CTkFont(family="Inter", size=30, weight="normal"))
    label7.pack(pady=20)

    icon_image1 = ctk.CTkImage(Image.open(r"Logo\home.png"), size=(40, 40))
    button1 = ctk.CTkButton(iframe, text="Home", font=ctk.CTkFont(family="Inter", size=10, weight="normal"), image=icon_image1, compound="top", fg_color=default_button_color, command=lambda: toggle_frame(frame1, "frame1", button1))
    button1.pack(pady=6)

    icon_image2 = ctk.CTkImage(Image.open(r"Logo\cardinal.png"), size=(40, 40))
    button2 = ctk.CTkButton(iframe, text="Magnetometer", font=ctk.CTkFont(family="Inter", size=10, weight="normal"), image=icon_image2, compound="top", fg_color=default_button_color, command=lambda: toggle_frame(frame2, "frame2", button2))
    button2.pack(pady=6)

    icon_image3 = ctk.CTkImage(Image.open(r"Logo\pressure.png"), size=(40, 40))
    button3 = ctk.CTkButton(iframe, text="BMP-180", font=ctk.CTkFont(family="Inter", size=10, weight="normal"), image=icon_image3, compound="top", fg_color=default_button_color, command=lambda: toggle_frame(frame3, "frame3", button3))
    button3.pack(pady=6)

    icon_image4 = ctk.CTkImage(Image.open(r"Logo\gps.png"), size=(40, 40))
    button4 = ctk.CTkButton(iframe, text="GPS", font=ctk.CTkFont(family="Inter", size=10, weight="normal"), image=icon_image4, compound="top", fg_color=default_button_color, command=lambda: toggle_frame(frame4, "frame4", button4))
    button4.pack(pady=6)

#button5
    icon_image5= ctk.CTkImage(Image.open(r"Logo\humidity.png"), size=(40, 40))
    button5 = ctk.CTkButton(iframe, text="DHT-11",  font=ctk.CTkFont(family="Inter", size=10, weight="normal"), image=icon_image5, compound="top",fg_color=default_button_color, command=lambda:toggle_frame(frame5, "frame1",button5))
    button5.pack(pady=6)

    #button6
    icon_image6= ctk.CTkImage(Image.open(r"Logo\3d.png"), size=(40, 40))
    button6 = ctk.CTkButton(iframe, text="3D view",  font=ctk.CTkFont(family="Inter", size=10, weight="normal"), image=icon_image6, compound="top",fg_color=default_button_color, command=lambda:toggle_frame(frame6, "frame1",button6))
    button6.pack(pady=6)
    
 
    icon_image7= ctk.CTkImage(Image.open(r"Logo\tools.png"), size=(40, 40))
    button7 = ctk.CTkButton(iframe, text="Accelerometer",  font=ctk.CTkFont(family="Inter", size=10, weight="normal"), image=icon_image7, compound="top",fg_color=default_button_color, command=lambda:toggle_frame(frame7, "frame1", button7))
    button7.pack(pady=6)

    all_buttons = [button1, button2, button3, button4, button5, button6, button7]

    root.mainloop()

Login.mainloop()
