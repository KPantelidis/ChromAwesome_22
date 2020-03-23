# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 19:30:33 2020

@author: blito
"""

def get_DNA_seq():
    '''
    returns a dictionary where "accession" is the key
            and "origin" (DNA_seq) is the value
    ----- uses the 'all_entries()' function-----
    '''
    x = all_entries()
    y = list(zip(*x))
    d = {y[0][i] : y[3][i] for i, _ in enumerate(y[3])}
    return d