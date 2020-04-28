import sqlite3
import pandas as pd
from pandas import DataFrame
    
conn = sqlite3.connect("chromawesome.db")
c = conn.cursor()

#you have to use this if you want to re-run the script after the very first time you run it, 
c.execute("DROP TABLE entries")

c.execute('''CREATE TABLE entries
              (accession VARCHAR(10), 
              gene_id VARCHAR(10), 
              location VARCHAR(10),
              dna_seq MEDIUMTEXT,
              gene_bp INT,
              protein_id VARCHAR(20),
              product VARCHAR(50),
              translation MEDIUMTEXT)''')


conn.commit()
conn.close()            
