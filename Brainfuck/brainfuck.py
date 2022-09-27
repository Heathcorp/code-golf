import sys
for a in sys.argv[1:]:
 i=0;t=[0]*99;p=0;l=[];j=-1
 while i<len(a):
  c=a[i]
  if c==']':
   k=l.pop()
   if j==k:j=-1
   elif j<0and t[p]:i=k-1
  if c=='[':
   l+=[i]
   if j<0and t[p]<1:j=i
  if j>0:c=0
  if c=='<':p-=1
  if c=='>':p+=1
  if c=='+':t[p]+=1
  if c=='-':t[p]-=1
  if c=='.':print(chr(t[p]),end='')
  i+=1
