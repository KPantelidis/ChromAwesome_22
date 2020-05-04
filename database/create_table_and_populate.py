import pymysql
import pymysql.cursors
from parser import list_of_entries

# Set parameters

config_dict = {'host' :'hope',
               'user' : 'pk001',  
               'password'   : 'xxx',   
               'port'     : 3306}

# Connect to the database

conn = pymysql.connect(**config_dict)

c = conn.cursor()
try:
    c.execute("CREATE TABLE pk001.entries \
            (accession VARCHAR(10),\
            gene_bp INT,\
            gene_id TEXT(1000),\
            location VARCHAR(100),\
              dna_seq MEDIUMTEXT,\
              cds MEDIUMTEXT,\
              complement VARCHAR(10),\
              protein_id VARCHAR(100),\
              product VARCHAR(100),\
              translation MEDIUMTEXT) ENGINE=InnoDB")
    conn.commit
    
except:
    c.execute("DROP TABLE pk001.entries")
    c.execute("CREATE TABLE pk001.entries \
            (accession VARCHAR(10),\
            gene_bp INT,\
            gene_id TEXT(1000),\
            location VARCHAR(100),\
              dna_seq MEDIUMTEXT,\
              cds MEDIUMTEXT,\
              complement VARCHAR(10),\
              protein_id VARCHAR(100),\
              product VARCHAR(100),\
              translation MEDIUMTEXT) ENGINE=InnoDB")

query = "INSERT INTO pk001.entries VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
c.executemany(query,list_of_entries)
conn.commit
print("Table 'entries' created and data inserted succesfully")

conn.commit()
conn.close()           
