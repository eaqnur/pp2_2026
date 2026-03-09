#moving a file
import shutil
shutil.move("../file_handling/students.txt", "students.txt")
print("file moved.")

#copying a file
import shutil
shutil.copy("students.txt", "students_copy.txt")
print("File copied.")