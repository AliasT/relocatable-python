import sys
import os
import subprocess

import shutil
print(os.getcwd())
print(sys.executable)

# For windows
executable_path = os.path.dirname(sys.executable)
requirements_path = os.path.join(os.getcwd(), "requirements.txt")
cmd = [executable_path, "-s", "-m", "pip", "install", "-r", requirements_path]

print("Installing modules from %s..." % requirements_path)

subprocess.check_call(cmd)

shutil.make_archive("python3win", 'zip', executable_path)
