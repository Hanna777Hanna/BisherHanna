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
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a class='CoronaZahlen' href="http://pan.th-brandenburg.de/~alkaisi/Corona.html"> COVID-19</a>

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


if len(V) ==0  or len(N)==0 or len(E)==0 or len(NA)==0:
    print("<p class='Oops'><Strong> Oops, bitte füll alle Eingabefeldenr aus</Strong></p><br>")

if len(V)==0:
    print("<br>")
else : 
    print("<p>Vorname:</p>")
    print("<p>{VV}</p><br>".format(VV=V))

if len(N)==0:
    print("<br>") 
else : 
    print("<p>Nachname:</p>")
    print("<p>{NV}</p><br>".format(NV=N))


if len(E)==0:
    print("<br>") 
else : 
    print("<p>Email:</p>")
    print("<p>{EV}</p><br>".format(EV=E))


if len(NA)==0:
    print("<br>") 
else : 
    print("<p>Nachricht:</p>")
    print("<p>{NAV}</p><br>".format(NAV=NA))



print('''
</div>
  
<br><br><br><br><br><br>
  
  
<p class='PowerdBy'>Powered by:</p>
  
<a class='Logo' href='https://www.th-brandenburg.de/startseite/'>
<img src='https://thbshop.shirt-instyle.de/img/thb-shop-logo-1486808210.jpg' alt='thb' style=background-color:white;  
width='300' height='70'>
   
</a>
 

</body>
</html>
''')
