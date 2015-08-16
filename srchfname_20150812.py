import os
import re

#dirPath = 'C:/UG/FindFileTypeComp/Listcat15Aug07/'
#memberList = os.listdir((os.path.normpath(dirPath)))
    
srchfname = 'C:/UG/FindFileTypeComp/myfiles.txt'
srchfiles = open(os.path.normpath(srchfname))
srchstr = []
for srchf in srchfiles:
    srchstr.append(srchfiles.next().rstrip())

extrFile = 'C:/Prudhvi/WorkPython/extrjcl.out'
#srchstr = ['IMP.DAY.IM1200AA.DCSCTFLO']
#
file = open(os.path.normpath(extrFile))
for srchitem in srchstr:
    gotlist = []
#
    for line in file:
        line = line.rstrip()
        if re.search(srchitem + '[A-Z0-9.]*', line):
            gotlist.append(srchitem + line)
#
    if len(gotlist) > 0:
        print '\n'.join(gotlist)
#        print 'total: ', len(gotlist)
    else:
        print 'Notfound>>%s' % srchitem
    file.seek(0, 0)
#
file.close()
exit()
                        
