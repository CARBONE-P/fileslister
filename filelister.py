import os.path,glob,shutil,os
from itertools import islice
listtype = []
x = 0
try:
   os.mkdir("filelister")
except:
   print("early good")
try:
   fnt = open("filelister/type","w")
   fnt.close()
except:
   print("early good")
with open("filelister/type") as f:
   lines = f.readlines()
while True:
   try:
    listtype.append(lines[x].translate({ord('\n'): None}))
    x=x+1
   except:
      break

for file in glob.glob("*.*"):
   extension = os.path.splitext(file)[1][1:]
   listtype_in_list = any(extension in listtype for string in listtype)
   filename = os.path.splitext(file)[0]
   new = str("filelister/") + (extension)
   if listtype_in_list == False:
      listtype.append(extension)
      filet = open("filelister/type", "a")  # append mode
      filet.write(extension + "\n")
      filet.close()
      filen = open(new,"w")
      filen.close()
   filex = open(new,"a")
   filex.write(filename + "\n")
   filex.close()
