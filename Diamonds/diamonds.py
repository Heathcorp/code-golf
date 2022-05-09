z=range
for i in z(2,11):
 for r in [*z(2,i),*z(i,0,-1)]:print((11-r)*' ',*z(1,r),*z(r-2,0,-1),sep='')
