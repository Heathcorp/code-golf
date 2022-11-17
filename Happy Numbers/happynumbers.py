def h(n,d=0):
 s=sum(map(lambda x:int(x)**2,list(str(n))))
 return h(s,d+1)if d<9else s==1
[print(i)for i in range(201)if h(i)]
