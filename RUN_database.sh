#!/bin/bash 

## Log in into database
## Download and extract the data (GenBank file)
## Parse the GenBank file
## Populate the database

echo "## Log in into database"
mysql -u pk001 -p'wbjcod3k6' pk001

echo "## Download and extract the data (GenBank file)"
wget http://www.bioinf.org.uk/teaching/bbk/biocomp2/project/data/chrom_CDS_22.gz -O /d/user6/pk001/Group_Project

echo "## Parse GeneBank file"
python /d/user6/pk001/Group_Project/parse.py

echo "## Populate Database"
python /d/user6/pk001/Group_Project/create_table_and_populate.py
