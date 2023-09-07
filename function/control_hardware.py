import serial
import time
import itertools

def turn_on_LED(color, port='com5', baudrate=115200): 
    arduinoData = None
    error_message_printed = False

    try:
        arduinoData = serial.Serial(port, baudrate)
    except serial.SerialException as e:
        if not error_message_printed:
            print("Breadboard not connected. Cannot send command, check port and baudrate")
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


def rotate_motor(open_or_close_the_lock, port='com5', baudrate=115200): 
    arduinoData = None
    error_message_printed = False

    try:
        arduinoData = serial.Serial(port, baudrate)
    except serial.SerialException as e:
        if not error_message_printed:
            print("Breadboard not connected. Cannot send command, check port and baudrate")
            error_message_printed = True

    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time

        if elapsed_time >= 2.7:
            break

        myCmd = open_or_close_the_lock
        myCmd = myCmd + '\r'

        if arduinoData:
            arduinoData.write(myCmd.encode())
        elif not error_message_printed:
            print("arduino not connected. Cannot send command.")
            error_message_printed = True

if __name__ == '__main__':

    rotate_motor('open')
    turn_on_LED('G')
    turn_on_LED('OFF')







