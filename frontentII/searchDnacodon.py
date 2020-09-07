#!/usr/bin/env python3
import cgi
import business as bl


form = cgi.FieldStorage() #set instance of field storage
value = form.getvalue("x")

print ("Content-Type: text/html\n")

#value = 'AB002059'

table = bl.DNA_Codon()
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
  
 
  html += "</tbody>"
  html += "</table>"
  html += "</ul>\n"
  html += "</body>\n"
  html += "</html>\n"


  print(table)
