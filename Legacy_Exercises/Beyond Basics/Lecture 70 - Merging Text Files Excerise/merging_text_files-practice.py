from datetime import datetime

myfiles = ["file1.txt","file2.txt","file3.txt"]

def concat_files(myfiles):
    dateformat = datetime.now()
    mydate = dateformat.strftime("%Y-%m-%d-%H-%M-%S-%f")
    with open(mydate+".txt", "w") as final_file:
        for i in myfiles:
            with open(i, "r") as f:
                output = f.read()
                final_file.write(str(output) +  "\n")

concat_files(myfiles)

print("----------------- Course solution --------------")

import glob2
filenames = glob2.glob("*.txt") # -> but is not completely right because glob2 orders list aleatory (unordered)
print(filenames)

with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + "-HEHE.txt", "w") as filewrite:
    for fff in filenames:
        with open(fff, "r") as fread:
            filewrite.write(fread.read() + "\n")
