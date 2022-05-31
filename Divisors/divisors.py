r=range(1,101)
for i in r:print(*[d for d in r if 0==i%d])
