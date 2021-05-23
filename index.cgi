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
<link href='Bestellung.css' rel='stylesheet' type='text/css'>

<title>Meine Bestellung</title>

</head>

<body>

<div class='Bar'>
  
  <a class='Home' href='http://pan.th-brandenburg.de/~alkaisi/'> HOME</a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a class='Ueber' href='http://pan.th-brandenburg.de/~alkaisi/Kontakt.html'> KONTAKT</a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a class='Ueber' href='http://pan.th-brandenburg.de/~alkaisi/Ueber.html'> ÜBER</a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a class='CoronaZahlen' href="http://pan.th-brandenburg.de/~alkaisi/Corona.html"> COVID-19</a>

</div>


<div class='Uebersicht'> <Strong>Übersicht</Strong> 

<br><br>

</div>
''')


print("<div class=List>")
print("<br>")

form = cgi.FieldStorage()

SS = form['SS'].value
ST = form['ST'].value
FS = form['FS'].value
FT = form['FT'].value
HT = form['HT'].value
A = form['A'].value
C = form['C'].value
S = form['S'].value
F = form['F'].value
W0 = form['W0'].value
W1 = form['W1'].value


if SS == '0' and ST == '0' and FS == '0' and FT == '0' and HT == '0' and A == '0' and C == '0' and S == '0' and F == '0' and W0 == '0' and W1 == '0':
    print("<p class='Oops'><Strong> Oops, du hast nichts aus dem Menü ausgewählt</Strong> </p><br>")


if SS != '0':
    print("<p> Schawrma Sandwish x{SSZ} </p>".format(SSZ=SS))

if ST != '0':
    print("<p> Schawrma Teller x{STZ} </p>".format(STZ=ST))
    
if FS != '0':
    print("<p> Falafel Sandwish x{FSZ} </p>".format(FSZ=FS))
    
if FT != '0':
    print("<p> Falafel Teller x{FTZ} </p>".format(FTZ=FT))
    
if HT != '0':
    print("<p> Hummus Teller x{HTZ} </p>".format(HTZ=HT))
    
if A != '0':
    print("<p> Ayran x{AZ} </p>".format(AZ=A))
    
if C != '0':
    print("<p> Coca Cola 0,25L x{CZ} </p>".format(CZ=C))  
    
if S != '0':
    print("<p> Sprite 0,25L x{SZ} </p>".format(SZ=S))
    
if F != '0':
    print("<p> Fanta 0,25L x{FZ} </p>".format(FZ=F))
    
if W0 != '0':
    print("<p> Wasser 0,25L x{W0Z} </p>".format(W0Z=W0))
    
if W1 != '0':
    print("<p> Wasser 1L x{W1Z} </p>".format(W1Z=W1))


print("<br>")
print("</div>")


print('''
<p class='PowerdBy'>Powered by:</p>
  
<a class='Logo' href='https://www.th-brandenburg.de/startseite/'>
<img 
src='https://thbshop.shirt-instyle.de/img/thb-shop-logo-1486808210.jpg'  style=background-color:white;
width='300' height='70' alt='thb'>
   
</a>
''')

print("</body>")
print("</html>")

