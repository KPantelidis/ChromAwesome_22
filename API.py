def dict_entries(a):
    '''
    gets user's input,
    searches if it is 'accession', 'gene_id', 'location' or 'protein_id',
    tries to populate a list if it has matched a search,
    returns False if not,
    creates and returns a dictionary 
    
    :param a: search using accession, gene_id, location, protein_id 
    :returns: a dictionary with 
              keys: the column names
              values: the value for each column for the row that the parameter 'a' belongs to    
    '''
    
    import sqlite3   
    conn = sqlite3.connect("chromawesome.db")
    c = conn.cursor()

    keys = ['accession','gene_id','location','DNA_seq',
            'gene_start','gene_end','CDS_start','CDS_end','CDS',
            'protein_id','product','protein_seq']
    
    c.execute("SELECT * FROM entries WHERE \
                accession = '%s' OR \
                gene_id = '%s' OR \
                location = '%s' OR \
                protein_id = '%s' " %(a,a,a,a)) 
    
    try:
        my_list = list(c.fetchone())  #'try' to populate the list if it has matched a search value. 
                                        #If no match the 'except' will return False. 
    except:
        return False
    
    return_dict = dict(zip(keys, my_list))  #If try is successful, populates a dictionary
    return return_dict                      #and returns the dictionary to user. 
      
    conn.commit()
    conn.close()
