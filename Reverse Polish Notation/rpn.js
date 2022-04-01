for(k of arguments){l=[]
n=0
for(a of k.split(' ')){a<'0'?eval(`l[n-2]${a}=l[--n]`):l[n++]=~~a}print(l[0])}
