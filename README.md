# Biocomputing II
Group Project/Birkbeck University of London

## ChromAwesome_22
| Members  | Layer |  Email |
| --- | --- | --- |
| Kostas Pantelidis  | Database/First  |  kpantelidis91@gmail.com |
| Annie Page | Business/Middle  | acpage94@gmail.com  |
| Olga Isman  | FrontEnd/Third  | o.isman@imperial.ac.uk  |
| Faizan Shaikh | Alternative FrontEnd  | faizanshaikh1897@gmail.com  |

## Requirements
Our team has been assigned chromosome 22.

[Instructions/Requirements](http://www.bioinf.org.uk/teaching/bbk/biocomp2/project/index.html) can be found here

## Installation

This work has been tested on hope, a server that is internal to Birkbeck crystallography.

To run and populate the database,

1)clone to repository
2)bash RUN_database.sh


The RUN_database.sh file is supposed to download the chromosome zip file, run the file tha parses the GenBank file and then create and populate the table in the database.
However, the RUN_database.sh file does not work properly so I decided to include chrom_CDS_22.gz file in the database folder.
