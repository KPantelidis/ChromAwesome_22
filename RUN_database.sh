#!/usr/bin/env python3

## Download and extract the data (GenBank file)
## Parse the GenBank file
## Populate the database


echo "## Download and extract the data (GenBank file)"
wget wget http://www.bioinf.org.uk/teaching/bbk/biocomp2/project/data/chrom_CDS_22.gz -O database/chrom_CDS_22.gz

echo "## Parse GeneBank file"
chmod +x database/parser.py
python database/parser.py

echo "## Populate Database"
chmod +x database/create_table_and_populate.py
python database/create_table_and_populate.py
