import sys
import os

import shutil


executable_path = os.path.dirname(sys.executable)

shutil.make_archive("python3win", 'zip', executable_path)
