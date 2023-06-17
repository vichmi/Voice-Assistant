import sounddevice as sd
from pycaw.pycaw import AudioUtilities

def change_playback_device():
    devices = sd.query_devices()
    print(devices)
    current_device = sd.default.device
    # Find the target device among the available devices
    for device in devices:
        if device['name'] == "Speakers (THX Spatial - Synapse)":
            target_device = "Speakers (Realtek High Definition Audio)"
            sd.default.device = target_device
            return target_device
        elif device['name'] == "Speakers (Realtek High Definition Audio)":
            target_device = "Speakers (THX Spatial - Synapse)"
            sd.default.device = target_device
            return target_device

    return None


# print(change_playback_device())
change_playback_device()