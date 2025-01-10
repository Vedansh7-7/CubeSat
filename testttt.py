import serial  # Make sure you have pySerial installed
import threading
import csv
from datetime import datetime
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pytz
from tkinter import messagebox


class PlotterGUI:
    def __init__(self, frame, filepath, columnNames, serial_port):
        self.frame = frame
        self.filepath = filepath
        self.columnNames = columnNames
        self.data_entries = []  # Store user data
        self.timestamps = []  # Store timestamps
        self.column_names = []  # Store column names from CSV
        self.serial_port = serial_port  # Serial port for reading data
        self.create_widgets()
        self.update_clock()
        
        # Start a separate thread to handle serial data
        self.serial_thread = threading.Thread(target=self.read_serial_data)
        self.serial_thread.daemon = True  # Ensures the thread stops when the program ends
        self.serial_thread.start()

    def create_widgets(self):
        self.columns_entry = self.columnNames
        self.submit_button = ctk.CTkButton(self.frame, text="Load CSV & Plot", command=self.load_csv_data)
        self.submit_button.pack(pady=10)
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        self.clock_label = ctk.CTkLabel(self.frame, text="", font=("Helvetica", 14))
        self.clock_label.pack(pady=10)

    def update_clock(self):
        current_time = datetime.now(tz_india).strftime("%H:%M:%S")
        self.clock_label.configure(text=f"Current Time: {current_time}")
        self.frame.after(100, self.update_clock)

    def load_csv_data(self):
        file_path = self.filepath
        selected_columns = self.columns_entry.get().split(',')
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                self.timestamps = []
                self.data_entries = {col: [] for col in selected_columns}
                for row in reader:
                    self.timestamps.append(row["Timestamp"])
                    for col in selected_columns:
                        if col in row:
                            try:
                                self.data_entries[col].append(float(row[col]))
                            except ValueError:
                                print(f"Invalid data for column {col} in row: {row}")
            if not self.data_entries:
                raise ValueError("No valid columns found in the CSV file.")
            self.plot_data(selected_columns)
        except FileNotFoundError:
            messagebox.showerror("File Not Found", "The specified CSV file could not be found.")
        except ValueError as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def plot_data(self, selected_columns):
        self.ax.clear()
        for col in selected_columns:
            self.ax.plot(self.timestamps, self.data_entries[col], marker="o", label=col)
        self.ax.set_xlabel("Timestamp")
        self.ax.set_ylabel("Data")
        self.ax.set_title("CSV Data Plot")
        self.ax.tick_params(axis="x", rotation=45)
        self.ax.legend()
        self.canvas.draw()

    def read_serial_data(self):
        # Open the serial port
        with serial.Serial(self.serial_port, 9600, timeout=1) as ser:
            while True:
                line = ser.readline().decode('utf-8').strip()  # Read and decode the data from serial port
                if line:
                    # Split the data based on your expected delimiter (e.g., comma)
                    data = line.split(',')  # Assuming the data is comma-separated
                    if len(data) == len(self.columnNames):  # Make sure the number of values matches the column count
                        timestamp = datetime.now(tz_india).strftime("%Y-%m-%d %H:%M:%S")  # Use the current timestamp
                        self.timestamps.append(timestamp)
                        for idx, value in enumerate(data):
                            try:
                                value = float(value)
                                self.data_entries[self.columnNames[idx]].append(value)
                            except ValueError:
                                print(f"Invalid value for column {self.columnNames[idx]}: {value}")
                    else:
                        print(f"Data does not match column names: {line}")

                    # Update the plot with new data
                    self.plot_data(self.columnNames)
