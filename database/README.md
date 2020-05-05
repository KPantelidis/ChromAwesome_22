## Database Layer
Kostas Pantelidis\
Birkbeck university of London\
Bioinformatics and Systems Biology\
Biocomputing II


The are three coding files.
Two for the database and one for the database api to the business layer

To run the database, one should run the following in the specific order: 
1) parser.py
2) create_table_and_populate.py

The RUN_database.sh file is supposed to download the chromosome zip file, run the file tha parses the GenBank file and thn create and populate the table in the database.\
However, the RUN_database.sh file does not work properly so I decided to include chrom_CDS_22.gz file. 

The doc folder contains the documentation for the database, the database api and a reflective essay.
