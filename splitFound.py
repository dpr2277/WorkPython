import os
import re

dirPath = 'C:/Prudhvi/WorkPython/'
member = 'srchfname.out'
#
srchitem = 'Notfound'
#
file = open(os.path.normpath(dirPath + member))
for line in file:
        line = line.rstrip()
        if re.search(srchitem, line) :   
#            print line
            continue
        else:
            print line
#            continue
file.close()
    
exit()
                        
