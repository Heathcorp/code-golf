l=[0,0,0,1,0]
for(let n=2;n<33;n++){l[n]=l[n]||0
l[n]+=l[n-1]+l[n-2]
print(l[n])}
