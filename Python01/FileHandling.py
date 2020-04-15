import os
st="File Not Found"
def search(filename,dirname):
   pathf=[]
   for root,dir,files in os.walk(dirname):
        for inFile in files:
           if filename==inFile:
             pathf.append(os.path.join(root, filename))
             return pathf
        for idir in dir:
            inDir=os.path.join(root,idir)
            inPath=search(filename,inDir)
            if(inPath!=0):
                return inPath
            else:
                return st
        
filename=input()
dirname=input()
print(search(filename,dirname))
