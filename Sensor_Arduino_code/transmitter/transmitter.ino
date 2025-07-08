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
        Serial.println("Transmitter initialization failed!");
    }
    else 
    {
        Serial.begin(9600);
        Serial.println("Transmitter initialized.");
    }
}

void loop()
{
    const char *msg = "RF433 Test";  // Message to send
    driver.send((uint8_t *)msg, strlen(msg)); // Send message
    driver.waitPacketSent(); // Wait until packet has been sent
    Serial.println("Message sent: RF433 Test");
    delay(1000); // Send message every second
}
