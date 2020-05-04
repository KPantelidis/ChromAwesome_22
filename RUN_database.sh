#!/bin/bash 

## Log in into database
## Download and extract the data (GenBank file)
## Parse the GenBank file
## Populate the database

echo "## Log in into database"
mysql -u pk001 -p'wbjcod3k6' pk001

echo "## Download and extract the data (GenBank file)"
wget http://www.bioinf.org.uk/teaching/bbk/biocomp2/project/data/chrom_CDS_22.gz -O database

echo "## Parse GeneBank file"
python database/parser.py

echo "## Populate Database"
python database/create_table_and_populate.py
