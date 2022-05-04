l=[1]+[0]*99
for n in range(20):
 for i in range(n,0,-1):l[i]+=l[i-1]
 print(*l[:n+1],sep=' ')
