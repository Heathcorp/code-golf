for n in range(201):
 if sum([i for i in range(1,n)if n%i==0])>n:print(n)
