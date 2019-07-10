import os
import sys

current_path = os.path.abspath('.')

parent_path = os.path.dirname(current_path)

sys.path.insert(0, parent_path)
