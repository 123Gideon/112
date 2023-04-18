import os
import shutil

from_dir=r"C:\Users\17034\Pictures\myimages"
to_dir=r"C:\Users\17034\Pictures\Saved Pictures"

list_of_files=os.listdir(from_dir)
# print(list_of_files)

for i in list_of_files:
    name,extension=os.path.splitext(i)
    print(extension)
    if(extension==""):
        continue
    if extension in [ ".txt", ".doc", ".docx", ".pdf",".jpg",".gif",".png"]:
        path1=from_dir+"/"+i
        path2=to_dir + '/' + "Document_Files"
        path3=to_dir + '/' + "Document_Files" + '/' +i

        if os.path.exists(path2):
            print("moving "+i+".......")

            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving "+i+"......")
            shutil.move(path1,path3)        
        