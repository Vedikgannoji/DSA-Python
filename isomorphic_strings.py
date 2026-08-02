#205 Isomorphic Strings
s = "egg"
t = "add"
def isom(s,t):
    st={}
    ts={}

    if len(s)!=len(t):
        return False
    for s1,t1 in zip(s,t):
        if s1 in st:
            if st[s1]!=t1:
                return False
        else:
            st[s1]=t1
        if t1 in ts:
            if ts[t1]!=s1:
                return False
        else:
            ts[t1]=s1
    return True
print(isom(s,t))