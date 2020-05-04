# -*- coding: utf-8 -*-
"""
Last update Mon May 4 2020
Created for Group Project
BBK UNI/Biocomputing II

@author: Kostas Pantelidis
"""

import gzip
import re

# I will use a for loop to search every entry of the chromosome individually,
#so i', spliting the chromosome after every entry (//) and put the
#entries in a list

my_list = []
with gzip.open('chrom_CDS_22.gz', mode="rt") as f:
    reader = f.read()
    my_list = reader.split("//\n")

#i'm searching for 10 different pieces of data from GenBank file
#and these are the lists i'll need later
    
accession_list = []
gene_id_list = []
gene_bp_list = []
location_list = []
dna_list =[]
cds_list = []
complement_list = []
protein_id_list = []
product_list = []
translation_list = []

for i in my_list:    

    #-----------accession----------------
    p1 = re.compile(r'ACCESSION \s+\w+\s')
    p1 = p1.findall(i)
    p1 = [i.replace('ACCESSION', '').strip() for i in p1]
    accession_list += p1
    #accession is unique per entry, no need to check for duplicates


    #----------gene_bp------------------
    gene_bp = []
    p2 = re.compile(r'(\bLOCUS)\s+(\w+)\s+(\d+)\s+')
    it = p2.finditer(i)
    for match in it:
        gene_bp.append(match.group(3))
    gene_bp_list += gene_bp
    #no need to check for duplicates, i take it from LOCUS line which is unique per entry

    #-----------gene_id-------------------
    p3 = re.compile(r'/gene=".+?"\s+')
    if p3.search(i):
        p3 = p3.findall(i)
        p3 = [i.replace('/gene="', '').replace('"', '').strip() for i in p3] 
        p3 = list(dict.fromkeys(p3)) #for duplicates
        gene_id_list.append(p3[0])
    else:
        gene_id_list.append('None') #put 'None' in case cannot find a gene_id
       

    #-----------location-------------------
    p4 = re.compile(r'/map=".+?"\s+')
    if p4.search(i):
        p4 = p4.findall(i)
        p4 = [i.replace('/map="', '').replace('"', '').strip() for i in p4] 
        p4 = list(dict.fromkeys(p4)) #for duplicates
        location_list.append(p4[0])
    else:
        location_list.append('None') #put 'None' in case cannot find a location


    #---------dna_sequence--------- 
    dna = []
    p5 = re.compile(r'(ORIGIN\s+)((.*\n){1,})')
    it = p5.finditer(i)
    for match in it:
        dna.append(match.group(2))
        dna = [i.replace('\n', '').replace(' ', '').strip() for i in dna]
        dna = [re.sub('[0-9]', '', i) for i in dna] 
    dna_list += dna
    #no need for 'None', there's always dna_seq(ORIGIN)
    # no need to check for duplicates, there's only one origin per entry

    
    #---------------CDS--------------------
    p6 = re.compile(r'CDS\s*(.[^\/]*?)\/')
    if p6.search(i):
        p6 = p6.findall(i)
        p6 = [i.replace('\n', '')
                .replace(' ', '')
                .replace('join', '')
                .replace('complement','')
                .strip() for i in p6]
        cds_list.append(p6[0])
    else:
        cds_list.append('None') #put 'None' in case cannot find a CDS
        

    #-----------protein_id-------------------
    p8 = re.compile(r'/protein_id=".+?"\s+')
    if p8.search(i):
        p8 = p8.findall(i)
        p8 = [i.replace('/protein_id="', '').replace('"', '').strip() for i in p8] 
        p8 = list(dict.fromkeys(p8)) #for duplicates
        protein_id_list.append(p8[0])
    else:
        protein_id_list.append('None')  #put 'None' in case cannot find a protein_id
        

    #-----------product-------------------
    p9 = re.compile(r'/product=".+?"\s+')
    if p9.search(i):
        p9 = p9.findall(i)
        p9 = [i.replace('/product="', '').replace('"', '').strip() for i in p9] 
        p9 = list(dict.fromkeys(p9)) #for duplicates
        product_list.append(p9[0])
    else:
        product_list.append('None')   #put 'None' in case cannot find a product
       

    #-----------translation----------------    
    p10 = re.compile(r'/translation="(.[^"]*?)"\s')
    if p10.search(i):
        p10=p10.findall(i)
        p10 = [i.replace('\n', '').replace(' ','').strip() for i in p10]
        p10 = list(dict.fromkeys(p10)) #for duplicates
        translation_list.append(p10[0]) 
    else:
        translation_list.append('None') #put 'None' in case cannot find a translation
        

#--------complement-------------------------
        #i couldn't work out the complement inside the big for (in my_list)
        # so i'm using a for loop for complement seperately
temp = []
for i in my_list:
    p8 = re.compile(r'CDS\s*(.[^\/]*?)\/')
    if p8.search(i):
        p8 = p8.findall(i)
        temp.append(p8[0])
for i in temp:
    p = re.compile(r'complement')
    if p.search(i):
        p = p.findall(i)
        complement_list.append('COMPLEMENT')
    else:
        complement_list.append('NO')
       

#make a list of lists, putting all the lists i found earlier
#i'm importing "list_of_entries" in "create_table_and_populate"
#to populate my database
        
list_of_entries = []
list_of_entries = list(zip(accession_list,
                               gene_bp_list,
                               gene_id_list,
                               location_list,
                               dna_list,
                               cds_list,
                               complement_list,
                               protein_id_list,
                               product_list,
                               translation_list
                               ))
