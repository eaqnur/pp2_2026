#create folder
import os
os.mkdir("example_folder")
print("Folder created.")


#create nested directories
import os
os.makedirs("project/data/files", exist_ok=True)
print("Nested directories created.")

#view the list of files
import os
files=os.listdir()
print("Files and folders in current directory:")
for f in files:
    print(f)

#show current directory
print("Current directory:")
print(os.getcwd())

#find files by extension
import os
print("TXT files:")
for file in os.listdir():
    if file.endswith(".txt"):
        print(file)


#delete folder
import os
os.rmdir("example_folder")
print("Folder deleted.")

