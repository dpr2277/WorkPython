########################################################
## Parses all JCL text files placed in a folder       ##
########################################################
import os
import re

dirPath = 'C:/UG/FindFileTypeComp/B1_Layered_Inventory/TYPRUN_SCAN_JCL/'
memberList = os.listdir((os.path.normpath(dirPath)))

memberList =['PDIM1210.JCL']

for member in memberList:
    wsPGMfnd = []
    wsPGM = ''
    wsDDfnd = []
    wsDD = ''
    wsDSNfnd = []
    wsDSN = ''
    wsDB2PGM = ''
    wsSTEP = ''
    wsSTEPDDs = dict()
    file = open(os.path.normpath(dirPath + member))
    for line in file:
        line = line.rstrip()
#
        if ('//*' == line[5:8]) or ('//' != line[5:7]):
            continue
#   
        wsPGMfnd = re.findall('PGM=[A-Z0-9]+',line)        
        if len(wsPGMfnd) > 0:
            wsDDKeyList = wsSTEPDDs.keys()
            for wsDDKey in wsDDKeyList:
                wsDSNList = wsSTEPDDs[wsDDKey]
                for wsDSNitem in wsDSNList:
                    print '>>JCL>>' + member + '>>STEP>>' + wsSTEP +'>>EXEC>>' + wsPGM + '>>DB2PGM>>' + wsDB2PGM + '>>DD>>' + wsDDKey[2:] + '>>' + wsDSNitem
#
            wsSTEPDDs.clear()
            wsDB2PGM = ''
#
            wsSTEP = line[7:15]
            wsPGM = ''.join(wsPGMfnd)
            continue
#   
        wsDDfnd = re.findall('//[A-Z0-9]+', line)
        if len(wsDDfnd) > 0:
            wsDD = ''.join(wsDDfnd)
#   
        wsDSNfnd = re.findall('DSN=[A-Z0-9.&()+-]+@*[A-Z0-9.&()+-]+', line)
        if len(wsDSNfnd) > 0:
            if wsSTEPDDs.has_key(wsDD):
                wsDSN = ''.join(wsDSNfnd)
                wsSTEPDDs[wsDD].append(wsDSN)
            else:
                wsSTEPDDs[wsDD] = wsDSNfnd
#
        if (wsPGM == 'PGM=IKJEFT1B' and wsDD == '//SYSTSIN'):
            wsDB2fnd = re.findall('([A-Z0-9.]+)', wsDSN)
            if len(wsDB2fnd) > 0:
                wsDB2PGM = wsDB2fnd[2]
#
#        print '>>JCL>>' + member + '>>STEP>>' + wsSTEP +'>>EXEC>>' + wsPGM + '>>DB2PGM>>' + wsDB2PGM + '>>DD>>' + wsDD[2:] + '>>' + wsDSN
        continue
    file.close()

exit()
                        
