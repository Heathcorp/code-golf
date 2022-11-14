def h(n,d=0):
 if d>9:return 0
 s=sum(map(lambda x:int(x)**2,list(str(n))))
 if s==1:return 1
 return h(s,d+1)
for i in range(201):
 if h(i):print(i)
