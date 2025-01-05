# import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from aise_hi import AudioApp
from CubeProjection import Pro_Cube
# from Ignore import App
# Set the theme and appearance mode for customtkinter
ctk.set_appearance_mode("dark")  # Options: "dark", "light", or "system"
ctk.set_default_color_theme("green")  # Default color theme


# Initialize main application window
def main(Login):
    Login.destroy()
    root = ctk.CTk()
    
    root.title("Main page")
    root.geometry("900x600") 
# Define frame visibility states
    frame_states = {
        "frame1": False,
        "frame2": False,
        "frame3": False,
        "frame4": False,
        "frame5": False,
        "frame6": False,
        "frame7": False
    }

        
    default_button_color = "transparent" # Default button colors
    selected_button_color = "#844A84"  # Color for the selected button

    iframe = ctk.CTkFrame(root,  width=55, height=98)
    iframe.pack(padx=10, pady=10)
    iframe.pack_propagate(False)
    iframe.pack(side="left", fill="y")

    mframe = ctk.CTkFrame(root,  width=848, height=98)
    mframe.pack( pady=10, padx=10)
    mframe.pack_propagate(False)
    mframe.pack(fill='both',expand= True)

    tabview = ctk.CTkTabview(mframe)
    tabview.pack(fill= 'both', expand=True)

    otab = tabview.add("OVERVIEW")
    dtab = tabview.add("Data Sheet")
    tabview.set("OVERVIEW")

    overview_frame = ctk.CTkFrame(otab, width=848, height=420)
    overview_frame.pack(fill='both', expand=True)

    # Configure rows and columns using weights for collage layout
    overview_frame.grid_rowconfigure(0, weight=3)  # Top row (both parts)
    overview_frame.grid_rowconfigure(1, weight=3)  # Bottom row
    overview_frame.grid_columnconfigure(0, weight=1)  # Left column
    overview_frame.grid_columnconfigure(1, weight=1)  # Right column

    top_left_frame = ctk.CTkFrame(overview_frame)
    top_left_frame.grid(row=0, column=0, sticky="nsew")

    top_right_frame = ctk.CTkFrame(overview_frame, fg_color="lightgreen")
    top_right_frame.grid(row=0, column=1, sticky="nsew")

    bottom_frame = ctk.CTkFrame(overview_frame, fg_color="lightcoral")
    bottom_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")



    # cube_frame = ctk.CTkFrame(overview_frame, width= 420, height=420)
    # cube_frame.place(x=400, y=10, anchor= 'ne')

    Pro_Cube(top_left_frame)

    # #Function to switch between frames
    # def show_frame(frame):
    #     frame.tkraise()

# Function to toggle frame visibility
    def toggle_frame(frame, frame_name,clicked_button):
        if frame_states[frame_name]:  # If the frame is visible, hide it
            frame.place_forget()
            frame_states[frame_name] = False
        else:  # If the frame is hidden, show it
            for f in all_frames:  # Hide all frames before showing the selected one
                f.place_forget()
            frame.place(x=0, y=0, relwidth=1, relheight=1)
            frame_states[frame_name] = True

 # Reset all button colors to default
        for button in all_buttons:
            button.configure(fg_color=default_button_color)

        # Change the clicked button color
        clicked_button.configure(fg_color=selected_button_color)

    def close_frame():
    # Hide all frames
        for frame in all_frames:
            frame.place_forget()
            frame_states[frame._name] = False  # Reset the state of all frames

    # Reset all button colors to the default
        for button in all_buttons:
            button.configure(fg_color=default_button_color)


# Create different frames for each button in mframe
    frame1 = ctk.CTkFrame(mframe, width=848, height=395, bg_color="black")
    AudioApp(frame1)
    try:
        pil_image = Image.open(r"Logo\cubesatIMG.jpg")

        def update_image_size(event, pil_image, label):
            frame_width = event.widget.winfo_width()
            frame_height = event.widget.winfo_height()
            image_width, image_height = pil_image.size

            # Rotate the image by 90 degrees counter-clockwise
            rotated_image = pil_image.rotate(90, expand=True)  # Hardcoded 90-degree rotation

            image_width, image_height = rotated_image.size
            width_ratio = frame_width / image_width
            height_ratio = frame_height / image_height
            min_ratio = min(width_ratio, height_ratio)
            new_width = int(image_width * min_ratio)
            new_height = int(image_height * min_ratio)
            resized_image = rotated_image.resize((new_width, new_height), Image.LANCZOS)
            ctk_image = ctk.CTkImage(light_image=resized_image, dark_image=resized_image, size=resized_image.size)
            label.configure(image=ctk_image)

        # Rotate the original image for initial display
        rotated_image = pil_image.rotate(90, expand=True)
        ctk_image = ctk.CTkImage(light_image=rotated_image, dark_image=rotated_image, size=rotated_image.size)

        label = ctk.CTkLabel(frame1, image=ctk_image, text="")
        label.pack(expand=True, fill="both")

        frame1.bind("<Configure>", lambda event: update_image_size(event, pil_image, label))
        frame1.event_generate("<Configure>")

    except FileNotFoundError:
        label = ctk.CTkLabel(frame1, text="Image not found!")
        label.pack()

    
    frame2 = ctk.CTkFrame(mframe, width=848, height=395, bg_color="blue")
    frame3 = ctk.CTkFrame(mframe, width=848, height=395, bg_color="black")
    frame4 = ctk.CTkFrame(mframe, width=848, height=395, bg_color="black")
    frame5 = ctk.CTkFrame(mframe, width=848, height=395, bg_color="black")
    frame6 = ctk.CTkFrame(mframe, width=848, height=395, bg_color="black")
    frame7 = ctk.CTkFrame(mframe, width=848, height=395, bg_color="black")

    all_frames = [frame1, frame2, frame3, frame4, frame5, frame6, frame7]  # List of all frames

    #subframes
    frame21 = ctk.CTkFrame(frame2, width=848, height=296)
    frame22 = ctk.CTkFrame(frame2, width=848, height=98)
    frame31 = ctk.CTkFrame(frame3, width=848, height=296)
    frame32 = ctk.CTkFrame(frame3, width=848, height=98)
    frame41 = ctk.CTkFrame(frame4, width=848, height=296)
    frame42 = ctk.CTkFrame(frame4, width=848, height=98)
    frame51 = ctk.CTkFrame(frame5, width=848, height=296)
    frame52 = ctk.CTkFrame(frame5, width=848, height=98)
    frame61 = ctk.CTkFrame(frame6, width=848, height=296)
    frame62 = ctk.CTkFrame(frame6, width=848, height=98)
    frame71 = ctk.CTkFrame(frame7, width=848, height=296)
    frame72 = ctk.CTkFrame(frame7, width=848, height=98)

    frame21.pack(fill='both', expand= True, pady= 3, padx=3)
    frame31.pack(fill='both', expand= True , pady= 3, padx=3)
    frame41.pack(fill='both', expand= True, pady= 3, padx=3)
    frame51.pack(fill='both', expand= True, pady= 3, padx=3)
    frame61.pack(fill='both', expand= True, pady= 3, padx=3)
    frame71.pack(fill='both', expand= True, pady= 3, padx=3)
    frame22.pack(fill='both', expand= True, pady= 3, padx=3)
    frame32.pack(fill='both', expand= True, pady= 3, padx=3)
    frame42.pack(fill='both', expand= True, pady= 3, padx=3)
    frame52.pack(fill='both', expand= True, pady= 3, padx=3)
    frame62.pack(fill='both', expand= True, pady= 3, padx=3)
    frame72.pack(fill='both', expand= True, pady= 3, padx=3)
   
    Pro_Cube(frame61)

    #BUTTONS

    #button1
    icon_image1= ctk.CTkImage(Image.open(r"Logo\home.png"), size=(40, 40))

    # Create a button with an icon
    button1 = ctk.CTkButton(iframe, text="Home", font=ctk.CTkFont(family="Inter", size=10, weight="normal"), image=icon_image1, compound="top", fg_color=default_button_color, command=close_frame) # Use the close_frame function
    button1.pack(pady=6)

    #button2
    icon_image2= ctk.CTkImage(Image.open(r"Logo\cardinal.png"), size=(40, 40))
    button2 = ctk.CTkButton(iframe, text="Magnetometer",  font=ctk.CTkFont(family="Inter", size=10, weight="normal"), image=icon_image2, compound="top",fg_color=default_button_color, command=lambda:toggle_frame(frame2, "frame1",button2))
    button2.pack(pady=6)

    #button3
    icon_image3= ctk.CTkImage(Image.open(r"Logo\pressure.png"), size=(40, 40))
    button3 = ctk.CTkButton(iframe, text="BMP-180",  font=ctk.CTkFont(family="Inter", size=10, weight="normal"), image=icon_image3, compound="top",fg_color=default_button_color, command=lambda:toggle_frame(frame3, "frame1",button3))
    button3.pack(pady=6)

    #button4
    icon_image4= ctk.CTkImage(Image.open(r"Logo\gps.png"), size=(40, 40))
    button4 = ctk.CTkButton(iframe, text="GPS module",  font=ctk.CTkFont(family="Inter", size=10, weight="normal"), image=icon_image4, compound="top",fg_color=default_button_color, command=lambda:toggle_frame(frame4, "frame1",button4))
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
    frame1.place(x=0, y=0, relwidth=1, relheight=1)
    root.mainloop()

#adding frames in otab(overview)
