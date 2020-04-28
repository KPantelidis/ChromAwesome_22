# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:54:06 2020

@author: blito
"""

import sqlite3

conn = sqlite3.connect("chromawesome.db")
c = conn.cursor()

entries = bla()   
#print(entries) 
for entry in entries:
    c.execute('''INSERT INTO entries VALUES''' + str(entry))

conn.commit()
conn.close() 

