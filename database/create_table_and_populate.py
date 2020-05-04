# -*- coding: utf-8 -*-
"""
Last update Mon May 4 2020
Created for Group Project
BBK UNI/Biocomputing II

@author: Kostas Pantelidis
"""

import pymysql
import pymysql.cursors
from parser import list_of_entries

# Set parameters

config_dict = {'host' :'hope',
               'user' : 'pk001',  
               'password'   : 'wbjcod3k6',   
               'port'     : 3306}

# Connect to the database

conn = pymysql.connect(**config_dict)
c = conn.cursor()

#try to create table "entries", if exists then drops table and create it
try:
    c.execute("CREATE TABLE pk001.entries \
            (accession VARCHAR(10) NOT NULL,\
             gene_bp INT NOT NULL,\
             gene_id TEXT(1000) NOT NULL,\
             location VARCHAR(100) NOT NULL,\
             dna_seq MEDIUMTEXT NOT NULL,\
             cds MEDIUMTEXT NOT NULL,\
             complement VARCHAR(10) NOT NULL,\
             protein_id VARCHAR(100) NOT NULL,\
             product VARCHAR(100) NOT NULL,\
             translation MEDIUMTEXT NOT NULL)\
             ENGINE=InnoDB")
    
except:
    c.execute("DROP TABLE pk001.entries")
    c.execute("CREATE TABLE pk001.entries \
            (accession VARCHAR(10) NOT NULL,\
             gene_bp INT NOT NULL,\
             gene_id TEXT(1000) NOT NULL,\
             location VARCHAR(100) NOT NULL,\
             dna_seq MEDIUMTEXT NOT NULL,\
             cds MEDIUMTEXT NOT NULL,\
             complement VARCHAR(10) NOT NULL,\
             protein_id VARCHAR(100) NOT NULL,\
             product VARCHAR(100) NOT NULL,\
             translation MEDIUMTEXT NOT NULL)\
             ENGINE=InnoDB")


#populate the database using "list_of_entries" from parser.py file
    
query = "INSERT INTO pk001.entries VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
c.executemany(query,list_of_entries)
print("Table 'entries' created and data inserted succesfully")

conn.commit()
conn.close()           
