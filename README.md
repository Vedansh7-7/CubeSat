# CubeSat

## Overview
This project involves designing, integrating, and testing a CubeSat prototype equipped with multiple sensors for environmental and positional data acquisition. The CubeSat includes a custom-designed PCB that integrates various sensors and communicates with an external Arduino Uno for data processing and transmission.

## Features
- **Sensor Integration:** 
  - Magnetometer (GY-271)
  - Pressure & Altitude Sensor (BMP180 - HW-415)
  - Humidity Sensor (DHT11)
  - GPS Module (GY-NEO6MV2)
  - Inertial Measurement Unit (IMU - GY-521)
  - RF Communication Module (RF433 - Receiver)
- **Custom PCB:** Designed to integrate all sensors and route connections to an external Arduino Uno.
- **Wireless Data Transmission:** Uses RF433 for communication.
- **Power Management:** Ensures stable power delivery to all components.
- **Graphical User Interface (GUI):** A user-friendly real-time data visualization and monitoring interface.

## System Architecture
The CubeSat consists of:
- A **sensor module** mounted on a PCB with routed connections.
- An **Arduino Uno** for data acquisition and processing.
- A **transmission system** to send real-time data.
- A **GUI** for displaying and analyzing collected data.
- Power supply and voltage regulation for stable operation.

## Hardware Components
| Component | Model |
|-----------|-------|
| Microcontroller | Arduino Uno |
| Magnetometer | GY-271 |
| Pressure Sensor | BMP180 (HW-415) |
| Humidity Sensor | DHT11 |
| GPS Module | GY-NEO6MV2 |
| IMU | GY-521 |
| RF Module | RF433 Receiver |
| Custom PCB | Designed for sensor integration |

## Design & Structural Analysis
The CubeSat structure was designed with an emphasis on modularity and accessibility, featuring a 3D-printed frame with open sides for easy sensor inspection and debugging. Finite Element Analysis (FEA) was performed using ANSYS to evaluate structural integrity under launch-like conditions, ensuring that the CubeSat could withstand vibrations and mechanical stresses. The layout was optimized for minimal weight while maintaining robustness, laying the groundwork for future space-qualified designs.

## PCB Design
- Designed to connect all sensors while keeping the Arduino Uno external.
- Ensures proper routing and signal integrity.
- Optimized for compactness and ease of assembly.

## Software & Communication
- **Programming Language:** Arduino (C++)
- **Libraries Used:**
  - Wire.h (for I2C communication)
  - SoftwareSerial.h (for GPS module)
  - Adafruit_Sensor.h (for various sensor readings)
  - RF433 communication libraries
- **Data Processing:**
  - Sensor data is read and formatted.
  - Processed data is transmitted via RF433.
  - Data logging for further analysis.
- **Graphical User Interface (GUI):**
  - Developed for real-time monitoring and visualization.
  - Displays sensor readings in an intuitive format.
  - Provides interactive controls for data analysis.

## Challenges & Solutions
- **Sensor Integration Issues:** Proper calibration and filtering were applied.
- **RF Communication Reliability:** Optimized antenna placement for better signal strength.
- **PCB Design Constraints:** Ensured correct routing and sufficient power delivery.
- **GUI Development:** Designed for ease of use and real-time responsiveness.

## Future Improvements
- **Better Power Management:** Implementing a more efficient power distribution system.
- **Telemetry & Remote Control:** Enhancing real-time monitoring and control capabilities.
- **Enclosure & Deployment Testing:** Testing under environmental conditions similar to space missions.
- **GUI Enhancements:** Adding advanced visualization features and real-time analytics.

## Images

![aa92c437-c04f-4863-9463-d0a5509d6f2c](https://github.com/user-attachments/assets/bd93c1db-17b8-494b-8385-38fd62592d15)

![3a626917-b77e-4af9-b07b-a473a621790c](https://github.com/user-attachments/assets/975991e4-fac4-4fe6-b609-a2f26e9ba26b)



## Conclusion
This CubeSat prototype successfully integrates multiple sensors, a well-designed PCB, and a functional data acquisition system. The project is a foundation for further advancements in small satellite technology and environmental data monitoring.



