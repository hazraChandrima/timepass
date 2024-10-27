# Ensure that you have VLC media player and psutil installed : pip install psutil
# Send this to someone who loves classical music like I do
# Thanks to Ayush Jayaswal for the idea and resource!


import subprocess
import psutil

MUSIC = "https://live.musopen.org:8085/streamvbr0?1729888126216"

def is_VLC_Running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] == "vlc.exe":
            return True
    return False


def strt_VLC():
    subprocess.Popen(["vlc", MUSIC, "--intf", "dummy", "--loop"])


def stop_VLC():
    for process in psutil.process_iter(['name']):
        if process.info['name'] == "vlc.exe":
            process.terminate()


def toggleMusic():
    if is_VLC_Running():
        stop_VLC()
        print("Music stopped.")
    else:
        strt_VLC()
        print("Music started.")


toggleMusic()
