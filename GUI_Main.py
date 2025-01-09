import customtkinter as ctk
import serial
import serial.tools.list_ports
import threading
import math
import os

class SerialApp:
<<<<<<< HEAD
    def __init__(self, frame):
=======
    def __init__(self, frame, port='COM3', baudrate=9600, file_path='File.csv'):
        self.serial = serial.Serial(port, baudrate, timeout=1)
        self.file_path = file_path
        self.running = True

>>>>>>> 46f38b0d21f44d9e8f747eea3eb984bb6e0c4935
        # Entry for COM Port
        self.com_label = ctk.CTkLabel(frame, text="COM Port:", text_color='#844A84')
        self.com_label.pack(pady=10)
        self.com_entry = ctk.CTkEntry(frame)
        self.com_entry.pack(pady=5)

        # Entry for Baudrate
        self.rate_label = ctk.CTkLabel(frame, text="Baudrate:", text_color='#844A84')
        self.rate_label.pack(pady=10)
        self.rate_entry = ctk.CTkEntry(frame)
        self.rate_entry.pack(pady=5)

        # Entry for CSV File Path
        self.file_label = ctk.CTkLabel(frame, text="CSV File Path:", text_color='#844A84')
        self.file_label.pack(pady=10)
        self.file_entry = ctk.CTkEntry(frame)
        self.file_entry.pack(pady=5)

<<<<<<< HEAD
        # Status Label
=======
        # Status label
>>>>>>> 46f38b0d21f44d9e8f747eea3eb984bb6e0c4935
        self.status_label = ctk.CTkLabel(frame, text="OFFLINE", text_color="red", font=("Helvetica", 20))
        self.status_label.pack(pady=20)

        # Start Button
        self.start_button = ctk.CTkButton(frame, text="Validate", command=self.start_reading)
        self.start_button.pack()

    def validate_inputs(self, port, baudrate, file_path):
        # Check if the port is available and the file path exists
        available_ports = [p.device for p in serial.tools.list_ports.comports()]  # List available COM ports
        if port not in available_ports:
            print(f"Error: COM port {port} not found.")
            return False
        try:
            baudrate = int(baudrate)  # Ensure baudrate is an integer
        except ValueError:
            print("Error: Invalid baudrate.")
            return False
        if not os.path.isfile(file_path):  # Check if file path exists
            print(f"Error: File {file_path} not found.")
            return False
        return True

    def start_reading(self):
        # Get user inputs
        port = self.com_entry.get()
        baudrate = self.rate_entry.get()
        file_path = self.file_entry.get()

        # Validate inputs
        if self.validate_inputs(port, baudrate, file_path):
            try:
                self.serial = serial.Serial(port=port, baudrate=int(baudrate), timeout=1)
                print(f"Connected to {port} at {baudrate} baud.")
                self.update_status("ONLINE", "green")
            except serial.SerialException as e:
                print(f"Error opening serial port: {e}")
                self.update_status("OFFLINE", "red")
        else:
            self.update_status("OFFLINE", "red")

    def update_status(self, status, color):
        self.status_label.configure(text=status, text_color=color)

# if __name__ == "__main__":
#     root = ctk.CTk()

#     # Create a frame to contain the widgets
#     frame = ctk.CTkFrame(root)
#     frame.pack(pady=20, padx=20)

#     app = SerialApp(frame)
#     root.mainloop()
