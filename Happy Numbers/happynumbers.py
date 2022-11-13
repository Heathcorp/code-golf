def happy(n,d=0):
 if d>9:return 0
 newnum=sum(map(lambda x:int(x)**2,list(str(n))))
 if newnum==1:return 1
 return happy(newnum,d+1)
for i in range(201):
 if happy(i):print(i)
