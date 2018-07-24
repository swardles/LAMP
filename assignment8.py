#!/usr/local/bin/python3

import cgi, cgitb
cgitb.enable()
import sys, os
import codecs
import pymysql
from assignment8Variables import *
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())



#send raw HTTP headers to browser
print("Content-type: text/html;charset=utf-8")
print("\n\n")
print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<title> US County Information</title>")
print('<link rel= "stylesheet" type = "text/css" href = "assignment8.css" />')
print("</head>")

print("<body>")
print("<h3> US County Information</h3>\n<hr />")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#print("<p>hello world</p>")
# set the connection
cxn = pymysql.connect(host,user,passwrd,db,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
#get a 'cursor'... a pointer to the database

#get the HTML form data
form = cgi.FieldStorage()
s = form["state"].value
q = form["quantity"].value
so = form["sorting"].value

cur = cxn.cursor()

#create the query inputed
query = '''SELECT state, name, population
	FROM c
	WHERE state = "'''+s+'''" 
	ORDER BY '''+so+'''
	LIMIT '''+q
print("<p>" +query+"</p> <hr/>")

cur.execute(query)

result = cur.fetchall()

print("<h4>Query results for "+s+"</h4>")



print("<table>")
for row in result:
    print("<tr>")
    print("<td>"+row['state']+"</td>")
    print("<td>"+row['name']+"</td>")
    print("<td>"+format(row['population'],",d")+"</td>")
    print("</tr>")
print("</table>")
#print("\n")
#print(s)

if s == "AL":
	print('''<img src="alabama-flag.png" alt="Alabama's State Flag" style="width:150px;height:100px;">''')
	print('''<img src="a2.jpeg" style="width:150px;height:100px;">''')
	print('''<img src="al2.jpeg" style="width:150px;height:100px;">''')
	print('''<a href="http://www.alabama.gov/">Visit the Alabama State Website</a>''')
if s == "CA":
	print('''<img src="cali.png" alt="California's State Flag" style="width:150px;height:100px;">''')
	print('''<img src="c2.jpeg" style="width:150px;height:100px;">''')
	print('''<img src="c3.jpeg" style="width:150px;height:100px;">''')
	print('''<a href="https://www.ca.gov/">Visit the California State Website</a>''')

if s == "NJ":
	print('''<img src="nj.png" alt="New Jersey's State Flag" style="width:150px;height:100px;">''')
	print('''<img src="nj2.jpeg" style="width:150px;height:100px;">''')
	print('''<img src="nj3.jpeg" style="width:150px;height:100px;">''')
	print('''<a href="http://www.nj.gov/">Visit the New Jersey State Website</a>''')

if s == "NY":
	print('''<img src="ny.png" alt="New York's State Flag" style="width:150px;height:100px;">''')
	print('''<img src="ny2.jpeg" style="width:150px;height:100px;">''')
	print('''<img src="ny3.png" style="width:150px;height:100px;">''')
	print('''<a href="https://www.ny.gov/">Visit the New York State Website</a>''')

if s == "OR":
	print('''<img src="or.png" alt="Oregon's State Flag" style="width:150px;height:100px;">''')
	print('''<img src="or2.jpeg" style="width:150px;height:100px;">''')
	print('''<img src="or3.png" style="width:150px;height:100px;">''')
	print('''<a href="http://www.oregon.gov/pages/index.aspx">Visit the Oregon State Website</a>''')


# # close the connection
cur.close()
#print out the bottom of the document
print("</body>\n</html>")
