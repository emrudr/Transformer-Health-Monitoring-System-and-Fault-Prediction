{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs22 \cf2 import serial\
import time\
import matplotlib.pyplot as plt\
from matplotlib.animation import FuncAnimation\
# Configure Serial connection\
arduino_port = "/dev/tty.usbmodem14101" # Replace with your Arduino port\
baud_rate = 9600\
ser = serial.Serial(arduino_port, baud_rate, timeout=1)\
# Initialize data storage\
data_points = \{"time": [], "temperature": [], "voltage": [], "current": [], "vibration": []\}\
start_time = time.time()\
def read_data():\
try:\
line = ser.readline().decode('utf-8').strip()\
if line:\
values = list(map(float, line.split(',')))\
current_time = time.time() - start_time\
data_points["time"].append(current_time)\
data_points["temperature"].append(values[0])\
data_points["voltage"].append(values[1])\
data_points["current"].append(values[2])\
data_points["vibration"].append(values[3])\
# Fault detection logic\
if values[0] > 75 or values[2] > 10: # Example thresholds\
send_tripping_signal()\
return values\
except Exception as e:\
print(f"Error: \{e\}")\
return None\
def send_tripping_signal():\
ser.write(b'TRIP\\n') # Send a trip signal to Arduino\
print("Tripping signal sent to Arduino!")\
def update_graph(i):\
read_data()\
plt.cla()\
plt.subplot(2, 2, 1)\
plt.plot(data_points["time"], data_points["temperature"], label="Temperature")\
plt.ylabel("Temp (\'b0C)")\
plt.legend()\
plt.subplot(2, 2, 2)\
plt.plot(data_points["time"], data_points["voltage"], label="Voltage")\
plt.ylabel("Volt (V)")\
plt.legend()\
plt.subplot(2, 2, 3)\
plt.plot(data_points["time"], data_points["current"], label="Current")\
plt.ylabel("Curr (A)")\
plt.legend()\
plt.subplot(2, 2, 4)\
plt.plot(data_points["time"], data_points["vibration"], label="Vibration")\
plt.ylabel("Vibration")\
plt.legend()# Setup live graph\
ani = FuncAnimation(plt.gcf(), update_graph, interval=1000)\
plt.tight_layout()\
plt.show()\
# Close Serial connection on exit\
ser.close()}