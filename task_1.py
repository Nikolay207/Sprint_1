a = '1h 45m,360s,25m,30m 120s,2h 60s'
a_new= a.replace(',', ' ')
b=a_new.split()
m=0
for i in b:
    if 'h' in i:
        d=i.replace('h', '')
        m = m + int(d)*60
    elif 'm' in i:
        t=i.replace('m', '')
        m = m + int(t)
    elif 's' in i:
        t = i.replace('s', '')
        m = m + int(t)//60
print(m)