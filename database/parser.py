import re

my_list = []
with open('bla', mode="r") as bla:
    reader = bla.read()
    my_list = reader.split("//\n")

 
list_of_entries = []
accession_list = []
gene_id_list = []
location_list = []
protein_id_list = []
product_list = []
translation_list = []

for i in my_list:    

    #-----------accession----------------
    p1 = re.compile(r'\bACCESSION \s+\w+\s')
    p1 = p1.findall(i)
    p1 = [i.replace('ACCESSION', '').strip() for i in p1]
    accession_list += p1
    
    #-----------gene_id-------------------
    p2 = re.compile(r'/gene=".+?"\s+')
    if p2.search(i):
        p2 = p2.findall(i)
        p2 = [i.replace('/gene="', '').replace('"', '').strip() for i in p2] 
        p2 = list(dict.fromkeys(p2)) #for duplicates
        gene_id_list.append(p2[0])
    else:
        gene_id_list.append('None')
        
    #-----------location-------------------
    p3 = re.compile(r'/map=".+?"\s+')
    if p3.search(i):
        p3 = p3.findall(i)
        p3 = [i.replace('/map="', '').replace('"', '').strip() for i in p3] 
        p3 = list(dict.fromkeys(p3)) #for duplicates
        location_list.append(p3[0])
    else:
        location_list.append('None')
        
    #-----------protein_id-------------------
    p10 = re.compile(r'/protein_id=".+?"\s+')
    if p10.search(i):
        p10 = p10.findall(i)
        p10 = [i.replace('/protein_id="', '').replace('"', '').strip() for i in p10] 
        p10 = list(dict.fromkeys(p10)) #for duplicates
        protein_id_list.append(p10[0])
    else:
        protein_id_list.append('None')
        
    #-----------product-------------------
    p11 = re.compile(r'/product=".+?"\s+')
    if p11.search(i):
        p11 = p11.findall(i)
        p11 = [i.replace('/product="', '').replace('"', '').strip() for i in p11] 
        p11 = list(dict.fromkeys(p11)) #for duplicates
        product_list.append(p11[0])
    else:
        product_list.append('None')   
       
#-----------translation----------------    
    p12 = re.compile(r'/translation="(.[^"]*?)"\s')
    if p12.search(i):
        p12=p12.findall(i)
        p12 = [i.replace('\n', '').replace(' ','').strip() for i in p12]
        p12 = list(dict.fromkeys(p12)) #for duplicates
        translation_list.append(p12[0]) 
    else:
        translation_list.append('None')
#print(translation_list)
        
#---------dna_sequence--------- 
# no need to check for duplicates, there's only one origin per entry
dna_list =[]      
for i in my_list:
    dna = []
    p4 = re.compile(r'(ORIGIN\s+)((.*\n){1,})')
    it = p4.finditer(i)
    for match in it:
        dna.append(match.group(2))
        dna = [i.replace('\n', '').replace(' ', '').strip() for i in dna]
        dna = [re.sub('[0-9]', '', i) for i in dna] 
    dna_list += dna
#print(dna_list)   
     
#----------gene_bp------------------
gene_bp_list = []
for i in my_list:
    gene_bp = []
    p6 = re.compile(r'(\bLOCUS)\s+(\w+)\s+(\d+)\s+')
    if p6.search(i):
        p6 = p6.findall(i)
        p6 = re.compile(r'(\bLOCUS)\s+(\w+)\s+(\d+)\s+')
        it = p6.finditer(i)
        for match in it:
            gene_bp.append(match.group(3))
        gene_bp_list += gene_bp
    else:
        gene_bp_list.append('None')
#no need to check for duplicates, i take it from LOCUS line


#----------CDS---------    
cds_list = []
for i in my_list:
    p7 = re.compile(r'CDS\s*(.[^\/]*?)\/')
    if p7.search(i):
        p7 = p7.findall(i)
        p7 = [i.replace('\n', '')
                .replace(' ', '')
                .replace('join', '')
                .replace('complement','')
                .strip() for i in p7]
        cds_list.append(p7[0])
    else:
        cds_list.append('None')

#--------complement----------
complement_list = []
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
