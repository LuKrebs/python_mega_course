import os
import glob2

list_all_files = os.listdir()
# List all file inside of the directory
print(list_all_files)

# List all methods available on os module
print(dir(os))

# Find pattenrs in the files in this folder
print(glob2.glob("*.py"))
