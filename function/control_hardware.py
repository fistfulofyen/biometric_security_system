#the file is used to control all hardware for this porject 
import serial
import time
arduinoData = serial.Serial('com4',115200)
import itertools

import time

def turn_on_LED(color):
    colors = ['R', 'G', 'B']  # List of colors to cycle through
    color_cycle = itertools.cycle(colors)
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time

        if elapsed_time >= 1:
            break

        myCmd = next(color_cycle) if color == 'CYCLE' else color
        myCmd = myCmd + '\r'
        arduinoData.write(myCmd.encode())

if __name__ == '__main__':
    turn_on_LED('OFF')



