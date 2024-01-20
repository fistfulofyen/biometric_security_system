import tkinter as tk
import subprocess
from tkinter import PhotoImage,messagebox, filedialog
import os
import sys
import webbrowser

"""
This script defines a graphical user interface (GUI) using the tkinter library for a HomeLand 
Security System. The GUI provides buttons to activate the system, modify the Bio_DataBase script, 
and check patrol mode recordings. It incorporates functionalities to interact with the Bio_DataBase 
script, enabling the addition of friend names, new persons, and modifications to the script. Additionally, 
it allows the user to check and play recordings from patrol mode.
"""

# Define script_text as a global variable
script_text = None

def on_run_button_click():
    # Create a custom prompt window
    calibration_prompt = tk.Toplevel(root)
    calibration_prompt.title("Calibration Warning")

    # Add calibration message label
    calibration_message = "Make sure to calibrate FOCAL_LENGTH_OF_YOUR_PC and USB_PORT before running the program."
    message_label = tk.Label(calibration_prompt, text=calibration_message)
    message_label.pack(pady=10)

    # Add buttons to navigate to control_hardware.py and face_depth_measure.py
    control_hardware_button = tk.Button(calibration_prompt, text="Calibrate USB_PORT", command=calibrate_usb_port)
    control_hardware_button.pack(side=tk.LEFT, padx=10)

    face_depth_measure_button = tk.Button(calibration_prompt, text="Calibrate FOCAL_LENGTH_OF_YOUR_PC", command=calibrate_focal_length)
    face_depth_measure_button.pack(side=tk.LEFT, padx=10)

    # Add an "OK" button to directly run the script
    ok_button = tk.Button(calibration_prompt, text="OK", command=run_main_script)
    ok_button.pack(side=tk.LEFT, padx=10)

def run_main_script():
    # Open control_hardware.py script or relevant calibration tool
    subprocess.run(["python", "face_recognition_main.py"])

def calibrate_usb_port():
    # Get the absolute path to control_hardware.py
    control_hardware_path = os.path.abspath("function/control_hardware.py")

    # Determine the default text editor based on the operating system
    if sys.platform.startswith('win'):
        editor_command = 'notepad'
    elif sys.platform.startswith('darwin'):
        editor_command = 'open -t'
    elif sys.platform.startswith('linux'):
        editor_command = 'xdg-open'
    else:
        raise RuntimeError('Unsupported operating system')

    # Open control_hardware.py script in the default text editor
    subprocess.run([editor_command, control_hardware_path])


def calibrate_focal_length():
    # Get the absolute path to face_depth_measure.py
    face_depth_measure_path = os.path.abspath("function/face_depth_measure.py")

    # Determine the default text editor based on the operating system
    if sys.platform.startswith('win'):
        editor_command = 'notepad'
    elif sys.platform.startswith('darwin'):
        editor_command = 'open -t'
    elif sys.platform.startswith('linux'):
        editor_command = 'xdg-open'
    else:
        raise RuntimeError('Unsupported operating system')

    # Open face_depth_measure.py script in the default text editor
    subprocess.run([editor_command, face_depth_measure_path])


def on_modify_button_click():
    global script_text  # Declare script_text as a global variable
    # Open a new window for modifying the Bio_DataBase script
    modify_window = tk.Toplevel(root)
    modify_window.title("Bio_DataBase.py Script viewer")

    # Create a text widget for script modification
    script_text = tk.Text(modify_window, height=30, width=120)
    script_text.insert(tk.END, face_recognition_script_content)
    script_text.pack(pady=10)

    # Create a button for adding friend names
    add_friend_button = tk.Button(modify_window, text="Add Friend Name", command=add_friend_names)
    add_friend_button.pack(side=tk.LEFT, padx=10)

    # Create a button for uploading and adding a picture
    adding_new_person_button = tk.Button(modify_window, text="Add New Person", command=adding_new_person)
    adding_new_person_button.pack(side=tk.LEFT, padx=10)

    # Create a button to save all modifications
    save_changes_button = tk.Button(modify_window, text="Save Changes", command=save_changes)
    save_changes_button.pack(side=tk.LEFT, padx=10)


def save_changes():
    global script_text  # Use the global variable script_text
    # Get all the text from script_text and save it to the original file
    modified_script = script_text.get("1.0", tk.END)
    with open("function/Bio_DataBase.py", "w") as script_file:
        script_file.write(modified_script)

    # Display success message
    messagebox.showinfo("Modification", "Changes saved successfully")

def add_friend_names():
    # Open a new window for adding friend names
    add_friend_window = tk.Toplevel(root)
    add_friend_window.title("Add Friend Names")

    # Add instructions label
    instructions_label = tk.Label(add_friend_window, text="Typing the name of the friend")
    instructions_label.pack(pady=10)

    # Create an entry widget for adding friend names
    friend_name_entry = tk.Entry(add_friend_window, width=30)
    friend_name_entry.pack(pady=10)

    # Create a button to add friend names
    add_friend_name_button = tk.Button(add_friend_window, text="Add", command=lambda: insert_friend_name(friend_name_entry.get()))
    add_friend_name_button.pack(pady=10)


def insert_friend_name(friend_name):
    global script_text  # Use the global variable script_text
    # Capitalize the first letter of friend_name
    friend_name = friend_name.capitalize()
    # Insert the new known face name code into the script_text
    code = f'\nknown_friend_names.append("{friend_name}")'
    script_text.insert(tk.END, code)


def adding_new_person():
    global script_text  # Use the global variable script_text
    
    # Open a file dialog for image selection
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg")])

    if file_path:
        # Create a new Tkinter window for user input
        name_window = tk.Toplevel()
        name_window.title("Enter Name")
        
        # Label and Entry for user to input the name
        name_label = tk.Label(name_window, text="Enter the name:")
        name_label.pack()

        name_entry = tk.Entry(name_window)
        name_entry.pack()

        def save_and_close():
            # Getting the name entered by the user
            user_entered_name = name_entry.get().strip()
            
            if user_entered_name:
                # Convert to uppercase and capitalize
                the_name_of_the_pic = user_entered_name.upper()
                the_name_of_the_pic_cap = the_name_of_the_pic.capitalize()

                # Generate code for loading and encoding the image
                code = f'{the_name_of_the_pic}_image = face_recognition.load_image_file("{file_path}")\n'
                code += f'{the_name_of_the_pic}_face_encoding = face_recognition.face_encodings({the_name_of_the_pic}_image)[0]\n'
                code += f'known_face_encodings.append({the_name_of_the_pic}_face_encoding)\n'
                code += f'known_face_names.append("{the_name_of_the_pic_cap}")\n'

                # Insert the generated code into the script_text
                script_text.insert(tk.END, code)

                # Close the name input window
                name_window.destroy()

        # Button to save the name and close the window
        save_button = tk.Button(name_window, text="Save", command=save_and_close)
        save_button.pack()

        # Make sure the user cannot close the name input window without entering a name
        name_window.protocol("WM_DELETE_WINDOW", lambda: None)


def get_variable_name(file_path):
    # Extract the file name without extension as a variable name
    return file_path.split("/")[-1].split(".")[0]

def on_check_recordings_button_click():
    recording_folder = os.getcwd()  # Use the current working directory

    # Get all mp4 files in the recordings folder
    mp4_files = [file for file in os.listdir(recording_folder) if file.endswith(".mp4")]

    if mp4_files:
        # Display a message to the user about available recordings
        message = "Recordings found:\n\n" + "\n".join(mp4_files)
        messagebox.showinfo("Recordings", message)

        # Allow the user to select and play a recording
        selected_file = filedialog.askopenfilename(
            initialdir=recording_folder,
            title="Select Recording",
            filetypes=[("MP4 files", "*.mp4")]
        )

        if selected_file:
            webbrowser.open(selected_file)
    else:
        # Display a message if no recordings are found
        messagebox.showinfo("Recordings", "No recordings found.")


#%% main window button location
        
# Load the content of the Bio_DataBase script
with open("function/Bio_DataBase.py", "r") as script_file:
    face_recognition_script_content = script_file.read()

# Create the main window
root = tk.Tk()
root.title("HomeLand Security System Interface")

# Set the window size to  (height x width)
root.geometry("500x350")

# Load the background image
background_image = PhotoImage(file="Supplementary\document\BGP.png")  # Update the path accordingly

# Create a label with the background image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Cover the entire window with the label

# Create a button to run the external script
run_button = tk.Button(root, text="Activate The System", command=on_run_button_click)
run_button.grid(row=0, column=0, pady=10, padx=(0, 10), sticky='w')  # Adjusted to grid and anchored to the right

# Create a button to modify the script
modify_button = tk.Button(root, text="Modify Bio Data Base", command=on_modify_button_click)
modify_button.grid(row=1, column=0, pady=10, padx=(0, 10), sticky='w')  # Adjusted to grid and anchored to the right

# Create a button to check patrol mode recordings
check_recordings_button = tk.Button(root, text="Check Recordings", command=on_check_recordings_button_click)
check_recordings_button.grid(row=2, column=0, pady=10, padx=(0, 10), sticky='w')  # Adjusted to grid and anchored to the right




# Start the main loop
root.mainloop()
