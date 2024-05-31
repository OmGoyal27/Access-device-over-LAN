import pyautogui as pg
import socket
import random
from functions import *


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(1)
print("Waiting for a connection...")
client, addr = server.accept()
print("Connection from", addr) # When it receives a connection

def execute(script):
    if script == "shutdown":
        shutdown()
    
    if script == "quit":
        pg.hotkey("alt", "F4")                                      # ALT+F4 is the shortcut for exiting an app on windows.

    if script == "hibernate":
        hibernate()
    
    if script == "rickroll":
        open_link("https://www.youtube.com/watch?v=xvFZjo5PgG0")    # Opens a YouTube rickroll page

    if script == "hold w":                                          # Holds the 'w' key down for a random amount of time
        hold_time = random.randint(1, 7)
        hold("w", hold_time)
    
    if script == "desktop":
        go_to_desktop()

    if script == "lock":
        lock_windows()

    if script.startswith("press"):
        key = script.split(":")
        key = key[1]
        pg.hotkey(key)

    if script.startswith("popup"):                                  # Gives a popup message
        popup = script.split(":")
        popup = popup[1]
        pg.alert(popup, "Warning!")

    if script.startswith("speak"):                                  # Speaks a message
        text = script.split(":")
        text = popup[1]
        speak(text, 120)

while True:
    data = client.recv(1024)
    if not data:
        break

    received_message = data.decode('utf-8') # Received message
    print("Received:", received_message)
    execute(received_message)

# Close the client connection
client.close()
