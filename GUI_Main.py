import customtkinter as ctk

class SerialApp:
    def __init__(self, frame):
        # Entry for COM Port
        self.com_label = ctk.CTkLabel(frame, text="COM Port:", text_color='#844A84')
        self.com_label.pack(pady=10)
        self.com_entry = ctk.CTkEntry(frame)
        self.com_entry.pack(pady=5)

        # Entry for CSV File Path
        self.file_label = ctk.CTkLabel(frame, text="CSV File Path:",text_color='#844A84')
        self.file_label.pack(pady=10)
        self.file_entry = ctk.CTkEntry(frame)
        self.file_entry.pack(pady=5)

        # Status label
        self.status_label = ctk.CTkLabel(frame, text="OFFLINE", text_color="red", font=("Helvetica", 20))
        self.status_label.pack(pady=20)

if __name__ == "__main__":
    root = ctk.CTk()

    # Create a frame to contain the widgets
    frame = ctk.CTkFrame(root)
    frame.pack(pady=20, padx=20)

    app = SerialApp(frame)
    root.mainloop()