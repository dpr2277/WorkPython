import os
import re

#dirPath = 'C:/UG/FindFileTypeComp/Listcat15Aug07/'
#memberList = os.listdir((os.path.normpath(dirPath)))
    
srchfname = 'C:/UG/FindFileTypeComp/myfiles.txt'
srchfiles = open(os.path.normpath(srchfname))
srchstr = []
for srchf in srchfiles:
    srchstr.append(srchfiles.next().rstrip())

#srchstr = ['IMP.DAY.IM1200AA.DCSCTFLO']
dirPath = 'C:/Prudhvi/WorkPython/'
memberList = ['extrjcl.out']
for srchitem in srchstr:
    itemfound = ''
    for member in memberList:
#        print member
        file = open(os.path.normpath(dirPath + member))
        for line in file:
            line = line.rstrip()
#            gotlist2 = re.findall(srchitem + '*[A-Z0-9.]*', line)
            if re.search(srchitem, line) :   
                print line
                itemfound = 'y'
        file.close()
    if itemfound == '':
        print 'Notfound>>%s' % srchitem
    
exit()
                        
