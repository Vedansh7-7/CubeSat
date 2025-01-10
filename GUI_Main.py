import customtkinter as ctk
import serial
import serial.tools.list_ports
from threading import *
import threading
# import math
import os
import csv

# class SerialApp:
#     def __init__(self, frame):
#         # Entry for COM Port
#         self.com_label = ctk.CTkLabel(frame, text="COM Port:", text_color='#844A84')
#         self.com_label.pack(pady=10)
#         self.com_entry = ctk.CTkEntry(frame)
#         self.com_entry.pack(pady=5)

#         # Entry for Baudrate
#         self.rate_label = ctk.CTkLabel(frame, text="Baudrate:", text_color='#844A84')
#         self.rate_label.pack(pady=10)
#         self.rate_entry = ctk.CTkEntry(frame)
#         self.rate_entry.pack(pady=5)

#         # Entry for CSV File Path
#         self.file_label = ctk.CTkLabel(frame, text="CSV File Path:", text_color='#844A84')
#         self.file_label.pack(pady=10)
#         self.file_entry = ctk.CTkEntry(frame)
#         self.file_entry.pack(pady=5)

#         # Status Label
#         self.status_label = ctk.CTkLabel(frame, text="OFFLINE", text_color="red", font=("Helvetica", 20))
#         self.status_label.pack(pady=20)

#         # Start Button
#         self.start_button = ctk.CTkButton(frame, text="Validate", command=self.start_reading)
#         self.start_button.grid(column=0, sticky="nsew")

#         # Create Button 
#         self.Button(frame,text="Click Me",command = threading).grid(column=1, sticky="nsew")

    

class SerialApp:
    def __init__(self, frame):
        # Configure grid layout for the frame
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        # Entry for COM Port
        self.com_label = ctk.CTkLabel(frame, text="COM Port:", text_color='#844A84')
        self.com_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        self.com_entry = ctk.CTkEntry(frame)
        self.com_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # Entry for Baudrate
        self.rate_label = ctk.CTkLabel(frame, text="Baudrate:", text_color='#844A84')
        self.rate_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        self.rate_entry = ctk.CTkEntry(frame)
        self.rate_entry.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # Entry for CSV File Path
        self.file_label = ctk.CTkLabel(frame, text="CSV File Path:", text_color='#844A84')
        self.file_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        self.file_entry = ctk.CTkEntry(frame)
        self.file_entry.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # Status Label
        self.status_label = ctk.CTkLabel(frame, text="OFFLINE", text_color="red", font=("Helvetica", 20))
        self.status_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # Buttons
        self.start_button = ctk.CTkButton(frame, text="Validate", command=self.start_reading)
        self.start_button.grid(row=7, column=0, padx=10, pady=10, sticky="ew")

        self.create_button = ctk.CTkButton(frame, text="Click Me", command=threadingzz)
        self.create_button.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

    def validate_inputs(self, port, baudrate, file_path):
        # Check if the port is available and the file path directory exists
        available_ports = [p.device for p in serial.tools.list_ports.comports()]  # List available COM ports
        if port not in available_ports:
            print(f"Error: COM port {port} not found.")
            return False
        try:
            baudrate = int(baudrate)  # Ensure baudrate is an integer
        except ValueError:
            print("Error: Invalid baudrate.")
            return False
        dir_path = os.path.dirname(file_path)
        if dir_path and not os.path.exists(dir_path):
            print(f"Error: Directory {dir_path} does not exist.")
            return False
        return True

    def read_serial(self):
        while self.running:
            if self.serial.in_waiting > 0:
                line = self.serial.readline().decode('utf-8').strip()
                self.save_to_csv(line)

    def save_to_csv(self, data):
        # Ensure the file exists, create it if it doesn't
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Filt_g_X","Filt_g_Y","Filt_g_Z","Filt_g_net","Hum","Temp","Bx","By","Bz","B_net","Head","P","T","Alt","GPS_lat","GPS_lon","GPS_time","GPS_date"])
        # Append data to the file
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.get_current_timestamp(), data])

    def get_current_timestamp(self):
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def start_reading(self):
        # Get user inputs
        port = self.com_entry.get()
        baudrate = self.rate_entry.get()
        self.file_path = self.file_entry.get()

        # Validate inputs
        if self.validate_inputs(port, baudrate, self.file_path):
            try:
                self.serial = serial.Serial(port=port, baudrate=int(baudrate), timeout=1)
                self.running = True
                print(f"Connected to {port} at {baudrate} baud.")
                self.update_status("ONLINE", "green")
                threading.Thread(target=self.read_serial, daemon=True).start()
            except serial.SerialException as e:
                print(f"Error opening serial port: {e}")
                self.update_status("OFFLINE", "red")
        else:
            self.update_status("OFFLINE", "red")

    def update_status(self, status, color):
        self.status_label.configure(text=status, text_color=color)


def threadingzz(tar, arg): 
    # Call work function 
        t1=Thread(target=tar, args=arg) 
        t1.start()

# if __name__ == "__main__":
#     root = ctk.CTk()

#     # Create a frame to contain the widgets
#     frame = ctk.CTkFrame(root)
#     frame.pack(pady=20, padx=20)

#     app = SerialApp(frame)
#     root.mainloop()
