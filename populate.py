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
              DNA_seq MEDIUMTEXT,
              gene_start INT,
              gene_end INT,
              CDS_start INT,
              CDS_end INT,
              CDS MEDIUMTEXT,
              protein_id VARCHAR(20),
              product VARCHAR(50),
              protein_seq MEDIUMTEXT)''')
    
    
read_entries = pd.read_csv (r'C:\Users\blito\Desktop\group_project\dummy_data.csv')
read_entries.to_sql('entries', conn, if_exists='replace', index = False) 

conn.commit()
conn.close()            
        