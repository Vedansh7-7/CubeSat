import customtkinter as ctk

# Set the theme and appearance mode for customtkinter
ctk.set_appearance_mode("dark")  # Options: "dark", "light", or "system"
ctk.set_default_color_theme("green")  # Default color theme


# Initialize main application window
def main(Login):
    Login.destroy()
    root = ctk.CTk()
    root.title("Main page")
    root.geometry("900x600") 

    iframe = ctk.CTkFrame(root,  width=52, height=400)
    iframe.pack(padx=5, pady=5)
    iframe.pack_propagate(False)
    iframe.pack(side="left", fill="y")

    mframe = ctk.CTkFrame(root,  width=848, height=400)
    mframe.pack( pady=5, padx=5)
    mframe.pack_propagate(False)
    mframe.pack(fill='both',expand= True)

    tabview = ctk.CTkTabview(mframe)
    tabview.pack(fill= 'both', expand=True)

    tabview.add("OVERVIEW")
    tabview.add("Data Sheet")
    tabview.set("OVERVIEW")




    root.mainloop()
