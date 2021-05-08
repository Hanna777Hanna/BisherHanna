#!/usr/bin/python
import cgi
import cgitb

cgitb.enable()


print("Content-Type: text/html")
print("")
print("<!DOCTYPE html>")
print("<html lang=de>")
print("<head>")
print("<title>")
print("<Die Dosis zur Behandlung>")
print("</title>")
print("</head>")
print("<body>")

form = cgi.FieldStorage()

def marinelli():
    k=24.7 
    hwz=8
    try:
        dose = float(form['Dosis'].value)
        volume = float(form['Volumen'].value)
        uptake= float(form['Uptake'].value)
        if (dose==150 or dose==350 and volume>=10 and volume<=25 and uptake>=10 and uptake<=100):
            activity = ((dose*volume)/uptake*hwz)*k
            return str(activity) + "[mBq]"
        else:
            return "Bitte halten Sie sich an die Vorgaben!"
    except:
        return "Es duerfen nur die Zahlen eingetragen werden"
        
print(marinelli())

print("</body>")
print("</html>")
