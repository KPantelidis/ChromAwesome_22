def return_column(name):

    ''' takes a column name and will return all data for that column.
    Returns a list of entries for that column.

    :param name: name of a column in SQL table
    returns: a list of column entries '''

    import pymysql
    import pymysql.cursors

    config_dict = {'host' :'hope',
               'user' : 'pk001',  
               'password'   : 'wbjcod3k6',   
               'port'     : 3306}

    conn = pymysql.connect(**config_dict)

    c = conn.cursor()

    if name == 'accession':
        c.execute("SELECT accession FROM pk001.entries")
    elif name == 'gene_id':
        c.execute("SELECT gene_id FROM pk001.entries")
    elif name == 'location':
        c.execute("SELECT location FROM pk001.entries")
    elif name == 'protein_id':
        c.execute("SELECT protein_id FROM pk001.entries")
    else:
        print('return_column function error: invalid column name')

    entries_list = list(c.fetchall())
    return entries_list

