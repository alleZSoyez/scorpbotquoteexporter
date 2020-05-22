#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ScorpBot quote database output tool for cs188
# Written by Tate Frost / alleZSoyez

# setup
import sqlite3
from datetime import datetime
	
# replace this file path with your own, each \ must be escaped with another \ though or it won't work
print("Accessing database...")
quotedb = sqlite3.connect("C:\\Users\\Soyez\\Desktop\\QuotesDB.sqlite")

# init cursor 
c = quotedb.cursor()

# empty string for database output
quotetext = ''

# grab all quotes
c.execute("SELECT * FROM Quotes")

# grab quotes
print("Fetching quotes...")
quotetext = c.fetchall()
print("\n")

# create our output file
# once again, replace the file path with your own
textfile = open("C:\\Users\\Soyez\\Desktop\\quotedb.txt","w+",encoding="utf-8")

# empty string for output
quoteoutput = ""

# iterate through them
counter = 0

for q in quotetext:
	print(str(q).encode("unicode-escape"))
	counter+=1
	quoteoutput = str(quoteoutput) + "[" + str(counter) + "] " + str(q[1]) + "\n"
	
# write file
print("\nWriting to file...")

timestamp = datetime.now().strftime("%b %d, %Y AT %I:%M:%S %p %Z").upper()
textfile.write("CS188'S SCORPBOT QUOTE DATABASE, UPDATED AS OF "+timestamp+"\n\n")
textfile.write(quoteoutput)

# close file & database
print("Closing files...")
textfile.close()
c.close()
quotedb.close()

print("Finished!")
