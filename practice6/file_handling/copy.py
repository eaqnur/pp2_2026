#delete a file
#remove the file "demofile.txt"
import os
os.remove("demofile.txt")


#check if file exists, then delete it
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")


#delete folder
import os
os.rmdir("myfolder")
#you can only remove empty folders

#shutil(copy)
import shutil
shutil.copy("file.txt", "copy.txt")

#create folder
import os
os.mkdir("folder")

#delete folder
os.rmdir("folder")
