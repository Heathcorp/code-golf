print("   2 3 4 5 6 7\n "+13*"-")
for i in range(16):print("%X:"%i,end='');r=2;exec(6*"print(' '+[chr(r*16+i),'DEL'][r*i>104],end=['','\\n'][r>6]);r+=1;")
