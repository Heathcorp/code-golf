l=[1]
for n in range(20):
 l+=[0]
 for j in range(n):i=n-j;l[i]+=l[i-1]
 print(*l[:n+1],sep=' ')
