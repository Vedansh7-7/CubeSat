# List of variable names for reference (just to show the order)
variable_names = [
    "Filt_g_X", "Filt_g_Y", "Filt_g_Z", "Filt_g_net", "Hum", "Temp", 
    "Bx", "By", "Bz", "B_net", "Head", "P", "T", "Alt", 
    "GPS_lat", "GPS_lon", "GPS_time", "GPS_date"
]

# Take comma-separated input from the user
csv_input = input("Enter comma-separated values for Filt_g_X, Filt_g_Y, Filt_g_Z, Filt_g_net, Hum, Temp, Bx, By, Bz, B_net, Head, P, T, Alt, GPS_lat, GPS_lon, GPS_time, GPS_date: ")

# Split the input into a list of values
values = csv_input.split(',')

# Ensure the input has the correct number of values
if len(values) != len(variable_names):
    print(f"Error: You must provide exactly {len(variable_names)} comma-separated values.")
else:
    # Assign each value to its corresponding variable
    Filt_g_X, Filt_g_Y, Filt_g_Z, Filt_g_net, Hum, Temp, Bx, By, Bz, B_net, Head, P, T, Alt, GPS_lat, GPS_lon, GPS_time, GPS_date = values

    # Optionally, print out each variable to verify the assignment
    print(f"Filt_g_X = {Filt_g_X}")
    print(f"Filt_g_Y = {Filt_g_Y}")
    print(f"Filt_g_Z = {Filt_g_Z}")
    print(f"Filt_g_net = {Filt_g_net}")
    print(f"Hum = {Hum}")
    print(f"Temp = {Temp}")
    print(f"Bx = {Bx}")
    print(f"By = {By}")
    print(f"Bz = {Bz}")
    print(f"B_net = {B_net}")
    print(f"Head = {Head}")
    print(f"P = {P}")
    print(f"T = {T}")
    print(f"Alt = {Alt}")
    print(f"GPS_lat = {GPS_lat}")
    print(f"GPS_lon = {GPS_lon}")
    print(f"GPS_time = {GPS_time}")
    print(f"GPS_date = {GPS_date}")