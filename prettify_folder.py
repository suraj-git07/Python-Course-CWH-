import os

def soldier(path,direc_file,format):
    os.chdir(path)
    total_files=os.listdir()

    format_file=[]
    with open(direc_file) as f:    #removing files that are requested not to touch
        critical_files=f.read().split("\n")
        for i in critical_files:
           total_files.remove(i)

    for j in total_files:           # removing folders
        if "." in j:
            pass
        else:
            total_files.remove(j)
    # print(total_files)           #now it only had specific files that include "."
    for l in total_files:
        if f".{format}" in l:
            ind=total_files.index(l)
            x=total_files.pop(ind)
            format_file.append(x)   #format files
        else:
            pass

    #now formatting
    for k in total_files:
        os.rename(k,k.capitalize())

    # print(total_files)
    #formatting for format_files
    for pos,m in  enumerate(format_file):

         new=f"{pos+1}.{format}"
         os.rename(m,new)





if __name__=="__main__":
    path=input("enter the path of your folder")
    direc_file=input("enter the name of direc file")
    format=input("enter the format")

    soldier(path,direc_file, format)