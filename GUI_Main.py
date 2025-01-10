import customtkinter as ctk
import tkinter as tk
import serial
import serial.tools.list_ports
import threading
import os
import csv


class SerialApp:
    def __init__(self, frame, textAreas, root):
        # Save root reference for later use
        self.rotation = True
        self.root = root
        self.text_areas = textAreas

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

        self.create_button = ctk.CTkButton(frame, text="Click Me", command=self.start_threads)
        self.create_button.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

    def toggleRotate(self):
        if self.rotation:
            self.rotation = False
        else:
            self.rotation = True

        return self.rotation

    def validate_inputs(self, port, baudrate, file_path):
        # Validate COM port, baudrate, and file path
        available_ports = [p.device for p in serial.tools.list_ports.comports()]
        if port not in available_ports:
            print(f"Error: COM port {port} not found.")
            return False
        try:
            int(baudrate)
        except ValueError:
            print("Error: Invalid baudrate.")
            return False
        dir_path = os.path.dirname(file_path)
        if dir_path and not os.path.exists(dir_path):
            print(f"Error: Directory {dir_path} does not exist.")
            return False
        return True

    def read_serial(self):
        try:
            while self.running:
                if self.serial.in_waiting > 0:
                    line = self.serial.readline().decode('utf-8').strip()
                    # print(f"Serial Data: {line}")
                    
                    # Update the text_area widget with the received data
                    self.update_text_area([line])  # Pass the data as a list
                    
                    # Save the data to CSV
                    self.save_to_csv(line)
        except Exception as e:
            print(f"Error reading serial data: {e}")    


    def save_to_csv(self, data):
        # Ensure the CSV file exists and save data
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Data"])
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.get_current_timestamp(), data])

    def get_current_timestamp(self):
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def start_reading(self):
        # Start reading serial data
        port = self.com_entry.get()
        baudrate = self.rate_entry.get()
        self.file_path = self.file_entry.get()

        if self.validate_inputs(port, baudrate, self.file_path):
            try:
                self.serial = serial.Serial(port=port, baudrate=int(baudrate), timeout=1)
                self.running = True
                print(f"Connected to {port} at {baudrate} baud.")
                self.update_status("ONLINE", "green")
            except serial.SerialException as e:
                print(f"Error opening serial port: {e}")
                self.update_status("OFFLINE", "red")
        else:
            self.update_status("OFFLINE", "red")

    def update_status(self, status, color):
        self.status_label.configure(text=status, text_color=color)
        
    def update_text_area(self, row):
        # Iterate over each text area and insert the row of data
        for text_area in self.text_areas:
            text_area.insert(tk.END, ', '.join(row) + '\n')
            text_area.see(tk.END)  # Scroll to the end

    def read_csv_from_file(self, csv_file_path=r"File.csv"):
        try:
            with open(csv_file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    # Use after() to safely update the Text widgets from the main thread
                    self.root.after(0, self.update_text_area, row)
        except Exception as e:
            print(f"Error reading CSV file: {e}")

    def start_threads(self):
        # Start threads for reading serial data and CSV file
        self.toggleRotate()
        thread1 = threading.Thread(target=self.read_serial, daemon=True)
        thread2 = threading.Thread(target=self.read_csv_from_file, args=(self.file_entry.get(),), daemon=True)
        
        thread1.start()
        thread2.start()



# # Main Code
# if __name__ == "__main__":
#     root = ctk.CTk()

#     # Create a frame to contain the widgets
#     frame = ctk.CTkFrame(root)
#     frame.pack(pady=20, padx=20)

#     app = SerialApp(frame)
#     root.mainloop()
