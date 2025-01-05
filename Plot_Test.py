from datetime import datetime
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pytz

tz_india = pytz.timezone('Asia/Kolkata')
now = datetime.now(tz_india)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Data Plotter")
        self.geometry("600x400")

        self.data_entries = []  # Store user data
        self.times = [] #store time
        self.create_widgets()

    def create_widgets(self):
        # Entry field
        self.entry = ctk.CTkEntry(self, placeholder_text="Enter data (comma-separated)")
        self.entry.pack(pady=10)

        # Submit button
        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.plot_data)
        self.submit_button.pack()

        # Matplotlib figure and canvas
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def plot_data(self):
        data_str = self.entry.get()
        try:
            data = [float(x.strip()) for x in data_str.split(",")]
            self.data_entries.extend(data)
            self.times.extend(range(len(self.times), len(self.times) + len(data)))
            self.ax.clear()  # Clear previous plot
            self.ax.plot(self.times, self.data_entries)
            self.ax.set_xlabel("Time")
            self.ax.set_ylabel("Data")
            self.ax.set_title("Data Plot")
            self.canvas.draw()
            self.entry.delete(0, ctk.END) #Clear the entry box
        except ValueError:
            print("Invalid input. Please enter comma-separated numbers.")
            # Optionally show a message box to the user

if __name__ == "__main__":
    app = App()
    app.mainloop()


# now() method is used to get object
# containing current date & time.


# strftime() method used to create a string
# representing the current time.
currentTime = now.strftime("%H:%M:%S")
