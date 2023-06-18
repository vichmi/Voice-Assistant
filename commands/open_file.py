import os

def open_file(file_name):
    # Assuming the file is in the same directory as the 'commands' directory
    print(file_name)
    file_name = ' '.join(file_name)
    if file_name == 'csgo' or file_name == 'counter strike global offensive' or file_name == 'cs go':
        os.startfile('F:\Games\SteamLibrary\steamapps\common\Counter-Strike Global Offensive')