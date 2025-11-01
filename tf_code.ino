{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs22 \cf2 // Pin connected to the relay\
#define RELAY_PIN 7\
void setup() \{\
Serial.begin(9600); // Start Serial communication\
pinMode(RELAY_PIN, OUTPUT); // Set the relay pin as output\
digitalWrite(RELAY_PIN, LOW); // Ensure the relay is off initially\
\}\
void loop() \{\
// Reading and sending sensor data\
float temperature = 25.6; // Replace with actual sensor readings\
float voltage = 220.0; // Replace with actual sensor readings\
float current = 5.2; // Replace with actual sensor readings\
int vibration = 1; // Replace with actual sensor readings\
// Send sensor data in a comma-separated format\
Serial.print(temperature); Serial.print(",");\
Serial.print(voltage); Serial.print(",");\
Serial.print(current); Serial.print(",");\
Serial.println(vibration);\
// Check for tripping signal from the computer\
if (Serial.available() > 0) \{\
String command = Serial.readStringUntil('\\n'); // Read the command\
if (command == "TRIP") \{\
digitalWrite(RELAY_PIN, HIGH); // Activate the relay\
delay(1000); // Hold the relay for 1 second\
digitalWrite(RELAY_PIN, LOW); // Deactivate the relay\
\}\
\}\
delay(1000); // Delay for 1 second before sending the next data\
\}}