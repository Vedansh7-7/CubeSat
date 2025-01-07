from datetime import datetime, timedelta
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import pytz

tz_india = pytz.timezone('Asia/Kolkata')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Data Plotter")
        self.geometry("800x500")

        self.data_entries = []  # Store user data
        self.timestamps = []  # Store timestamps
        self.create_widgets()

        # Start the real-time clock
        self.update_clock()

    def create_widgets(self):
        # Entry field
        self.entry = ctk.CTkEntry(self, placeholder_text="Enter data (comma-separated)")
        self.entry.pack(pady=10)

        # Submit button
        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.plot_data)
        self.submit_button.pack()

        # Real-time clock display
        self.clock_label = ctk.CTkLabel(self, text="", font=("Helvetica", 14))
        self.clock_label.pack(pady=10)

        # Matplotlib figure and canvas
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def update_clock(self):
        """Update the clock and refresh every 100 milliseconds."""
        current_time = datetime.now(tz_india).strftime("%H:%M:%S")
        self.clock_label.configure(text=f"Current Time: {current_time}")
        self.after(100, self.update_clock)

    def plot_data(self):
        data_str = self.entry.get()
        try:
            data = [float(x.strip()) for x in data_str.split(",")]
            self.data_entries.extend(data)
            now = datetime.now(tz_india)
            new_timestamps = [
                (now - timedelta(milliseconds=100 * (len(data) - i - 1))).strftime("%H:%M:%S")
                for i in range(len(data))
            ]
            self.timestamps.extend(new_timestamps)

            self.ax.clear()  # Clear previous plot
            self.ax.plot(self.timestamps, self.data_entries, marker="o")
            self.ax.set_xlabel("Timestamp")
            self.ax.set_ylabel("Data")
            self.ax.set_title("Data Plot")
            self.ax.tick_params(axis="x", rotation=45)
            self.canvas.draw()

            self.entry.delete(0, ctk.END)  # Clear the entry box
        except ValueError:
            print("Invalid input. Please enter comma-separated numbers.")
            # Optionally show a message box to the user


if __name__ == "__main__":
    app = App()
    app.mainloop()
