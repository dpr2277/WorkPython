########################################################
## Parses all COBOL source files placed in a folder   ##
########################################################
import os
import re

dirPath = 'C:/UG/FindFileTypeComp/B1_Layered_Inventory/cbl/'
memberList = os.listdir((os.path.normpath(dirPath)))

#memberList =['PRUDHVI0.cbl']

for member in memberList:
    print member
    wsDatDivfnd = ''
    wsProDivfnd = ''
    wsPGM = ''
    wsCPYfnd = []
    wsCPYs = []
    wsREADfnd = []
    wsCALLfnd = []
    wsSELfnd = []
    file = open(os.path.normpath(dirPath + member))
    for line in file:
        try:
    #        print len(line), line.split()
            newline = ''
            if len(line) < 7:
                continue
            line = line[6:72]
            if line[0] == '*':
                continue
            if not re.search('.[^ ]+', line):
                continue
            if line[:15] == ' DATA DIVISION.':
                wsDatDivfnd ='y'
                continue
            if line[:20] == ' PROCEDURE DIVISION.':
                wsProDivfnd = 'y'
                continue
    #
            if wsDatDivfnd != 'y' and re.search(' SELECT +[A-Z0-9-]* *', line):
                if re.search('.*[.]', line):
                    newline += line.strip()[:len(line.strip()) - 1] + ' '
                else:
                    while True:
                        newline += line.strip() + ' '
                        line = file.next()
                        line = line[6:72]
                        if re.search('.*[.]', line):
                            newline += line.strip()[:len(line.strip()) - 1] + ' '
                            break
                if newline.split()[3] == 'TO':
                    wsSELfnd.append(newline.split()[1] + '==' + newline.split()[4])
                else:
                    wsSELfnd.append(newline.split()[1] + '==' + newline.split()[3])
                continue
    #
            if wsProDivfnd != 'y' and re.search(' +COPY +[A-Z0-9]+', line):
                wsCPYs.append(line.split()[1])
                continue
    #
            if wsProDivfnd == 'y' and re.search(' +READ +[A-Z0-9-]+', line):
                for item in line.split():
                    if line.split()[item] == 'INTO':
                        wsREADfnd.append(line.split()[1] + '==' + line.split()[item + 1])
    #
            if wsProDivfnd == 'y' and re.search(' +CALL +[A-Z0-9\']+', line):
                wsCALLfnd.append(line.split()[1])
        except Exception as e:
            print 'Error: ' + member + ': Llen: ' + str(len(line)) + ': ' + line
            continue
#
    print member[:8] + '>>' + 'FILESELECT>>' + '>>'.join(wsSELfnd)
    print member[:8] + '>>' + 'COPY>>' + '>>'.join(wsCPYs)
    print member[:8] + '>>' + 'READFILE>>' + '>>'.join(wsREADfnd)
    print member[:8] + '>>' + 'PGMCALLS>>' + '>>'.join(wsCALLfnd)
    file.close()
    
##        if re.search('^ FD', line):
##            print member[:8] + '>>' + line
#            print line
#
##        if wsProDivfnd == 'y' and re.search(' +WRITE +[A-Z0-9-]+', line):
##            print line

exit()
