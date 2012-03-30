import win32com.client as com

class Disk():
    def __init__(self, computer, disk):
        self.name = computer
        self.disk = disk
        self.drive = '\\\\' + computer + '\\' + disk

    def TotalSize(self):
        """ Return the TotalSize of a shared drive [GB]"""
        try:
            fso = com.Dispatch("Scripting.FileSystemObject")
            drv = fso.GetDrive(self.drive)
            return drv.TotalSize/2**30
        except:
            return 0
     
    def FreeSpace(self):
        """ Return the FreeSpace of a shared drive [GB]"""
        try:
            fso = com.Dispatch("Scripting.FileSystemObject")
            drv = fso.GetDrive(self.drive)
            return drv.FreeSpace/2**30
        except:
            return 0