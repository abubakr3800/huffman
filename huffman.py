def lam(e):
  return e[1]

def find_prop(i):
    l = len(i)
    d = []
    s = set(i.copy())
    for x in s:
        d.append((x,round((i.count(x)/l),4)))
        
    return(sorted(d,key=lam,reverse=True))

def huffman(d,h):
    l,v1=d[-1]
    L,v2=d[-2]   
    d=d[:-2]
    if h.keys() is not None:
        for e in list(h.keys()):
            if e in l :
                h[e] = '1' + h[e]
            if e in L :
                h[e] = '0' + h[e]
    h[l],h[L]='1','0'
    d.append((f'{l}{L}',round(v1+v2,4)))
    d=sorted(d,key=lam,reverse=True)
    return(d,h)
   
i = input("Your Message : ")
i=[x for x in i]
d=find_prop(i)
print("probabilities =",d)
h=dict()
while(len(d)!=1):    
    d,h=huffman(d,h)
for e in set(i) :
    print(f"The encode of \"{e}\" is :",h[e])