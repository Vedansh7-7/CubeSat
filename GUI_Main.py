import customtkinter as ctk
import serial
import serial.tools.list_ports
import threading
import csv
import math
import os

class SerialApp:
    def __init__(self, frame, port='COM3', baudrate=9600, file_path='File.csv'):
        self.serial = serial.Serial(port, baudrate, timeout=1)
        self.file_path = file_path
        self.running = True

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

        self.start_button = ctk.CTkButton(frame, text="Start", command=self.start_reading)
        self.start_button.pack()

        # Testing..
    def on_closing(self):
        if self.serial_reader:
            self.serial_reader.stop()
        self.master.destroy()

    def update_cube_orientation(self, data):
        try:
            # Assuming data format is "angle_x,angle_y,angle_z"
            angles = list(map(float, data.split(',')))
            self.angle_x, self.angle_y, self.angle_z = angles
            self.rotate_cube(self.angle_x * math.pi / 180, self.angle_y * math.pi / 180, self.angle_z * math.pi / 180)
            self.draw_cube()
        except Exception as e:
            print("Error updating cube orientation:", e)

    def update_status(self, status, color):
        self.status_label.configure(text=status, fg=color)

    def validate_inputs(self, port, file_path):
        # Check if the port is available and the file path exists
        available_ports = [p.device for p in serial.tools.list_ports.comports()]  # List available COM ports
        if port not in available_ports:  # Check if the specified port is available
            return False
        if not os.path.isfile(file_path):  # Check if file path exists
            return False
        return True
    
    def start_reading(self):
        port = self.com_entry.get()  # Get the COM port from the entry
        file_path = self.file_entry.get()  # Get the CSV file path from the entry
        
        # Validate COM port and file path
        if self.validate_inputs(port, file_path):
            self.serial_reader = SerialApp(port=port, baudrate='9600', file_path=file_path)
            self.thread = threading.Thread(target=self.serial_reader.read_serial)
            self.thread.start()
            self.update_status("ONLINE", "green")
        else:
            self.update_status("OFFLINE", "red")


# if __name__ == "__main__":
#     root = ctk.CTk()

#     # Create a frame to contain the widgets
#     frame = ctk.CTkFrame(root)
#     frame.pack(pady=20, padx=20)

#     app = SerialApp(frame)
#     root.mainloop()