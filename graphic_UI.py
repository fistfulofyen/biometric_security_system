import tkinter as tk
from tkinter import filedialog
import subprocess
import face_recognition
from tkinter import PhotoImage

# Define script_text as a global variable
script_text = None

def on_run_button_click():
    subprocess.run(["python", "face_recognition_main.py"])

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
    success_label.config(text="Changes saved successfully")

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
    # Insert the new known face name code into the script_text
    code = f'\nknown_friend_names.append("{friend_name}")'
    script_text.insert(tk.END, code)


def adding_new_person():
    global script_text  # Use the global variable script_text
    # Open a file dialog for image selection
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg")])

    if file_path:
        # Getting the name of the picture
        the_name_of_the_pic = get_variable_name(file_path)
        # Getting the name of the picture with the first letter capitalized and the rest in lowercase
        the_name_of_the_pic_cap = get_variable_name(file_path).capitalize()

        # Generate code for loading and encoding the image
        code = f'{the_name_of_the_pic}_image = face_recognition.load_image_file("{file_path}")\n'
        code += f'{the_name_of_the_pic}_face_encoding = face_recognition.face_encodings({the_name_of_the_pic}_image)[0]\n'
        code += f'known_face_encodings.append({the_name_of_the_pic}_face_encoding)\n'
        code += f'known_face_names.append("{the_name_of_the_pic_cap}")\n'

        # Insert the generated code into the script_text
        script_text.insert(tk.END, code)


def get_variable_name(file_path):
    # Extract the file name without extension as a variable name
    return file_path.split("/")[-1].split(".")[0]

# Load the content of the Bio_DataBase script
with open("function/Bio_DataBase.py", "r") as script_file:
    face_recognition_script_content = script_file.read()

# Create the main window
root = tk.Tk()
root.title("HomeLand Security System Interface")

# Set the window size to  (height x width)
root.geometry("500x350")

# Load the background image
background_image = PhotoImage(file="Supplementary\BGP.png")  # Update the path accordingly

# Create a label with the background image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Cover the entire window with the label

# Create a button to run the external script
run_button = tk.Button(root, text="Activate The System", command=on_run_button_click)
run_button.pack(pady=10)

# Create a button to modify the script
modify_button = tk.Button(root, text="Modify Bio_DataBase.py", command=on_modify_button_click)
modify_button.pack(pady=10)

# Create a label for displaying success messages
success_label = tk.Label(root, text="")
success_label.pack(pady=10)

# Start the main loop
root.mainloop()
