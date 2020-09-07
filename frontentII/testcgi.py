#!/usr/bin/env python3

import cgi

print ("Content-Type: text/html\n")


html="<html>"
html += "<head>\n"
html += "<title>Test CGI script</title>\n"
html += "</head>\n"
html += "<body>\n"
html += "<h1>Test CGI script</h1>\n"
html += "<p>If you see this page, everything is working correctly.</p>\n"
html += "</body>\n"
html += "</html>\n"
print (html)
