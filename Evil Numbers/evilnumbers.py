for i in range(50):
 e=0;b=i
 while b:e+=b&1;b>>=1
 if e%2^1:print(i)
