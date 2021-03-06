
#Last updated Tues May 5 2020
#The function of this code is to allow the Front End to remove raw data from the database
#and call functions that will perform manipulations on the data from the DB.
#author: Annabel Page

import dbapi
import dbapi_column
from Bio import Restriction
from Bio.Seq import Seq
from Bio.Alphabet.IUPAC import IUPACAmbiguousDNA
from Bio.Alphabet import IUPAC
import re
import pymysql
import pymysql.cursors

#Create function that will store user input search query and search the database for
#specfic row of data

def search_db(Search_Query):
   
    
    Database_Result = dbapi.dict_entries(Search_Query)
    return(Database_Result)
   

#create function returning cleaned up columns from the DB layer for either location, gene_id, accession or protein_id
def column_list(name):
   
    infolist = list(dbapi_column.return_column(name))
    newlist = []
    for elem in infolist:
      if elem not in newlist:
        newlist.append(elem)
    #change from list of tuples to list    
    endlist = [a for b in newlist for a in b] 
    remove = ['None']
    for elem in list(endlist):
      if elem in remove:
        endlist.remove(elem)
    return(endlist)


## Create a function to identify RE enzyme sites in the DNA sequence
def search_RE(Search_Query, RE_name):
    
    amb = IUPACAmbiguousDNA()
    Database_Result = dbapi.dict_entries(Search_Query)
    if Database_Result == False:
      return('Please enter valid search value for either accession, location, gene_id or protein_id')
    DNA_seq = Database_Result['dna_seq']
    DNASeq = Seq(DNA_seq, amb)

    if RE_name == 'EcoRI':
        EcoRI = Restriction.EcoRI.search(DNASeq)
        if EcoRI == []:
            print('There are no EcoRI restriction sites in this DNA sequence')
        else:
            return 'The location sites for EcoRI are', EcoRI
    elif RE_name == 'BamHI':
        BamHI = Restriction.BamHI.search(DNASeq)
        if BamHI == []:
                print('There are no BamHI restriction sites in this DNA sequence')
        else:
            return 'The location sites for BamHI are', BamHI
    elif RE_name == 'BsuRI':
        BsuRI = Restriction.BsuRI.search(DNASeq)
        if BsuRI == []:
                print('There are no BsuRI restriction sites in this DNA sequence')
        else:
            return 'The location sites for BsuRI are', BsuRI
    else:
        print('search_RE function error: invalid RE name')



#create a function to mark up the CDS regions on the gene DNA seq
def CDS_markup(Search_Query):
    #Take the search term and search database for corresponding information
    Database_Result = dbapi.dict_entries(Search_Query)
    if Database_Result == False:
      print('Please enter valid search value for either accession, location, gene_id or protein_id')
    
    p = re.compile(r'(\d+)..(\d+),?')
    CDS = Database_Result['cds']
    it = p.finditer(CDS)
    
    start_end_list = [(int(match.group(1)),int(match.group(2))) for match in it]
    DNA_seq = Database_Result['dna_seq']

    #Mark up the sequence with < > to locate start and end of CDS regions
    DNA_list = list(DNA_seq)
    offset = 0

    for start,end in start_end_list:
        DNA_list.insert((start-1)+offset, "<")
        offset += 1
        DNA_list.insert((end-1) +offset, ">")
        offset += 1

    DNA_str = ""
    for elem in DNA_list:
        DNA_str += elem
    return(DNA_str)


#return a list of all the coding DNA regions without the mark ups
def CDS_DNA(Search_Query):
    
    CDS_Data = CDS_markup(Search_Query)
    p2 = re.compile(r'\<(\w+)\>')
    CDS_Seq = p2.findall(CDS_Data)
    return(CDS_Seq)


#Create a function to translate the CDS list into the translated protein seq
def CDS_Protein(Search_Query):
    
    CDS_List = CDS_DNA(Search_Query)
    trans_list = []
    for elem in CDS_List:
        coding_DNA2 = Seq(elem, IUPAC.unambiguous_dna)
        trans_list.append(str(coding_DNA2.translate()))
    return(trans_list)



#create a function to match the CDS DNA sequence with the translated protein seq
def matched_seq(Search_Query):
    CDS_Seq = CDS_DNA(Search_Query)
    trans_list = CDS_Protein(Search_Query)
    mapped = zip(CDS_Seq, trans_list)
    matched_seq = list(mapped)

    return(matched_seq)



#create function to determine the codon frequeny in the gene DNA
def codon_freq(Search_Query):
    
    Database_Result = dbapi.dict_entries(Search_Query)
    if Database_Result == False:
      print('Please enter valid search value for either accession, location, gene_id or protein_id')
    DNA_seq = Database_Result['dna_seq']
    
    #create a list of DNA seq split into groups of 3 non-overlapping nucleotides
    p5 = re.compile(r'\w\w\w') 
    codon = p5.findall(DNA_seq)

    #Create a dictionary of codons and populate with the frequency of each codon
    codon_dict = {}
    for elem in codon:
        if elem in codon_dict:
            codon_dict[elem] += 1
        else:
            codon_dict[elem] = 1
    return(codon_dict)


#Create a function to identify RE sites in the CDS regions
def CDS_RE(Search_Query, RE_Site):
    CDS_Seq = CDS_DNA(Search_Query)
    print(CDS_Seq)
    if CDS_Seq == []:
        print ('No CDS sites have been identified in DNA')
    
    for elem in CDS_Seq:
        amb = IUPACAmbiguousDNA()
        search = Seq(elem, amb)
        if RE_Site == 'EcoRI':
            ecori = Restriction.EcoRI.search(search)
            if ecori == []:
                print('There are no EcoRI locations in CDS region',elem)
            else:
                print('The locations for EcoRI RE Site in CDS region',elem, 'are:', ecori)
        elif RE_Site == 'BamHI':
            bamhi = Restriction.BamHI.search(search)
            if bamhi == []:
                print('There are no BamHI locations in CDS region',elem)
            else:
                print('The locations for BamHI RE Site in CDS region',elem, 'are:', bamhi)
        elif RE_Site == 'BsuRI':
            bsuri = Restriction.BsuRI.search(search)
            if bsuri == []:
                print('There are no BsuRI locations in CDS region',elem)
            else:
                print('The locations for BsuRI RE Site in CDS region',elem, 'are:', bsuri)
        else:
            print('CDS_RE function error: invalid search term or RE name')
            
            
#create function to determine the codon frequeny in the whole chromosome
def DNA_Codon():
    
    DNA_list = list(dbapi_column.return_column('dna_seq'))
    DNA = [a for b in DNA_list for a in b] 
    DNA_str = ""
    for elem in DNA:
      DNA_str += elem
      
    p5 = re.compile(r'\w\w\w') 
    codon = p5.findall(DNA_str)

    #Create a dictionary of codons and populate with the frequency of each codon
    codon_dict = {}
    for elem in codon:
        if elem in codon_dict:
            codon_dict[elem] += 1
        else:
            codon_dict[elem] = 1
            
     #turn dictionary into zipped lists for storage in database
     
    codon_value = [codon_dict[key] for key in sorted(codon_dict.keys())]
    codon_key = list(sorted(codon_dict.keys()))
  
    
    codon_list = list(zip(codon_value, codon_key))
    
    
    config_dict = {'host' :'hope',
               'user' : 'pk001',  
               'password'   : 'wbjcod3k6',   
               'port'     : 3306}

    conn = pymysql.connect(**config_dict)

    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS pk001.dna_codon")
    c.execute("CREATE TABLE pk001.dna_codon \
              (frequency INT, \
              codon VARCHAR(10)) ENGINE=InnoDB")
    
    query = "INSERT INTO pk001.dna_codon VALUES(%s,%s)"
    c.executemany(query,codon_list)
                 
    conn.commit
    print("Table 'dna_codon' created and data inserted successfully")   
    conn.commit()
    conn.close()        
    return(codon_dict)
    
    
def get_DNA_codon():
   
    config_dict = {'host' :'hope',
               'user' : 'pk001',  
               'password'   : 'wbjcod3k6',   
               'port'     : 3306}

    conn = pymysql.connect(**config_dict)

    c = conn.cursor()

    c.execute("SELECT * FROM pk001.dna_codon")
    DNA_codon = list(c.fetchall())
    return(DNA_codon)
