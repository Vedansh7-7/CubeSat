import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

# Initialize the CustomTkinter app
app = ctk.CTk()
app.geometry("500x400")
app.title("Basic File Operations")

# File path
file_path = "Repo_GUI\GUI_CubeSat\File.txt"
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import csv

# Initialize the CustomTkinter app
app = ctk.CTk()
app.geometry("600x500")
app.title("CSV File Handling")

# CSV file path
csv_file_path = r"Repo_GUI\GUI_CubeSat\File.csv"

# Function to read CSV file
def read_csv():
    try:
        text_widget.delete("1.0", tk.END)
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                text_widget.insert(tk.END, ', '.join(row) + '\n')
    except Exception as e:
        messagebox.showerror("Error", f"Could not read CSV file: {e}")

# Function to write new content to the CSV file
def write_csv():
    try:
        content = text_widget.get("1.0", tk.END).strip().splitlines()
        with open(csv_file_path, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            for line in content:
                writer.writerow(line.split(', '))
        messagebox.showinfo("Success", "CSV file overwritten successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not write to CSV file: {e}")

# Function to append text to the CSV file
def append_csv():
    try:
        content = text_widget.get("1.0", tk.END).strip().splitlines()
        with open(csv_file_path, "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            for line in content:
                writer.writerow(line.split(', '))
        messagebox.showinfo("Success", "Text appended to CSV file successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not append to CSV file: {e}")

# Function to delete content of the CSV file
def delete_csv_content():
    try:
        open(csv_file_path, "w").close()  # Clears CSV content
        text_widget.delete("1.0", tk.END)
        messagebox.showinfo("Success", "CSV file content deleted!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not delete CSV file content: {e}")

# Create buttons for CSV operations
read_button = ctk.CTkButton(app, text="Read CSV", command=read_csv)
read_button.pack(pady=5)

write_button = ctk.CTkButton(app, text="Write CSV", command=write_csv)
write_button.pack(pady=5)

append_button = ctk.CTkButton(app, text="Append to CSV", command=append_csv)
append_button.pack(pady=5)

delete_button = ctk.CTkButton(app, text="Delete CSV Content", command=delete_csv_content)
delete_button.pack(pady=5)

# Text widget to display file content
text_widget = tk.Text(app, wrap="word", height=15, width=60)
text_widget.pack(pady=10)

# Run the app
app.mainloop()

# Function to read file
def read_file():
    try:
        with open(file_path, "r") as file:
            content = file.read()
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, content)
    except Exception as e:
        messagebox.showerror("Error", f"Could not read file: {e}")

# Function to write new content to the file
def write_file():
    try:
        content = text_widget.get("1.0", tk.END)
        with open(file_path, "w") as file:
            file.write(content)
        messagebox.showinfo("Success", "File overwritten successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not write to file: {e}")

# Function to append text to the file
def append_file():
    try:
        content = text_widget.get("1.0", tk.END)
        with open(file_path, "a") as file:
            file.write(content)
        messagebox.showinfo("Success", "Text appended successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not append to file: {e}")

# Function to delete content of the file
def delete_content():
    try:
        open(file_path, "w").close()  # Opens the file in write mode to clear content
        text_widget.delete("1.0", tk.END)
        messagebox.showinfo("Success", "File content deleted!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not delete file content: {e}")

# Buttons for each operation
read_button = ctk.CTkButton(app, text="Read File", command=read_file)
read_button.pack(pady=5)

write_button = ctk.CTkButton(app, text="Write File", command=write_file)
write_button.pack(pady=5)

append_button = ctk.CTkButton(app, text="Append to File", command=append_file)
append_button.pack(pady=5)

delete_button = ctk.CTkButton(app, text="Delete Content", command=delete_content)
delete_button.pack(pady=5)

# Text widget to display file content
text_widget = tk.Text(app, wrap="word", height=15, width=50)
text_widget.pack(pady=10)

# Run the app
app.mainloop()
