# Walk the directory
import os
path = "l:/Downloads/Python"
i = 0
for dirpath, dirnames, filenames in os.walk(path,  topdown=False):
    print(dirpath, dirnames, filenames)
for file in filenames:
	if ".mp4" in file:
		print (file)
i += 1
print(filenames)

import os
for dirpath, dirs, files in os.walk("\\"):
	path = dirpath.split('\\')
	print ('|', (len(path))*'---', '[', os.path.basename(dirpath), ']')
	# for i,f in enumerate(files, start=1):
	# 	print (f"| {len(path)*'   '} {i} {os.path.join(dirpath,f)}")

	for  f in (files):
		print(f"| {len(path)*'   '}  {os.path.join(dirpath,f)}")

