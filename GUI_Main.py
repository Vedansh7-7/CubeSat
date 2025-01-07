import tkinter as tk

class SerialApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Serial Data Reader")

        # Entry for COM Port
        self.com_label = tk.Label(self.master, text="COM Port:")
        self.com_label.pack()
        self.com_entry = tk.Entry(self.master)
        self.com_entry.pack()

        # Entry for CSV File Path
        self.file_label = tk.Label(self.master, text="CSV File Path:")
        self.file_label.pack()
        self.file_entry = tk.Entry(self.master)
        self.file_entry.pack()

        # Status label
        self.status_label = tk.Label(self.master, text="OFFLINE", fg="red", font=("Helvetica", 12))
        self.status_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = SerialApp(root)
    root.mainloop()
