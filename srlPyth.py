import serial
import time
import random

# Configure the serial connection
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)  # Update 'COM3' as needed

# Give time for the connection to be established
time.sleep(2)

# Function to send data to the Arduino
def send_data(data):
    arduino.write(f"{data}\n".encode())  # Send data as bytes
    time.sleep(0.05)
    response = arduino.readline().decode('utf-8').strip()  # Read response
    print("Arduino Response:", response)

# Send a test message
x = []
for i in range(120):
    x.append("Raam")

for data_Bhejo in range(len(x)):
    send_data(x[data_Bhejo])
    # time.sleep(1)

# Close the serial connection when done
arduino.close()
