#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import cgi

print("Content-Type: text/html")
print("")

print('''
<!DOCTYPE html>

<html lang=de>

<head>

  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width'>
  <link href='Nachricht.css' rel='stylesheet' type='text/css'>
  <title>Deine Nachricht</title>
  
</head>
  

<body>
  
<div class='Bar'>
  
  <a class='Home' href='http://pan.th-brandenburg.de/~alkaisi/'> HOME</a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a class='Ueber' href='http://pan.th-brandenburg.de/~alkaisi/Kontakt.html'> KONTAKT</a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a class='Über' href='http://pan.th-brandenburg.de/~alkaisi/Ueber.html'> ÜBER</a>

</div>

  
<div class='Uebersicht'> <Strong>Übersicht</Strong> 

<br><br>

</div>
  
<div class='List'>
<br>
''')

form = cgi.FieldStorage()

V = form['Vorname'].value
N = form['Nachname'].value
E = form['Email'].value
NA = form['Nachricht'].value


if V == "" and N == "" and E == "" and NA == "":
    print("<p class='Oops'><Strong> Oops, du hast nichts in der Nachricht geschrieben</Strong></p><br>")

if V != "":
    print("<p>Vorname:</p>")
    print("<p>{VV}</p><br>".format(VV=V))

if N != "":
    print("<p>Nachname:</p>")
    print("<p>{NV}</p><br>".format(NV=N))


if E != "":
    print("<p>Email:</p>")
    print("<p>{EV}</p><br>".format(EV=E))


if NA != "":
    print("<p>Nachricht:</p>")
    print("<p>{NAV}</p><br>".format(NAV=NA))



print('''
</div>
  
<br><br><br><br><br><br>
  
  
<p class='PowerdBy'>Powered by:</p>
  
<a class='Logo' href='https://www.th-brandenburg.de/startseite/'>
<img 
src='https://thbshop.shirt-instyle.de/img/thb-shop-logo-1486808210.jpg' 
width='300' height='70' alt='thb'>
   
</a>
 

</body>
</html>
''')
