s = input().strip()
s =  list(s)

i = len(s)-1 
while i >=0 and s[i] == '1':
    s[i]='0'
    i-=1
if i<0:
    print("NO NEXT")
else:
    s[i]='1'
    print("".join(s))