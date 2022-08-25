import os
import shutil

# for subdir, dirs, files in os.walk(os.getcwd()):
    # for filename in files:
    #     # filepath = dirs + os.sep + filename
    #     print (dirs)
    #     for f in files: print (os.path.abspath(f))
    #     if filename.endswith(".html") or filename.endswith(".docx"):
    #         # print (os.path.abspath(filename))
    #         # print (str(Path(filename).resolve()))
    #         # print (filename)
    #         pass

dest=os.path.join(os.getcwd(),"combined")
if not os.path.isdir(dest):
            os.makedirs(dest)
            
for dirpath,_,filenames in os.walk(os.getcwd()):
       for f in filenames:
           if not f.endswith(".py"):
               print(os.path.join(dirpath,f))
               newfn=os.path.split(dirpath)[1].split("_")[0]+"_"+f
               print(newfn)
               newdest=os.path.join(dest,newfn)
               shutil.copyfile(os.path.join(dirpath,f),newdest)

