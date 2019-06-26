import serial
import csv
import time
import numpy as np
import warnings
import serial
import serial.tools.list_ports

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'Arduino' in p.description
]
if not arduino_ports:
    raise IOError("No Arduino found")
if len(arduino_ports) > 1:
    warnings.warn('Multiple Arduinos found - using the first')

Arduino = serial.Serial(arduino_ports[0])
Arduino.flush()
Arduino.reset_input_buffer()

start_time=time.time()
Distance = 0.5 # This is how long the lever arm is in feet

while True:
    while (Arduino.inWaiting()==0):
        pass
    try:
        data = Arduino.readline()
        dataarray = data.decode().rstrip().split(',')
        Arduino.reset_input_buffer()
        Force = float(dataarray[0])
        RPM = float (dataarray[1])
        Torque = Force * Distance
        HorsePower = Torque * RPM / 5252
        Run_time = time.time()-start_time
        print (Force , 'Grams',"," , RPM ,'RPMs',"," ,Torque,"ft-lbs",",", HorsePower, "hp", Run_time, "Time Elasped")
    except (KeyboardInterrupt, SystemExit,IndexError,ValueError):
        pass
    with open('DynoData.csv', 'w') as outfile:
        outfileWrite = csv.writer(outfile)        
        while True:
            outfileWrite.writerow([Force, RPM])