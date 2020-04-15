import os
st="File Not Found"
def search(filename,dirname):
   pathf=[]
   #os.chdir(str(dirname))
   for root,dir,files in os.walk(dirname):

        print(" Printing the files : ",files)
        for inFile in files:
            if filename==inFile:
             pathf.append(os.path.join(root, filename))
             return pathf
             break
        for indir in dir:
            print("Entering this one ")
            if filename==indir:
                pathf.append(os.path.join(root,indir))
                return pathf
        for idir in dir:
            print("Printing the directory : ",idir)
            inDir=os.path.join(root,idir)
            inPath=search(filename,inDir)
            if(inPath!=0):
                return inPath
            else:
                return st

        
        
filename=input()
dirname=input()
print(search(filename,dirname))
