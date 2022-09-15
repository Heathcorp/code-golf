import sys
for arg in sys.argv[1:]:
 i=0
 tape=[0]*999
 p=0
 loops=[]
 skip=-1
 while i < len(arg):
  c=arg[i]
  if c==']':
   ls=loops.pop()
   if skip==ls:skip=-1
   elif skip==-1 and tape[p]!=0:i=ls-1
  if c=='[':
   loops.append(i)
   if skip==-1 and tape[p]==0:skip=i
  if c=='<':p-=1
  if c=='>':p+=1
  if c=='+':tape[p]+=1
  if c=='-':tape[p]-=1
  if c=='.':print(chr(tape[p]),end='')
  tape[p]=tape[p]%256
  i+=1
