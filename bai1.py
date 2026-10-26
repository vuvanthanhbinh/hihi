n , k ,S = map(int, input().split())
ketqua=[]
cur=[]

def quaylui(batdau, tong):
    if len(cur) ==k:
        if tong == S :
            ketqua.append(cur[:])
        return 
    for v in range(batdau, n+1 ):
        if tong + v > S:
            break 
        cur.append(v)
        quaylui(v+1, tong+v)
        cur.pop()
quaylui(1,0)
if len(ketqua)==0:
    print(0)
else:
    print(len(ketqua))
    for r in ketqua:
        print(*r)