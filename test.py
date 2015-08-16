import os

myfiles = 'C:/UG/FindFileTypeComp/myfiles.txt'
srchf = open(os.path.normpath(myfiles))
for li in srchf:
        print li
srchf.close()
exit()
