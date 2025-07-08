#include <RH_ASK.h>  // Include RadioHead ASK library
#include <SPI.h>     // Not used but needed to compile

// Create an instance of the RH_ASK driver
RH_ASK driver;

void setup()
{
    // Initialize ASK driver
    if (!driver.init())
    {
        Serial.begin(9600); // Initialize serial port
        Serial.println("Receiver initialization failed!");
    }
    else
    {
        Serial.begin(9600);
        Serial.println("Receiver initialized.");
    }
}

void loop()
{
    uint8_t buf[RH_ASK_MAX_MESSAGE_LEN];  // Buffer for the received message
    uint8_t buflen = sizeof(buf);         // Length of the buffer

    // Check if a message has been received
    if (driver.recv(buf, &buflen))
    {
        Serial.print("Message received: ");
        Serial.println((char*)buf);  // Print the received message
    }
}
