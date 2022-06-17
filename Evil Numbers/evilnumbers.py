for i in range(50):
 if sum([i>>b&1for b in range(50)])%2==0:print(i)
