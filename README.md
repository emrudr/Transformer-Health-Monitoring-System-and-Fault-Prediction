# Transformer-Health-Monitoring-System-and-Fault-Prediction
A sensor-based Arduino + Python project for real-time transformer fault analysis and health monitoring.

Overview
A sensor-based Arduino + Python project for real-time transformer fault analysis and health monitoring.
The system continuously measures key parameters like voltage, current, temperature, humidity, and vibration, analyzes them using a machine learning model, and automatically isolates the transformer if a fault is detected.

Features
Real-time monitoring of transformer parameters
Anomaly detection using Isolation Forest (Machine Learning)
Automatic trip control via relay & contactor during fault conditions
Continuous data logging to Excel (.xlsx)
Scalable and low-cost design using open-source hardware/sofware

Components Used
| Component                                          | Description                                             |
| -------------------------------------------------- | ------------------------------------------------------- |
| **Arduino Uno**                                    | Central microcontroller for data collection and control |
| **LM35 / DHT11**                                   | Measures transformer temperature and humidity           |
| **ACS712**                                         | Measures load current                                   |
| **ZMPT101B**                                       | Measures AC voltage                                     |
| **SW-420**                                         | Detects abnormal vibrations                             |
| **Songle 5V Relay + Schneider LC1-D32A Contactor** | For automatic circuit isolation                         |
| **12V Battery**                                    | Provides power to Arduino and sensors                   |

Sensor to Arduino Pin Mapping
| Sensor                              | Arduino Pin | Type           |
| ----------------------------------- | ----------- | -------------- |
| ZMPT101B Voltage Sensor             | A0          | Analog         |
| ACS712 Current Sensor               | A2          | Analog         |
| DHT11 Temperature & Humidity Sensor | D6          | Digital        |
| SW-420 Vibration Sensor             | D4          | Digital        |
| Relay Module                        | D5          | Digital Output |


Software & Tools
Arduino IDE (for uploading .ino file)
Python 3.x
Libraries: pyserial, pandas, openpyxl, scikit-learn, matplotlib
Excel for data logging and visualization

Working Principle
Sensors measure voltage, current, temperature, humidity, and vibration.
Arduino sends this data to a Python program via serial communication.
Python script logs the data in Excel and uses machine learning (Isolation Forest) to detect anomalies.
If a fault is detected (overheating, overcurrent, etc.), Python sends a trip signal back to Arduino.
Arduino activates the relay module to open the circuit, simulating transformer isolation.

Data Output Example
| Timestamp           | Current (A) | Temp (°C) | Humidity (%) | Voltage (V) | Vibration |
| ------------------- | ----------- | --------- | ------------ | ----------- | --------- |
| 2025-03-23 13:59:37 | 1.94        | 37.3      | 32.4         | 256.55      | 0         |
| 2025-03-23 14:00:03 | 1.95        | 37.3      | 32.4         | 255.76      | 0         |


Machine Learning Logic
StandardScaler – Normalizes the data.
Isolation Forest – Detects abnormal readings (faults).
Cosine Similarity – Confirms if a detected pattern matches a known fault event.

Future Scope
Integrate GSM/Wi-Fi module for remote alerts
Add mobile dashboard for real-time monitoring
Expand ML model for multiple fault type classification
Cloud-based data storage and visualization
