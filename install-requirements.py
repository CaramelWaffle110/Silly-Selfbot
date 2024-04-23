import sys
import os


if sys.platform == 'win32':
    command = "python -m pip install -r requirements.txt"
else:
    command = "python3 -m pip install requirements.txt"
    
os.system(command)