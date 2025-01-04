import tkinter as tk
import serial
import serial.tools.list_ports
import threading
import csv
import math
import os

class SerialReader:
    def __init__(self, port, baudrate, file_path):
        self.serial = serial.Serial(port, baudrate, timeout=1)
        self.file_path = file_path
        self.running = True

    def read_serial(self):
        while self.running:
            if self.serial.in_waiting > 0:
                line = self.serial.readline().decode('utf-8').strip()
                self.save_to_csv(line)
                app.update_display(line)
                app.update_cube_orientation(line)

    def save_to_csv(self, data):
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([data])

    def stop(self):
        self.running = False
        self.serial.close()

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Arduino Serial Data and Cube Rotation")

        # Create a frame for serial data
        self.frame1 = tk.Frame(master)
        self.frame1.pack(side=tk.LEFT)

        # Entry for COM Port
        self.com_label = tk.Label(self.frame1, text="COM Port:")
        self.com_label.pack()
        self.com_entry = tk.Entry(self.frame1)
        self.com_entry.pack()

        # Entry for CSV File Path
        self.file_label = tk.Label(self.frame1, text="CSV File Path:")
        self.file_label.pack()
        self.file_entry = tk.Entry(self.frame1)
        self.file_entry.pack()

        # Status label for connection
        self.status_label = tk.Label(self.frame1, text="OFFLINE", fg="red", font=("Helvetica", 12))
        self.status_label.pack()

        # Serial Data Section
        self.text_area = tk.Text(self.frame1, height=20, width=50)
        self.text_area.pack()

        self.start_button = tk.Button(self.frame1, text="Start", command=self.start_reading)
        self.start_button.pack()

        # Button to hide/show data received frame
        self.toggle_data_button = tk.Button(self.frame1, text="Toggle Data Frame", command=self.toggle_data_display)
        self.toggle_data_button.pack()

        # Button to hide/show cube sketch
        self.toggle_cube_button = tk.Button(self.frame1, text="Toggle Cube Display", command=self.toggle_cube_display)
        self.toggle_cube_button.pack()

        self.serial_reader = None

        # Create a frame for cube rotation
        self.frame2 = tk.Frame(master)
        self.frame2.pack(side=tk.RIGHT)

        # Initialize Cube Drawing
        self.canvas = tk.Canvas(self.frame2, width=400, height=400, bg="white")
        self.canvas.pack()

        # 3D Cube Vertices and Edges
        self.vertices = self.initialize_cube_vertices()
        self.edges = self.initialize_cube_edges()
        
        # Default angles
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0

        # Initial drawing of the cube
        self.draw_cube()

        # Toggle for continuous updates
        self.is_rotating = False

        # Handle window close
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def initialize_cube_vertices(self):
        return [
            [-50, -50, -50],
            [50, -50, -50],
            [50, 50, -50],
            [-50, 50, -50],
            [-50, -50, 50],
            [50, -50, 50],
            [50, 50, 50],
            [-50, 50, 50]
        ]

    def initialize_cube_edges(self):
        return [
            [0, 1], [1, 2], [2, 3], [3, 0],
            [0, 4], [1, 5], [2, 6], [3, 7],
            [4, 5], [5, 6], [6, 7], [7, 4]
        ]

    def init_cube_front_face(self):
        return [
            [0, 1, 2, 3]
        ]

    def update_display(self, data):
        self.text_area.insert(tk.END, data + '\n')
        self.text_area.see(tk.END)  # Scroll to the end

    def start_reading(self):
        port = self.com_entry.get()  # Get the COM port from the entry
        file_path = self.file_entry.get()  # Get the CSV file path from the entry
        
        # Validate COM port and file path
        if self.validate_inputs(port, file_path):
            self.serial_reader = SerialReader(port=port, baudrate=9600, file_path=file_path)
            self.thread = threading.Thread(target=self.serial_reader.read_serial)
            self.thread.start()
            self.update_status("ONLINE", "green")
        else:
            self.update_status("OFFLINE", "red")

    def validate_inputs(self, port, file_path):
        # Check if the port is available and the file path exists
        available_ports = [p.device for p in serial.tools.list_ports.comports()]  # List available COM ports
        if port not in available_ports:  # Check if the specified port is available
            return False
        if not os.path.isfile(file_path):  # Check if file path exists
            return False
        return True

    def update_status(self, status, color):
        self.status_label.config(text=status, fg=color)

    def rotate_cube(self, angle_x, angle_y, angle_z):
        cos_x, sin_x = math.cos(angle_x), math.sin(angle_x)
        cos_y, sin_y = math.cos(angle_y), math.sin(angle_y)
        cos_z, sin_z = math.cos(angle_z), math.sin(angle_z)

        for i in range(len(self.vertices)):
            x, y, z = self.vertices[i]

            # Rotation around x-axis
            new_y = y * cos_x - z * sin_x
            new_z = y * sin_x + z * cos_x
            y, z = new_y, new_z

            # Rotation around y-axis
            new_x = x * cos_y + z * sin_y
            new_z = -x * sin_y + z * cos_y
            x, z = new_x, new_z

            # Rotation around z-axis
            new_x = x * cos_z - y * sin_z
            new_y = x * sin_z + y * cos_z
            x, y = new_x, new_y       

            self.vertices[i] = [x, y, z]

    def draw_cube(self):
        self.canvas.delete('cube')
        self.canvas.delete('face')
        for edge in self.edges:
            p1 = self.project(self.vertices[edge[0]])
            p2 = self.project(self.vertices[edge[1]])
            self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], tags="cube")

        # Draw the front face
        for face in self.init_cube_front_face():
            p1 = self.project(self.vertices[face[0]])
            p2 = self.project(self.vertices[face[1]])
            p3 = self.project(self.vertices[face[2]])
            p4 = self.project(self.vertices[face[3]])
            self.canvas.create_polygon(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1], p4[0], p4[1], outline="#000000", fill="orange", width=2, tag='face')

    def project(self, vertex):
        fov = 250
        scale = fov / (fov + vertex[2])
        x = vertex[0] * scale + 200  # Center the cube in the canvas
        y = vertex[1] * scale + 200  # Center the cube in the canvas
        return [x, y]

    def toggle_cube_display(self):
        # Toggle the visibility of the canvas (3D cube sketch)
        if self.canvas.winfo_ismapped():
            self.canvas.pack_forget()  # Hide the canvas
        else:
            self.canvas.pack()  # Show the canvas

    def toggle_data_display(self):
        # Toggle the visibility of the text area (data received frame)
        if self.text_area.winfo_ismapped():
            self.text_area.pack_forget()  # Hide the text area
        else:
            self.text_area.pack()  # Show the text area

    def toggle_rotation(self):
        self.is_rotating = not self.is_rotating
        if self.is_rotating:
            self.update_continuous_rotation()

    def update_continuous_rotation(self):
        if self.is_rotating:
            self.draw_cube()  # Redraw the cube with current orientation
            self.master.after(100, self.update_continuous_rotation)  # Update every 100 milliseconds

    def update_cube_orientation(self, data):
        try:
            # Assuming data format is "angle_x,angle_y,angle_z"
            angles = list(map(float, data.split(',')))
            self.angle_x, self.angle_y, self.angle_z = angles
            self.rotate_cube(self.angle_x * math.pi / 180, self.angle_y * math.pi / 180, self.angle_z * math.pi / 180)
            self.draw_cube()
        except Exception as e:
            print("Error updating cube orientation:", e)

    def on_closing(self):
        if self.serial_reader:
            self.serial_reader.stop()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


