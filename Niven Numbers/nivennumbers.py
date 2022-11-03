for i in range(1,101):
 if i%sum([int(d)for d in list(str(i))])==0:print(i)
