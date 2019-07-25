import sys
import os
path = "l:\handbrake movies"
# for root, dirs, files in os.walk("\\", topdown=True):
# #    for name in files:
# #       print(os.path.join(root, name))
#     for name in dirs:
#       print(os.path.join(root, ""))
dirlist = (os.listdir(path))
# for file in dirlist:
#     print(file)
print(len(dirlist))
print((dirlist))

# Retrieve maximum length of a filename
print(os.get_exec_path())
