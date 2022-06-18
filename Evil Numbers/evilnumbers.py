r=range(50)
for i in r:
 if sum([i>>b&1for b in r])%2==0:print(i)
