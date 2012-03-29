import win32com.client as com
 
def TotalSize(drive):
    """ Return the TotalSize of a shared drive [GB]"""
    try:
        fso = com.Dispatch("Scripting.FileSystemObject")
        drv = fso.GetDrive(drive)
        return drv.TotalSize/2**30
    except:
        return 0
 
def FreeSpace(drive):
    """ Return the FreeSpace of a shared drive [GB]"""
    try:
        fso = com.Dispatch("Scripting.FileSystemObject")
        drv = fso.GetDrive(drive)
        return drv.FreeSpace/2**30
    except:
        return 0
 
#workstations = ['DT-w7p-it2', 'srv-ws08-exact']
#print 'Hard drive sizes:'
#for compName in workstations:
#    drive = '\\\\' + compName + '\\d$'
#    print 'FreeSpace on %s = %f GB' % (drive, FreeSpace(drive))