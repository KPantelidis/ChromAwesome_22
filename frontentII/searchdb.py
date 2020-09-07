#!/usr/bin/env python3
import cgi
import business as bl


form = cgi.FieldStorage() #set instance of field storage
value = form.getvalue("x")

print ("Content-Type: text/html\n")

#value = 'AB002059'

table = bl.search_db(value)
if table == False:
  html = "<html>"
  html += "<html lang= 'en'>\n"
  html += "<head>\n"
  html += "<meta charset = 'utf-8'/>"
  html += "<title> Biocomputing II - Human Genome Browser </title>\n"
  html += "</head>\n"
  html += "<body>\n"
  html += "<h1>Please enter a valid search ID.</h1>\n"
  html += "</body>\n"
  html += "</html>\n"
  print (html)
  
else: 
  html = "<html>"
  html += "<html lang= 'en'>\n"
  html += "<head>\n"
  html += "<meta charset = 'utf-8'/>"
  html += "<title> Biocomputing II - Human Genome Browser </title>\n"
  html += "</head>\n"
  html += "<body>\n"
  html += "<h1> Result</h1>\n"
  
  #Print filtered results as table
  html += "<div class="'col-md-s'"."
  html += "<table class="'table table-bordered'">"
  html += "<thead>"
  html +=     "<tr>"
  html +=         "<th> Accession            </th>"
  html +=         "<th> Gene                 </th>"
  html +=         "<th> Protein Product      </th>"
  html +=         "<th> Chromosomal Location </th>"
  html +=     "</tr>"
  html += "</thead>"
  html += "<tbody>"
  html += "<ul>\n"
  
  gene_id = table['gene_id']
  location = table['location']
  protein_id = table['protein_id']
  accession = table['accession']
  
  html += "<tr>\n"
  html += "<td>\n"+ str(accession) + "</td>\n" 
  html += "<td>\n"+ str(gene_id) + "</td>\n"
  html += "<td>\n"+ str(protein_id) + "</td>\n"
  html += "<td>\n"+ str(location) + "</td>\n"
  html += "</tr>\n"
  html += "</tbody>"
  html += "</table>"
  html += "</ul>\n"
  html += "</body>\n"
  html += "</html>\n"
  
  print(table)
