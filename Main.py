import customtkinter as ctk
from PIL import Image
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
    iframe.pack(padx=15, pady=15)
    iframe.pack_propagate(False)
    iframe.pack(side="left", fill="y")

    mframe = ctk.CTkFrame(root,  width=848, height=400)
    mframe.pack( pady=15, padx=15)
    mframe.pack_propagate(False)
    mframe.pack(fill='both',expand= True)

    tabview = ctk.CTkTabview(mframe)
    tabview.pack(fill= 'both', expand=True)

    otab = tabview.add("OVERVIEW")
    dtab = tabview.add("Data Sheet")
    tabview.set("OVERVIEW")
    
    #BUTTONS
    #button1
    icon_image1= ctk.CTkImage(Image.open(r"E:\C downloads backup\Downloads\speedometer.png"), size=(40, 40))

    # Create a button with an icon
    button1 = ctk.CTkButton(iframe, text="Accelerometer",  font=ctk.CTkFont(family="Inter", size=10, weight="normal"), image=icon_image1, compound="top",fg_color="transparent")
    button1.pack(pady=15)

    #button2

    icon_image2= ctk.CTkImage(Image.open(r"E:\C downloads backup\Downloads\compass.png"), size=(40, 40))

    button2 = ctk.CTkButton(iframe, text="Magnetometer",  font=ctk.CTkFont(family="Inter", size=10, weight="normal"), image=icon_image2, compound="top",fg_color="transparent")
    button2.pack(pady=15)
    #button3

    icon_image3= ctk.CTkImage(Image.open(r"E:\C downloads backup\Downloads\humidity.png"), size=(40, 40))



        # Create a button with an icon
    button3 = ctk.CTkButton(iframe, text="BMP-180",  font=ctk.CTkFont(family="Inter", size=10, weight="normal"), image=icon_image3, compound="top",fg_color="transparent")
    button3.pack(pady=15)
    #button4
    icon_image4= ctk.CTkImage(Image.open(r"E:\C downloads backup\Downloads\placeholder.png"), size=(40, 40))



        # Create a button with an icon
    button4 = ctk.CTkButton(iframe, text="GPS module",  font=ctk.CTkFont(family="Inter", size=10, weight="normal"), image=icon_image4, compound="top",fg_color="transparent")
    button4.pack(pady=15)
    #button5
    icon_image5= ctk.CTkImage(Image.open(r"E:\C downloads backup\Downloads\humidity (1).png"), size=(40, 40))

#fg_color=("#DB3E39", "#821D1A")

        # Create a button with an icon
    button5 = ctk.CTkButton(iframe, text="DHT-11",  font=ctk.CTkFont(family="Inter", size=10, weight="normal"), image=icon_image5, compound="top",fg_color="transparent")
    button5.pack(pady=15)
    #button6
    icon_image6= ctk.CTkImage(Image.open(r"E:\C downloads backup\Downloads\3d.png"), size=(40, 40))



        # Create a button with an icon
    button6 = ctk.CTkButton(iframe, text="3D view",  font=ctk.CTkFont(family="Inter", size=10, weight="normal"), image=icon_image6, compound="top",fg_color="transparent")
    button6.pack(pady=15)
 


    root.mainloop()

