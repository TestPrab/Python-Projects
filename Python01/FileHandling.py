import os
def search(filename,dirname):
   pathf=[]
   for root,dir,files in os.walk(dirname):
       if filename in files:
           pathf.append(os.path.join(root, filename))
           return pathf
print("Enter the filename and the directory")
filename=input()
dirname=input()
print(search(filename,dirname))
