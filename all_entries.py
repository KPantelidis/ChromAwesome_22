# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 19:23:03 2020

@author: blito
"""

def all_entries():
    '''
    creates an sql table that has 10 columns
    (accession, gene, location, origin, CDS_start, CDS_end, CDS, 
    protein, product, translation)
    
    ----- at the moment it gets 3 entries (3 genes), 
          some dummy data is expected --------------
    
    returns a list of all entries from the GenBank file
    '''
    
    import sqlite3
    conn = sqlite3.connect("chromawesome.db")
    c = conn.cursor()
    c.execute("DROP TABLE test1")

    c.execute('''CREATE TABLE test1
              (accession INT, 
              gene INT, 
              location INT, 
              origin INT,
              CDS_start INT,
              CDS_end INT,
              CDS INT,
              protein_ID INT,
              product INT,
              translation INT)''')
    
    rows = [(1,2,3,4,5,6,7,8,9,10),
            (11,12,13,14,15,16,17,18,19,20),
            (21,22,23,24,25,26,27,28,29,30)]
    
    c.executemany('INSERT INTO test1 VALUES (?,?,?,?,?,?,?,?,?,?)', rows)
    
    c.execute("SELECT * FROM test1")
    list_of_entries = list(c.fetchall())
    
    conn.commit()
    conn.close()
    
    return(list_of_entries)