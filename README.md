# CubeSat

## Overview
This project involves the design, integration, and testing of a CubeSat prototype equipped with multiple sensors for environmental and positional data acquisition. The CubeSat includes a custom-designed PCB that integrates various sensors and communicates with an external Arduino Uno for data processing and transmission.

## Features
- **Sensor Integration:** 
  - Magnetometer (GY-271)
  - Pressure & Altitude Sensor (BMP180 - HW-415)
  - Humidity Sensor (DHT11)
  - GPS Module (GY-NEO6MV2)
  - Inertial Measurement Unit (IMU - GY-521)
  - High-Precision Pressure Sensor (Hx710B)
  - RF Communication Module (RF433 - Receiver)
- **Custom PCB:** Designed to integrate all sensors and route connections to an external Arduino Uno.
- **Wireless Data Transmission:** Uses RF433 for communication.
- **Power Management:** Ensures stable power delivery to all components.
- **Graphical User Interface (GUI):** A user-friendly interface for real-time data visualization and monitoring.

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
| High-Precision Sensor | Hx710B |
| RF Module | RF433 Receiver |
| Custom PCB | Designed for sensor integration |

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

## Conclusion
This CubeSat prototype demonstrates a successful integration of multiple sensors, a well-designed PCB, and a functional data acquisition system. The project serves as a foundation for further advancements in small satellite technology and environmental data monitoring.



