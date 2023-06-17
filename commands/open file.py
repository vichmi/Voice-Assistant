import os

def open_file(file_name):
    # Assuming the file is in the same directory as the 'commands' directory
    file_path = os.path.join(os.path.dirname('F:\Programming\Projects\Assistant'), file_name)
    print(file_path)
    if os.path.exists(file_path):
        print('asd')
        os.startfile(file_path)  # Open the file
        print("File opened successfully.")
    else:
        print("File not found.")

open_file('not.mp3')