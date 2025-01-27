import json
import urllib
import urllib.request
import sys
import pprint
import re

schemaurl = "https://www.kth.se/social/api/schema/v2/course/"
course = "DD1321"
# start = "?startTime=2021-01-14"
# end = "endTime=2021-06-01"

s="[^a-zA-Z,._#¤%/()=`@£$€{[]"
s1="20"+s+s+"-"+s+s+"-"+s+s
# s1=s+s+"-"+s+s+"-"+s+s
# s2=s+s+"-"+s+s+"-"+s+s
# s3=s+s+s+s+s+s

if len(sys.argv) == 2: # Om endast kursen anges, ska den läggas till i schemaurl.
    course = sys.argv[1]
    schemaurl += course

elif len(sys.argv) == 3: # Om både kurs och startdatum anges, läggs de till i länken.
    if re.findall(s1,sys.argv[2])!=None and len(sys.argv[2])==10:
        course = sys.argv[1]
        start = sys.argv[2]
        start = "?startTime="+start #Kombinerar ihop användarens inmatning med en sträng för att få det korrekta formatet.
        schemaurl += course + start #Kombinerar ihop användarens inmatning med en sträng för att få det korrekta formatet.
    else:
        print("Vänligen ange datum i formatet: YYYY-MM-DD") # Om formatet skiljer sig, ber programmet användaren att skriva korrekt datumformat.

elif len(sys.argv) == 4: # Om alla 3 parameterar anges, läggs de till i länken.
    if re.findall(s1,sys.argv[3])!=None and len(sys.argv[3])==10:
        course = sys.argv[1]
        start = sys.argv[2]
        end = sys.argv[3]
        start = "?startTime="+start #Kombinerar ihop användarens inmatning med en sträng för att få det korrekta formatet. 
        end   = "&endTime="+end     #Kombinerar ihop användarens inmatning med en sträng för att få det korrekta formatet.
        schemaurl += course + start + end
    else:
        print("Vänligen ange datum i formatet: YYYY-MM-DD") # Om formatet skiljer sig, ber programmet användaren att skriva korrekt datumformat.


request_data = urllib.request.urlopen(schemaurl).read() # hämtar data från REST-servern
utf_data = request_data.decode('utf-8')                 # översätter u00f6 -> ö
schemainfo = json.loads(utf_data)                     # lägger in i en pythonstruktur



for x in range(len(schemainfo["entries"])):
    if len(schemainfo["entries"][x]["locations"])==0: # om plats för specifikt tillfälle inte anges i schemat, skriv ut "ingen plats angiven"
        print(schemainfo["entries"][x]["start"][0:13] + "-" + schemainfo["entries"][x]["end"][11:13],schemainfo["entries"][x]["title"],"\t","ingen plats angiven")
    else: # Annars skriv ut hela raden.
        print(schemainfo["entries"][x]["start"][0:13] + "-" + schemainfo["entries"][x]["end"][11:13],schemainfo["entries"][x]["title"],"\t",schemainfo["entries"][x]["locations"][0]["name"])


'''

import json
import urllib
import urllib.request
import sys
import pprint
import re

schemaurl = "https://www.kth.se/social/api/schema/v2/course/"
# course = "DD1321"
# start = "?startTime=2021-01-14"
# end   = "&endTime=2021-02-01"


s="[^a-zA-Z,._#¤%/()=`@£$€{[]"
s1="20"+s+s+"-"+s+s+"-"+s+s
s2=s+s+"-"+s+s+"-"+s+s
s3=s+s+s+s+s+s



st=sys.argv[2]
en=sys.argv[3]

x21= re.search(s2,st) #19-12-30
x22= re.search(s3,st) #191230

x31= re.search(s2,en) #19-12-30
x32= re.search(s3,en) #191230

if len(st)!=10 and len(en)!=10:
    if x21:
        st="20"+st

    elif x22==True:
        st="20"+st[0:2]+"-"+ st[2:4]+"-"+ st[4:6]

    if x31:
        en="20"+en

    elif x32==True:
        en="20"+en[0:2]+"-"+ en[2:4]+"-"+ en[4:6]

if len(st)==6 and len(en)==6:
    if x21==True:
        st="20"+st
    
    elif x22:
        st="20"+st[0:2]+"-"+ st[2:4]+"-"+ st[4:6]
    
    if x31==True:
        en="20"+en
    
    elif x32:
        en="20"+en[0:2]+"-"+ en[2:4]+"-"+ en[4:6]


if len(sys.argv) == 2:
    course = sys.argv[1]
    schemaurl += course

elif len(sys.argv) == 3:
    course = sys.argv[1]
    start = st
    start = "?startTime="+start
    schemaurl += course + start

elif len(sys.argv) == 4:
    course = sys.argv[1]
    start = st
    end = en

    start = "?startTime="+start
    end   = "&endTime="+end
    schemaurl += course + start + end


request_data = urllib.request.urlopen(schemaurl).read() # hämtar data från REST-servern
utf_data = request_data.decode('utf-8')                 # översätter u00f6 -> ö
schemainfo = json.loads(utf_data)                     # lägger in i en pythonstruktur



for x in range(len(schemainfo["entries"])):
    if len(schemainfo["entries"][x]["locations"])==0:
        print(schemainfo["entries"][x]["start"][0:13] + "-" + schemainfo["entries"][x]["end"][11:13],schemainfo["entries"][x]["title"],"\t","ingen plats angiven")
    else:
        print(schemainfo["entries"][x]["start"][0:13] + "-" + schemainfo["entries"][x]["end"][11:13],schemainfo["entries"][x]["title"],"\t",schemainfo["entries"][x]["locations"][0]["name"])

'''