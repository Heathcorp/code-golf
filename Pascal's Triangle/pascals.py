l=[1,0]
for n in range(3,23):
 b=[0]*n
 for i in range(1,n-1):
  b[i]=l[i]+l[i-1]
  print(b[i],end=' ')
 print()
 l=b
