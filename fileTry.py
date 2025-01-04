import customtkinter as ctk
import math

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("3D Cube Rotation Demo")

        # Create a frame for cube rotation
        self.frame = ctk.CTkFrame(master, width=400, height=400)
        self.frame.pack(padx=10, pady=10)

        # Initialize Cube Drawing
        self.canvas = ctk.CTkCanvas(self.frame, width=400, height=400, bg="white")
        self.canvas.pack()

        # 3D Cube Vertices and Edges
        self.vertices = self.initialize_cube_vertices()
        self.edges = self.initialize_cube_edges()

        # Default rotation angles
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0

        # Start continuous rotation
        self.rotate_cube()

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

    def project(self, vertex):
        fov = 250  # Field of view
        scale = fov / (fov + vertex[2])
        x = vertex[0] * scale + 200  # Center the cube in the canvas
        y = vertex[1] * scale + 200  # Center the cube in the canvas
        return [x, y]

    def rotate_vertices(self, angle_x, angle_y, angle_z):
        cos_x, sin_x = math.cos(angle_x), math.sin(angle_x)
        cos_y, sin_y = math.cos(angle_y), math.sin(angle_y)
        cos_z, sin_z = math.cos(angle_z), math.sin(angle_z)

        for i in range(len(self.vertices)):
            x, y, z = self.vertices[i]

            # Rotate around X-axis
            new_y = y * cos_x - z * sin_x
            new_z = y * sin_x + z * cos_x
            y, z = new_y, new_z

            # Rotate around Y-axis
            new_x = x * cos_y + z * sin_y
            new_z = -x * sin_y + z * cos_y
            x, z = new_x, new_z

            # Rotate around Z-axis
            new_x = x * cos_z - y * sin_z
            new_y = x * sin_z + y * cos_z
            x, y = new_x, new_y

            self.vertices[i] = [x, y, z]

    def draw_cube(self):
        self.canvas.delete('cube')
        self.canvas.delete('face')

        # Draw edges
        for edge in self.edges:
            p1 = self.project(self.vertices[edge[0]])
            p2 = self.project(self.vertices[edge[1]])
            self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], tags="cube", fill="black", width=2)

        # Draw the front face in orange
        front_face = [0, 1, 2, 3]
        p1 = self.project(self.vertices[front_face[0]])
        p2 = self.project(self.vertices[front_face[1]])
        p3 = self.project(self.vertices[front_face[2]])
        p4 = self.project(self.vertices[front_face[3]])
        self.canvas.create_polygon(
            p1[0], p1[1], p2[0], p2[1],
            p3[0], p3[1], p4[0], p4[1],
            outline="black", fill="orange", width=2, tags="face"
        )

    def rotate_cube(self):
        # Update angles for rotation
        self.angle_x += math.radians(2)
        self.angle_y += math.radians(3)
        self.angle_z += math.radians(1)

        # Rotate vertices
        self.rotate_vertices(self.angle_x, self.angle_y, self.angle_z)

        # Redraw the cube
        self.draw_cube()

        # Schedule the next frame
        self.master.after(500, self.rotate_cube)

if __name__ == "__main__":
    app = ctk.CTk()
    App(app)
    app.mainloop()
