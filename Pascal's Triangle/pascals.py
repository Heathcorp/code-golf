l=[0]*99
l[1]=1
for n in range(21):
 for j in range(n):i=n-j;l[i]+=l[i-1];print(l[i],end='\n '[i>1])
