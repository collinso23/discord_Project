import os
import sys
#'/home/user/example/parent/child'
CURRENT_PATH = os.path.abspath('.')

#'/home/user/example/parent'
PARENT_PATH = os.path.dirname(CURRENT_PATH)

sys.path.append(PARENT_PATH)
