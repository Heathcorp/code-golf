l=[0,1]
for n in range(3,23):
 l+=[0]
 for i in range(n-2,0,-1):l[i]+=l[i-1];print(l[i],end=' ')
 print()
