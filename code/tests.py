import os

path = r"F:\images\001"
for root ,dirs ,files in os.walk(path) :
	print(root)
	print(dirs)
	print(files)
