#create and write to a file
with open("students.txt", "w") as f:
    f.write("Alice 90\n")
    f.write("Bob 85\n")
    f.write("Charlie 95\n")
print("File created and data written.")


#read file contents
with open("students.txt", "r") as f:
    content=f.read()
print("file content:")
print(content)


#append new data to file
with open("students.txt", "a") as f:
    f.write("David 88\n")
    f.write("emma 92\n")
print("New lines added.")


#copy file
import shutil
shutil.copy("students.txt", "students_backup.txt")
print("Backup file created.")


#check
import os
import shutil
if os.path.exists("students.txt"):
    shutil.copy("students.txt", "students_backup.txt")
else:
    print("File not found")


#delete file
import os
if os.path.exists("students_backup.txt"):
    os.remove("students_backup.txt")
    print("Backup deleted")
else:
    print("Backup file not found")