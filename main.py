# main.py

from diskFree import Disk

workstations = ['DT-W7P-IT2', 'DT-W7P-IT1']
drive = ['c$','d$']
print 'Hard drive sizes:'
for compName in workstations:
	for disk in drive:
		computer = Disk(compName, disk)
		print 'Freespace on %s\%s: %i GB' % (computer.name, computer.drive,  computer.FreeSpace())