#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_HMC5883_U.h>
#include <Adafruit_BMP085_U.h>
#include <MPU6050.h>
#include <dht.h>
#include <TinyGPS++.h>
#include <SoftwareSerial.h>
#include <RH_ASK.h>
#include <SPI.h> // Not actually used but needed to compile
#include<RadioHead.h>
//DHT 
dht DHT;

#define DHT11_PIN 7

Adafruit_HMC5883_Unified mag = Adafruit_HMC5883_Unified(12345);  // magnetometer
Adafruit_BMP085_Unified bmp = Adafruit_BMP085_Unified(10085);    // pressure altitute temp

//Accelerometer
MPU6050 mpu;
long accelX, accelY, accelZ;
float gForceX, gForceY, gForceZ;
long accelXOffset = 0, accelYOffset = 0, accelZOffset = 0;

float alpha = 0.5;  // Low-pass filter constant (can be adjusted)
float prevX = 0, prevY = 0, prevZ = 0;
float lowPassFilter(float currentValue, float previousValue) 
  {
    return previousValue + alpha * (currentValue - previousValue);
  }
long accelXSum = 0, accelYSum = 0, accelZSum = 0;
  const int calibrationSamples = 1000; // Number of samples for calibration
  
//GPS
TinyGPSPlus gps;
SoftwareSerial ss(4, 3); // RX, TX (connect RX of GPS to pin 4 and TX to pin 3)

//Accelerometer
void calibrateAccelerometer() 
{
  Serial.println("Calibrating accelerometer...");
  accelXSum = 0;
  accelYSum = 0;
  accelZSum = 0;

  for (int i = 0; i < calibrationSamples; i++) 
  {
    int16_t ax, ay, az;
    mpu.getAcceleration(&ax, &ay, &az);
    accelXSum += ax;
    accelYSum += ay;
    accelZSum += az;
    delay(5);  // Short delay to avoid overwhelming the sensor
  }

  // Calculate offsets
  accelXOffset = accelXSum / calibrationSamples;
  accelYOffset = accelYSum / calibrationSamples;
  accelZOffset = (accelZSum / calibrationSamples) - 16384;

  Serial.print("Accel Offsets - X: "); Serial.print(accelXOffset);
  Serial.print(" | Y: "); Serial.print(accelYOffset);
  Serial.print(" | Z: "); Serial.println(accelZOffset);
  Serial.println("Accelerometer Calibration done.");
}

float lowPassFilter(float currentValue, float previousValue);


void setup() 
{
 Serial.begin(9600);
 ss.begin(9600);
  Wire.begin();
  mpu.initialize();
  // Check if MPU6050 is connected properly
  if (!mpu.testConnection()) 
  {
    Serial.println("MPU6050 connection failed!");
    while (1);  // Halt the program if MPU6050 is not connected
  }

  //Magnetometer
  if(!mag.begin())
  {
    /* There was a problem detecting the HMC5883 ... check your connections */
    Serial.println("Ooops, no HMC5883 detected ... Check your wiring!");
    while(1);
  }
  if(!bmp.begin())
  {
    /* There was a problem detecting the BMP085 ... check your connections */
    Serial.print("Ooops, no BMP085 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }

  // Accelerometer
  calibrateAccelerometer();
}
void loop() 
{
  //DHT
  int chk = DHT.read11(DHT11_PIN);
  Serial.print("Temperature = ");
  Serial.println(DHT.temperature);
  Serial.print("Humidity = ");
  Serial.println(DHT.humidity);
  delay(1000);

  //Magnetometer
  sensors_event_t magevent; 
  mag.getEvent(&magevent);
 
  /* Display the results (magnetic vector values are in micro-Tesla (uT)) */
  Serial.print("X: "); Serial.print(magevent.magnetic.x); Serial.print("  ");
  Serial.print("Y: "); Serial.print(magevent.magnetic.y); Serial.print("  ");
  Serial.print("Z: "); Serial.print(magevent.magnetic.z); Serial.print("  ");Serial.println("uT");

  // Hold the module so that Z is pointing 'up' and you can measure the heading with x&y
  // Calculate heading when the magnetometer is level, then correct for signs of axis.
  float heading = atan2(magevent.magnetic.y, magevent.magnetic.x);
  
  float declinationAngle = 0.37;
  heading += declinationAngle;
  float headingDegrees = heading * 180/M_PI - 70; 
  // Correct for when signs are reversed.
  if(headingDegrees < 0)
    headingDegrees += 360;
    
  // Check for wrap due to addition of declination.
  if(headingDegrees > 360)
    headingDegrees -= 360;
  

  Serial.print("Magnetic field magnitude ");
  Serial.println(sqrt(sq(magevent.magnetic.x) + sq(magevent.magnetic.y) + sq(magevent.magnetic.z)));

  if(headingDegrees > 337.25 || headingDegrees < 22.5)
  {
    Serial.print("Heading (degrees): "); Serial.print(headingDegrees); Serial.println(" N ");
  }
  else if(headingDegrees > 292.5 && headingDegrees < 337.25)
  {
    Serial.print("Heading (degrees): "); Serial.print(headingDegrees); Serial.println(" NW ");
  }
  else if(headingDegrees > 247.5 && headingDegrees < 292.5)
  {
  Serial.print("Heading (degrees): "); Serial.print(headingDegrees); Serial.println(" W ");
  }
  else if(headingDegrees > 202.5 && headingDegrees < 247.5)
  {
    Serial.print("Heading (degrees): "); Serial.print(headingDegrees); Serial.println(" SW ");
  }
  else if(headingDegrees > 157.5 && headingDegrees < 202.5)
  {
    Serial.print("Heading (degrees): "); Serial.print(headingDegrees); Serial.println(" S ");
  }
  else if(headingDegrees > 112.5 && headingDegrees < 157.5)
  {
    Serial.print("Heading (degrees): "); Serial.print(headingDegrees); Serial.println(" SE ");
  }
  else if(headingDegrees > 67.5 && headingDegrees < 112.5)
  {
    Serial.print("Heading (degrees): "); Serial.print(headingDegrees); Serial.println(" E ");
  }
  else if(headingDegrees > 0 && headingDegrees < 67.5)
  {
    Serial.print("Heading (degrees): "); Serial.print(headingDegrees); Serial.println(" NE ");
  }
  
  delay(500);
  // PRESSURE ALT TEMP
  /* Get a new sensor event */ 
  sensors_event_t pltevent;
  bmp.getEvent(&pltevent);
 
  if (pltevent.pressure)
  {
    /* Display atmospheric pressue in hPa */
    Serial.print("Pressure:    ");
    Serial.print(pltevent.pressure);
    Serial.println(" hPa");
    
    float temperature;
    bmp.getTemperature(&temperature);
    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.println(" C");

    /* Then convert the atmospheric pressure, and SLP to altitude         */
    /* Update this next line with the current SLP for better results      */
    float seaLevelPressure = SENSORS_PRESSURE_SEALEVELHPA;
    Serial.print("Altitude:    "); 
    Serial.print(bmp.pressureToAltitude(seaLevelPressure,
                                        pltevent.pressure)); 
    Serial.println(" m");
    Serial.println("");
  }
  else
  {
    Serial.println("Sensor error");
  }

  // ACCELEROMETER
  
  // Read raw accelerometer data
  accelX = mpu.getAccelerationX() - accelXOffset;
  accelY = mpu.getAccelerationY() - accelYOffset;
  accelZ = mpu.getAccelerationZ() - accelZOffset;

  // Apply a low-pass filter to smooth the values
  gForceX = lowPassFilter(accelX / 16384.0, prevX);
  gForceY = lowPassFilter(accelY / 16384.0, prevY);
  gForceZ = lowPassFilter(accelZ / 16384.0, prevZ);

  // Update previous values for the filter
  prevX = gForceX;
  prevY = gForceY;
  prevZ = gForceZ;

  // Calculate net acceleration
  float netAcceleration = sqrt(gForceX * gForceX + gForceY * gForceY + gForceZ * gForceZ);

  // Output the filtered acceleration values in g
  Serial.print("Filtered Acceleration in g | X: "); Serial.print(gForceX, 2);
  Serial.print(" | Y: "); Serial.print(gForceY, 2);
  Serial.print(" | Z: "); Serial.print(gForceZ, 2);
  Serial.print(" | Net: "); Serial.println(netAcceleration, 2);  // Output the net acceleration

  delay(500);  // Slow down the output for readability

  //GPS
  while (ss.available())
  {
    gps.encode(ss.read());
    
    // Check if new GPS data is available
    if (gps.location.isUpdated()) {
      Serial.print("Latitude: ");
      Serial.print(gps.location.lat(), 6); // 6 decimal places
      Serial.print(" Longitude: ");
      Serial.println(gps.location.lng(), 6);
    } else {
      Serial.println("Waiting for location data...");
    }
    
    // Debugging output for date and time
    if (gps.date.isUpdated()) {
      Serial.print("Date: ");
      Serial.print(gps.date.day());
      Serial.print("/");
      Serial.print(gps.date.month());
      Serial.print("/");
      Serial.println(gps.date.year());
    }

    if (gps.time.isUpdated()) {
      Serial.print("Time: ");
      Serial.print(gps.time.hour());
      Serial.print(":");
      Serial.print(gps.time.minute());
      Serial.print(":");
      Serial.println(gps.time.second());
    }
  }
}