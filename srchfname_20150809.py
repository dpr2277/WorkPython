import os
import re

#dirPath = 'C:/UG/FindFileTypeComp/Listcat15Aug07/'
#memberList = os.listdir((os.path.normpath(dirPath)))
    
srchfname = 'C:/UG/FindFileTypeComp/myfiles.txt'
srchfiles = open(os.path.normpath(srchfname))
srchstr = []
for srchf in srchfiles:
    srchstr.append(srchfiles.next().rstrip())

dirPath = 'C:/Prudhvi/WorkPython/'
memberList = ['extrjcl.out']
#srchstr = ['IMP.DAY.IM1200AA.DCSCTFLO']

for srchitem in srchstr:
    gotlist = []
    for member in memberList:
#        print member
        file = open(os.path.normpath(dirPath + member))
        for line in file:
            line = line.rstrip()
#            gotlist1 = re.findall(srchitem, line)
            gotlist2 = re.findall(srchitem + '*[A-Z0-9.]*', line)
            if len(gotlist2) == 0:
                continue
            else:
#                gotlist.extend(gotlist1)
                gotlist.extend(gotlist2)
        file.close()
    if len(gotlist) > 0:
        print '\n'.join(gotlist)
        print 'total: ', len(gotlist)
    else:
        print 'Notfound>>%s' % srchitem
    
exit()
                        
