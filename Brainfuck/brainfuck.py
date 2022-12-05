import sys
for a in sys.argv[1:]:
 i=0;t=[0]*99;p=0;l=[];j=0
 while i<len(a):
  c=a[i]
  if c==']':
   k=l.pop()
   if j==k:j=0
   elif j<1and t[p]:i=k-1
  if c=='[':
   l+=[i]
   if j<1and t[p]<1:j=i
  if j:c=0
  p+=(c=='>')-(c=='<')
  t[p]+=(c=='+')-(c=='-')
  if c=='.':print(chr(t[p]),end='')
  i+=1
