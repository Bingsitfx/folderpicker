import os
import shutil
namafile = []
print("Program menghapus Folder dari kesamaan nama")
filePath = input("Nama directory file: ")
inputFolder = input("Directory folder dimana: ")
os.chdir(filePath)

for file in os.listdir():
    name, ext = os.path.splitext(file)
    namafile.append(name)

os.chdir(inputFolder)

if not os.path.exists("Folder pindahan"):
    os.mkdir("Folder pindahan")

for i in range(len(namafile)):
    for file in os.listdir():
        name, ext = os.path.splitext(file)
        if name == (namafile[i]):
            shutil.move(file, "Folder pindahan")
        else :
            continue
    i +=1
    