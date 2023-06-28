import serial
import time
import itertools

def turn_on_LED(color, port='com4', baudrate=115200):
    arduinoData = None
    error_message_printed = False

    try:
        arduinoData = serial.Serial(port, baudrate)
    except serial.SerialException as e:
        if not error_message_printed:
            print("Breadboard not connected. Cannot send command.")
            error_message_printed = True

    colors = ['R', 'G', 'B']  # List of colors to cycle through
    color_cycle = itertools.cycle(colors)
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time

        if elapsed_time >= 1:
            break

        myCmd = next(color_cycle) if color == 'CYCLE' else color
        myCmd = myCmd + '\r'

        if arduinoData:
            arduinoData.write(myCmd.encode())
        elif not error_message_printed:
            print("arduino not connected. Cannot send command.")
            error_message_printed = True

if __name__ == '__main__':
    turn_on_LED('G')





