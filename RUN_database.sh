#!/bin/bash 

## Log in into database
## Download and extract the data (GenBank file)
## Parse the GenBank file
## Populate the database


echo "## Download and extract the data (GenBank file)"
wget http://www.bioinf.org.uk/teaching/bbk/biocomp2/project/data/chrom_CDS_22.gz -O database/chrom_CDS_22.gz

echo "## Parse GeneBank file"
python database/parser.py

echo "## Populate Database"
python database/create_table_and_populate.py
