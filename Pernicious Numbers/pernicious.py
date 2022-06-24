for i in range(3,51):
 n=bin(i).count('1')
 if not 0in[n%b for b in range(2,n)]and n>1:print(i)
