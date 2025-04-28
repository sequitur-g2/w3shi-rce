import subprocess
import sys

def open_notepad_once():
    if sys.platform == "win32":
        try:
            subprocess.Popen(["notepad.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass

open_notepad_once()
