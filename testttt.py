import customtkinter as ctk
import serial
import serial.tools.list_ports
import threading
import math
import os
import csv

class SerialApp:
    def __init__(self, frame):
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

        # Status Label
        self.status_label = ctk.CTkLabel(frame, text="OFFLINE", text_color="red", font=("Helvetica", 20))
        self.status_label.pack(pady=20)

        # Start Button
        self.start_button = ctk.CTkButton(frame, text="Validate", command=self.start_reading)
        self.start_button.pack()

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
            os.makedirs(dir_path)
            print(f"Directory {dir_path} created.")
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
                writer.writerow(["Timestamp", "Data"]) # Data format
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


if __name__ == "__main__":
    root = ctk.CTk()

    # Create a frame to contain the widgets
    frame = ctk.CTkFrame(root)
    frame.pack(pady=20, padx=20)

    app = SerialApp(frame)
    root.mainloop()


# Create Button 
Button(root,text="Click Me",command = threading).pack()