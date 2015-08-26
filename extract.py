## This is a test for Git
## This is a test for Git from home
import os

dirPath = 'C:/UG/FindFileTypeComp/B1_Layered_Inventory/TYPRUN_SCAN_JCL/'
memberList = os.listdir((os.path.normpath(dirPath)))

stepRec = ''
EXECpgm = ''
PGMpos = 0
DSNnam = ''
DSNpos = 0

##for member in memberList:
member = 'PDIM1200.JCL'
fi = open(os.path.normpath(dirPath + member))
for line in fi:
    gline = line.rstrip()
    if ('//*' == gline[5:8]) or ('//' != gline[5:7]):
        continue
    else:
        PGMpos = gline.find('EXEC PGM=')
        if PGMpos > 0:
            EXECpgm = gline[PGMpos + 9:PGMpos + 9 + 8]
            
        DSNpos = gline.find('DSN=')
        if DSNpos > 0:
            DSNnam = gline[DSNpos + 4:77]

        stepRec = '>>EXEC>>'+EXECpgm+'>>DSN='+DSNnam
        print stepRec
        stepRec = ''

fi.close()

##for srchitem in srchstr:
##    for member in memberList:
##        file = open(os.path.normpath(dirPath + member))
##        for line in file:
##            if '//*' not in line[4:3]
##                PGMpos = line.find('PGM=')
##                PGMname = line[PGMpos + 4:8]
##                if srchitem in line.rstrip()
##                    print 'File::' + srchitem + 'Member::' + fname
                        
