# main.py

from diskFree import Disk

workstations = []

# Edit this text file to change the server names.
f = open('../servers.txt', 'r')
for line in f.readlines():
	workstations.append(line.rstrip())

# Which drives shuld we check?
drive = ['c$','d$']

print 'Hard drive sizes:'
for compName in workstations:
	for disk in drive:
		computer = Disk(compName, disk)
		print 'Freespace on %s\%s: %i GB' % (computer.name, computer.drive,  computer.FreeSpace())