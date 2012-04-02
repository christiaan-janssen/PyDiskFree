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

if warnings != []:
	# Create a text/plain message
	msg = MIMEText("Disk Space Low on:\n\n")

	# me == the sender's email address
	# you == the recipient's email address
	msg['Subject'] = 'Disk Space Low '
	msg['From'] = 'mailadress'
	msg['To'] = 'mailadress'
	mail = msg.as_string()

	for computer in warnings:
		mail += computer.drive + "\n"

	s = smtplib.SMTP('MailServer')
	s.sendmail('mail_from', 'mail_to', mail)
	s.quit()
