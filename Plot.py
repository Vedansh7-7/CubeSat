import csv
from datetime import datetime
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pytz
from tkinter import messagebox

tz_india = pytz.timezone('Asia/Kolkata')

class PlotterGUI:
    def __init__(self, frame, filepath, columnNames):
        self.frame = frame
        self.filepath = filepath
        self.columnNames = columnNames
        self.data_entries = []  # Store user data
        self.timestamps = []  # Store timestamps
        self.column_names = []  # Store column names from CSV
        self.create_widgets()
        self.update_clock()

    def create_widgets(self):
        # Entry for column names to plot
        self.columns_entry = self.columnNames

        # Submit button to load data and plot
        self.submit_button = ctk.CTkButton(self.frame, text="Load CSV & Plot", command=self.load_csv_data)
        self.submit_button.pack(pady=10)

        # Matplotlib figure and canvas
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        # Real-time clock display
        self.clock_label = ctk.CTkLabel(self.frame, text="", font=("Helvetica", 14))
        self.clock_label.pack(pady=10)

    def update_clock(self):
        """Update the clock and refresh every 100 milliseconds."""
        current_time = datetime.now(tz_india).strftime("%H:%M:%S")
        self.clock_label.configure(text=f"Current Time: {current_time}")
        self.frame.after(100, self.update_clock)

    def load_csv_data(self):
        file_path = self.filepath  # Replace with your actual CSV file path
        selected_columns = self.columns_entry.split(',')

        try:
            with open(file_path, mode='r') as file:
                # Specify the correct delimiter here (e.g., ',' or ';' or other)
                reader = csv.DictReader(file, delimiter=',')  # You can change ',' to another delimiter if needed
                self.timestamps = []
                self.data_entries = {col: [] for col in selected_columns}

                for row in reader:
                    # Add timestamp to plot
                    self.timestamps.append(row["Timestamp"])

                    # Add selected columns to data entries
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
        # Clear previous plot
        self.ax.clear()

        # Plot data for the selected columns
        for col in selected_columns:
            self.ax.plot(self.timestamps, self.data_entries[col], marker="o", label=col)

        self.ax.set_xlabel("Timestamp")
        self.ax.set_ylabel("Data")
        self.ax.set_title("CSV Data Plot")
        self.ax.tick_params(axis="x", rotation=45)
        self.ax.legend()

        # Redraw the canvas
        self.canvas.draw()

# if __name__ == "__main__":
#     app = ctk.CTk()
#     app.title("CSV Data Plotter")
#     app.geometry("800x500")

#     main_frame = ctk.CTkFrame(app)
#     main_frame.pack(fill="both", expand=True)

#     PlotterGUI(main_frame)

#     app.mainloop()
