# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:53:17 2020

@author: blito
"""

def get_data(a,b):
    '''
    returns a dictionary where "accession" is always the key
            and the user chooses a column from the sql table as the value
    a: the key in the dictionary
    b:  1: gene
        2: location
        3: origin
        4: CDS_start
        5: CDS_end
        6: CDS
        7: protein_ID
        8: product
        9: translation
    '''
    x = all_entries()
    y = list(zip(*x))
    d = {y[a][i] : y[b][i] for i, _ in enumerate(y[4])}
    return d