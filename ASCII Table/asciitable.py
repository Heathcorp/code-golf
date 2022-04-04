print("   2 3 4 5 6 7\n "+13*"-")
for i in range(16):
 print("%X:"%i,end='')
 for r in range(2,8):
  print(" "+[chr((r<<4)+i),'DEL'][r*i>104],end=['','\n'][r>6])
