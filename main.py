import pvporcupine
import pyaudio
import struct
import speech_recognition as sr
from commands.spotify_control import skip
import json
import importlib
import colorama
import os
from dotenv import load_dotenv

load_dotenv()

access_key = os.getenv('PVPORCUPINE_ACCESS_KEY')

def listen_for_trigger_phrase(keyword_path):
    keyword_detector = pvporcupine.create(access_key=access_key, keyword_paths=[keyword_path])

    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=keyword_detector.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=keyword_detector.frame_length)

    print("Listening for trigger phrase...")

    while True:
        pcm = audio_stream.read(keyword_detector.frame_length)
        pcm = struct.unpack_from("h" * keyword_detector.frame_length, pcm)
        keyword_index = keyword_detector.process(pcm)
        if keyword_index >= 0:
            print("Trigger phrase detected.")
            break

    audio_stream.close()
    pa.terminate()

def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        command = r.recognize_google(audio).lower()
        print("You said:", command)
        
        command_parts = command.split(' ')

        with open('commands.json') as f:
            command_mapping = json.load(f)
        
        for cmd in command_mapping['commands']:
            aliases = command_mapping['commands'][cmd]['aliases']
            for alias in aliases:
                if alias.lower() in command.lower():
                    module_name = command_mapping['commands'][cmd]['module']
                    function_name = command_mapping['commands'][cmd]['function']
                    module = importlib.import_module(f'commands.{module_name}')
                    command_func = getattr(module, function_name)
                    
                    arguments = command_parts[len(alias.split(' ')):]

                    if len(command_mapping['commands'][cmd]['arguments']) > 0:
                        if cmd in ('add to queue', 'play song'):
                            command_func(' '.join(arguments))
                        else:
                            command_func(*arguments)
                    else:
                        command_func()
                    break
        
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError:
        print("Sorry, I couldn't request results from the speech recognition service.")

# Paths to Porcupine's keyword files (you need to provide your own)
keyword_path = "./hey-victor_en_windows_v2_2_0.ppn"

while True:
    listen_for_trigger_phrase(keyword_path)
    listen_for_command()