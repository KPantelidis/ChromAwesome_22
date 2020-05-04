import API
import API_Column
from Bio import Restriction
from Bio.Seq import Seq
from Bio.Alphabet.IUPAC import IUPACAmbiguousDNA
from Bio.Alphabet import IUPAC
import re

#Create function that will store user input search query and search the database for
#specfic row of data

def search_db():
    '''will search DB for query value, either accession, gene_id, location or protein_id and return a dictionary with the search outcome'''
    Search_Query = input("Please enter a valid accession, gene_id, location or protein_id: ")
    Database_Result = API.dict_entries(Search_Query)
    return(Database_Result)
   

#create function returning cleaned up columns from the DB layer for either location, gene_id, accession or protein_id
def column_list(name):
    '''takes a column name and will return all non-duplicated values and
    remove all 'None' values

    param name: name of a column in SQL table
    returns: a list of entries from column '''

    newlist = API_Column.return_column(name)
    return(newlist)


## Create a function to identify RE enzyme sites in the DNA sequence
def search_RE(Search_Query, RE_name):
    '''takes a restriction enzyme name and will search the gene DNA sequence
    and return the location of the restriction enzyme.

    param RE_name: the name of the restriction enzyme you want to search
                    either EcoRI, BamHI or BsuRI. The search format must be in
                    the same case format as stated here and in a string eg: test = search_RE('EcoRI').
    returns: the location of the searched enzyme in the sequence '''
    
    amb = IUPACAmbiguousDNA()
    Database_Result = API.dict_entries(Search_Query)
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
def CDS_MarkUp(Search_Query):
    '''This function will take a DNA sequence, identify CDS sites and produce a marked up sequence
    that identifies one or more CDS sites in the DNA sequence.

    param: user search query
    return: marked up sequence in string format
    '''
    #Take the search term and search database for corresponding information
    Database_Result = API.dict_entries(Search_Query)
    
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
    '''This function will take the marked up CDS DNA sequence and extract only the CDS information
    param: user search query
    return: list of CDS DNA sequence '''
    
    CDS_Data = CDS_MarkUp(Search_Query)
    p2 = re.compile(r'\<(\w+)\>')
    CDS_Seq = p2.findall(CDS_Data)
    return(CDS_Seq)
 

#Create a function to translate the CDS list into the translated protein seq
def CDS_Protein(Search_Query):
    '''Takes the list of CDS sequences and returns a list of the translated
    protein sequence

    param: user search query
    return: list of translated protein sequences '''

    CDS_List = CDS_DNA(Search_Query)
    trans_list = []
    for elem in CDS_List:
        coding_DNA2 = Seq(elem, IUPAC.unambiguous_dna)
        trans_list.append(str(coding_DNA2.translate()))
    return(trans_list)



#create a function to match the CDS DNA sequence with the translated protein seq
def matched_seq(Search_Query):
    '''takes a search query and will match the translated protein CDS sequence
    with the original CDS DNA sequence.

    param: user search query
    return: list of tuples of matched DNA and protein sequences '''
    CDS_Seq = CDS_DNA(Search_Query)
    trans_list = CDS_Protein(Search_Query)
    mapped = zip(CDS_Seq, trans_list)
    matched_seq = list(mapped)

    return(matched_seq)



#create function to determine the codon frequeny in the gene DNA
def codon_freq(Search_Query):
    '''this function takes a user search query and will return a dictionary of codon
    usage frequencies from the DNA seq.

    param: user search query
    return: dictionary of codons and their frequencies '''

    Database_Result = API.dict_entries(Search_Query)
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
    '''Will take a search query and specified RE and return the location of RE sites in
    the CDS sequence of the gene.

    param: user search query, resriction enzyme name
    return: list of RE locations in seq '''
    CDS_Seq = CDS_DNA(Search_Query)
    if CDS_Seq == []:
        return ('No CDS sites have been identified in DNA')
    
    for elem in CDS_Seq:
        amb = IUPACAmbiguousDNA()
        search = Seq(elem, amb)
        if RE_Site == 'EcoRI':
            ecori = Restriction.EcoRI.search(search)
            if ecori == []:
                return('There are no EcoRI locations in CDS region',elem)
            else:
                return('The locations for EcoRI RE Site in CDS region',elem, 'are:', ecori)
        elif RE_Site == 'BamHI':
            bamhi = Restriction.BamHI.search(search)
            if bamhi == []:
                return('There are no BamHI locations in CDS region',elem)
            else:
                return('The locations for BamHI RE Site in CDS region',elem, 'are:', bamhi)
        elif RE_Site == 'BsuRI':
            bsuri = Restriction.BsuRI.search(search)
            if bsuri == []:
                return('There are no BsuRI locations in CDS region',elem)
            else:
                return('The locations for BsuRI RE Site in CDS region',elem, 'are:', bsuri)
        else:
            return('CDS_RE function error: invalid search term or RE name')
