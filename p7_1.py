import os
with open(r'c:\poshe1\log.html','wt',encoding='utf-8') as f: 
    f.write('<html><body>')
    for x,y,z in os.walk('c:\\prg'):
        f.write(f"root: {x}<br>")
        if y:
            f.write(f"dir: {y}<br>")
        if z:
            f.write(f"files: {z}<br>")
        f.write(f"<hr>")
    f.write('</body></html>')
    









##import os
##
####print(os.getcwd())
##f=open(r'C:\Users\LAITEC\Desktop\python_summer_1400\14.wmv','rb')
##fw=open(r'C:\poshe1\14.wmv','wb')
##fw.write(f.read())
##fw.close()
##f.close()
