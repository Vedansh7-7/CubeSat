import customtkinter as ctk

# Set the theme and appearance mode for customtkinter
ctk.set_appearance_mode("dark")  # Options: "dark", "light", or "system"
ctk.set_default_color_theme("dark-blue")  # Default color theme

# Initialize main application window
root = ctk.CTk()
root.title("Login Window")
root.geometry("900x600") 
root.configure(fg_color="#000000")

# Create a frame to hold the login components
frame = ctk.CTkFrame(root, fg_color="#1C191C", width=513, height=270, corner_radius= 12)
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

user_entry1 = ctk.CTkEntry(frame, fg_color="#2C2A2C", text_color="white", placeholder_text="Enter password", show= "₪")
user_entry1.pack(fill='x', padx=20, pady=(0, 10))


# Start the main event loop
root.mainloop()

