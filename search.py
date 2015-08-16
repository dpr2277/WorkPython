import os

srchfname = 'C:/UG/FindFileTypeComp/myfiles_blanks.txt'
srchfiles = open(os.path.normpath(srchfname))
##srchstr = []
##for srchf in srchfiles:
##    srchstr.append(srchfiles.next())

i = 0
j = 0
for srchitem in srchfiles:
    if srchitem[2:3] == 'Q':
        print srchitem[0:2] + 'P' + srchitem[3:].rstrip()
        i = i + 1
    else:
        print srchitem.rstrip()
        j = j + 1
                        
srchfiles.close()
#print 'Total Q to P updated: ', i
#print 'Total Q not found   : ', j
exit()
