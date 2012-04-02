# main.py
# Import smtplib for the actual sending function
import smtplib
from diskFree import Disk
# Import the email modules we'll need
from email.mime.text import MIMEText

workstations = []
warnings = []

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
		print "Freespace on %s\\%s: %i GB" % (computer.name, computer.disk, computer.FreeSpace())

		if computer.FreeSpace() < 150 and computer.disk == "d$":
			warnings.append(computer)

for computer in warnings:
	print ""
	print "****** Warning *******"
	print "Space on these drive(s) is getting low:"
	print computer.drive