import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import csv


# Function to read CSV file
def read_csv(csv_file_path = r"File.csv", textA= tk.Text):
    try:
        textA.delete("1.0", tk.END)
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                textA.insert(tk.END, ', '.join(row) + '\n')
    except Exception as e:
        messagebox.showerror("Error", f"Could not read CSV file: {e}")

# Function to write new content to the CSV file
def write_csv(csv_file_path = r"File.csv", textA= tk.Text):
    try:
        content = textA.get("1.0", tk.END).strip().splitlines()
        with open(csv_file_path, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            for line in content:
                writer.writerow(line.split(', '))
        messagebox.showinfo("Success", "CSV file overwritten successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not write to CSV file: {e}")

# Function to append text to the CSV file
def append_csv(csv_file_path = r"File.csv", textA= tk.Text):
    try:
        content = textA.get("1.0", tk.END).strip().splitlines()
        with open(csv_file_path, "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            for line in content:
                writer.writerow(line.split(', '))
        messagebox.showinfo("Success", "Text appended to CSV file successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not append to CSV file: {e}")

# Function to delete content of the CSV file
def delete_csv_content(csv_file_path = r"File.csv", textA= tk.Text):
    try:
        open(csv_file_path, "w").close()  # Clears CSV content
        textA.delete("1.0", tk.END)
        messagebox.showinfo("Success", "CSV file content deleted!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not delete CSV file content: {e}")

# # Create buttons for CSV operations
# read_button = ctk.CTkButton(app, text="Read CSV", command=read_csv)
# read_button.pack(pady=5)

# write_button = ctk.CTkButton(app, text="Write CSV", command=write_csv)
# write_button.pack(pady=5)

# append_button = ctk.CTkButton(app, text="Append to CSV", command=append_csv)
# append_button.pack(pady=5)

# delete_button = ctk.CTkButton(app, text="Delete CSV Content", command=delete_csv_content)
# delete_button.pack(pady=5)

# def textA(frame):
# # Text widget to display file content
#     textA = tk.Text(frame, wrap="word", height=15, width=60)
#     textA.pack(pady=10)

