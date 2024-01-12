import serial
import time
import itertools
print("control_hardware module - activate")

#NOTE: for my ROG laptop, pulg arduino in the USB next to the arrow right key, which is com5

def turn_on_LED(color, port='com5', baudrate=9600): 
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


def rotate_motor(open_or_close_the_lock, port='com5', baudrate=9600): 
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

        if elapsed_time >= 2.5:
            break

        myCmd = open_or_close_the_lock
        myCmd = myCmd + '\r'

        if arduinoData:
            arduinoData.write(myCmd.encode())
        elif not error_message_printed:
            print("arduino not connected. Cannot send command.")
            error_message_printed = True


def check_finger_print(check_or_not, port='com5', baudrate=9600, duration=10):
    finger_check_pass = 0
    arduino_data = None
    error_message_printed = False

    try:
        arduino_data = serial.Serial(port, baudrate, timeout=1)
    except serial.SerialException as e:
        if not error_message_printed:
            print("Breadboard not connected. Cannot send command, check port and baudrate")
            error_message_printed = True

    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time

        if elapsed_time >= duration:
            break

        my_cmd = check_or_not + '\r'

        if arduino_data:
            arduino_data.write(my_cmd.encode())
            response = arduino_data.readline().decode().strip() #read data from finger print reader.

            if "No finger detected" in response:
                print("No finger detected")


            elif "Found a print match!" in response:
                print("Found a print match!")
                finger_check_pass = 1
                return finger_check_pass

            
            elif "Did not find a match" in response:
                print("Did not find a match")
    
    if arduino_data:
        arduino_data.close()




def open_the_door(port='com5',baudrate = '9600'):
    rotate_motor('open',port,baudrate)
    turn_on_LED('G',port,baudrate)
    turn_on_LED('R',port,baudrate)
    rotate_motor('close',port,baudrate)
    turn_on_LED('OFF',port,baudrate)

if __name__ == '__main__':

    finger_check_pass=check_finger_print('check','com5')

    if finger_check_pass:
        open_the_door('com5')

    #open_the_door('com5')


    







