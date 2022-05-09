for i in range(2,11):
 for r in [*range(2,i),*range(i,0,-1)]:
  print((11-r)*' ',*range(1,r),*range(r-2,0,-1),sep='')
