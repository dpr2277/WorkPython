########################################################
## Parses all JCL text files placed in a folder       ##
########################################################
import os
import re

dirPath = 'C:/UG/FindFileTypeComp/B1_Layered_Inventory/TYPRUN_SCAN_JCL/'
memberList = os.listdir((os.path.normpath(dirPath)))

#memberList =['P8IM1450.JCL']

for member in memberList:
    wsPGMfnd = []
    wsPGM = ''
    wsDDfnd = []
    wsDD = ''
    wsDSNfnd = []
    wsDSN = ''
    file = open(os.path.normpath(dirPath + member))
    for line in file:
        line = line.rstrip()
#
        if ('//*' == line[5:8]) or ('//' != line[5:7]):
            continue
#   
        wsPGMfnd = re.findall('PGM=[A-Z0-9]+',line)        
        if len(wsPGMfnd) > 0:
            wsPGM = ''.join(wsPGMfnd)
            continue
#   
        wsDDfnd = re.findall('//[A-Z0-9]+', line)
        if len(wsDDfnd) > 0:
            wsDD = ''.join(wsDDfnd)
#   
        wsDSNfnd = re.findall('DSN=[A-Z0-9.&()+-]+@*[A-Z0-9.&()+-]+', line)
        if len(wsDSNfnd) > 0:
            wsDSN = ''.join(wsDSNfnd)
            print '>>JCL>>' + member + '>>EXEC>>' + wsPGM + '>>DD>>' + wsDD[2:] + '>>' + wsDSN
            continue
    file.close()

exit()
                        
