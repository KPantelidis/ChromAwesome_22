import sqlite3
from pandas import DataFrame
    
conn = sqlite3.connect("chromawesome.db")
c = conn.cursor()

#creating this list to create a dataframe and use it as keys for dictionaries later in APIs 
keys = ['accession','gene_id','location','DNA_seq',
               'gene_start','gene_end','CDS_start','CDS_end','CDS',
               'protein_id','product','protein_seq']
#create a dataframe    
c.execute("SELECT * FROM entries")
list_of_entries = list(c.fetchall())    
df = DataFrame(list_of_entries, columns=keys)


def test(a):
    '''
    gets user's input,
    searches if it is 'accession', 'gene_id', 'location' or 'protein_id',
    returns an error message if not,
    creates and returns a dictionary for each case
    
    :param a: search using accession, gene_id, location, protein_id 
    :returns: a dictionary with 
              keys: the column names
              values: the value for each column for the row that the parameter 'a' belongs to    
    '''
    
    #create lists that are needed to search where 'a' belongs to
    d1 = list(df['accession'])
    d2 = list(df['gene_id'])
    d3 = list(df['location'])
    d4 = list(df['protein_id'])
    
    #search cases
    if a in d1: #if 'a' is accession
        c.execute("SELECT * FROM entries WHERE accession = '%s' " %a)
        my_list = list(c.fetchone())
        dict1 = dict(zip(keys, my_list))
        print(dict1)
    elif a in d2: #if 'a' is gene_id
        c.execute("SELECT * FROM entries WHERE gene_id = '%s' " %a)
        my_list = list(c.fetchone())
        dict2 = dict(zip(keys, my_list))
        print(dict2)
    elif a in d3:  #if 'a' is location
        c.execute("SELECT * FROM entries WHERE location = '%s' " %a)
        my_list = list(c.fetchone())
        dict3 = dict(zip(keys, my_list))
        print(dict3)
    elif a in d4:  #if 'a' is protein_id
        c.execute("SELECT * FROM entries WHERE protein_id = '%s' " %a)
        my_list = list(c.fetchone())
        dict4 = dict(zip(keys, my_list))
        print(dict4)
    else:
        print("Please insert a valid 'accession', 'gene_id', 'location' or protein_id'")
        
        
        
    conn.commit()
    conn.close()