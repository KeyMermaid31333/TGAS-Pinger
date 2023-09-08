ascii_art = """

 /$$$$$$$$ /$$$$$$   /$$$$$$   /$$$$$$ 
|__  $$__//$$__  $$ /$$__  $$ /$$__  $$
   | $$  | $$  \__/| $$  \ $$| $$  \__/
   | $$  | $$ /$$$$| $$$$$$$$|  $$$$$$ 
   | $$  | $$|_  $$| $$__  $$ \____  $$
   | $$  | $$  \ $$| $$  | $$ /$$  \ $$
   | $$  |  $$$$$$/| $$  | $$|  $$$$$$/
   |__/   \______/ |__/  |__/ \______/ 
                                       
                                       
                                    
"""

print(ascii_art)

import os
import subprocess

# Dictionary of commands and their meanings
commands = {
    'help': 'Show all available commands and their meanings',
    'ping': 'Ping - Status of IP',
    'exit': 'Exit the program',
}

def display_help():
    print("Available commands:")
    for cmd, meaning in commands.items():
        print(f"{cmd}: {meaning}")

def ping_ip(ip_address):
    try:
        subprocess.run(['ping', '-c', '4', ip_address], check=True)
        print(f"Ping to {ip_address} was successful.")
    except subprocess.CalledProcessError:
        print(f"Ping to {ip_address} failed.")

while True:
    user_input = input(">> ").strip().lower()

    if user_input == 'help':
        display_help()
    elif user_input == 'exit':
        break
    elif user_input.startswith('ping '):
        # Split the user input to get the IP address
        ip_to_ping = user_input.split(' ', 1)[1]
        ping_ip(ip_to_ping)
    else:
        print("Command not recognized. Type 'help' for available commands.")
