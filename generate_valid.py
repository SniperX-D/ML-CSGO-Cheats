import os
from random import randrange

image_files = []
os.chdir(os.path.join("data", "obj"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpeg"):
        image_files.append("data/obj/" + filename)
os.chdir("..")
with open("valid.txt", "w") as outfile:
    for i in range(50):
        image = image_files[randrange(len(image_files))]
        outfile.write(image)
        outfile.write("\n")
        image_files.remove(image)
    outfile.close()
os.chdir("..")