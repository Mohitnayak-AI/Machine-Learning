import os
import sys

# get the absolute path of the project root dict
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))

print("project root: ", project_root)

sys.path.insert(0,project_root)


# we use this to add the root path for the test so it can access the src folder