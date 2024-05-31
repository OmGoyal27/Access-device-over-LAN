import pyautogui as pg
import webbrowser
import os
import subprocess
import pyttsx3
import sys
import ctypes
import time

def go_to_desktop():                                                # minimizes all the current windows and goes to the desktop
    SW_SHOW = 5
    WM_COMMAND = 0x0111
    MIN_ALL = 419
    user32 = ctypes.windll.user32
    shell32 = ctypes.windll.shell32

    # Get the handle of the Shell window (the desktop)
    hwnd = user32.FindWindowW("Shell_TrayWnd", None)

    if hwnd:
        # Send the command to minimize all windows
        user32.SendMessageW(hwnd, WM_COMMAND, MIN_ALL, 0)

def speak(text, speed):                                             # Speaks text using text to speech
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set the speed (words per minute)
    engine.setProperty('rate', speed)

    # Convert text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

def lock_windows():                                             
    user32 = ctypes.windll.User32                                   # Lock the windows machine
    if not user32.LockWorkStation():
        print("Failed to lock workstation", file=sys.stderr)
        sys.exit(1)

def open_link(link):                                            # Opens link in a browser
    webbrowser.open(link)

def shutdown():                                                 # Shuts down the computer
    subprocess.run("shutdown /s /t 0", shell=True)

def hold(key, duration):
    pg.keyDown(key)
    time.sleep(duration)
    pg.keyUp(key)

def hibernate():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")        # Hibernates the windows

def on_key_press(event):                                                # Whenever a key is pressed
    print(f"Key '{event.name}' pressed")