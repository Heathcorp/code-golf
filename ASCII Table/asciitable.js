write("   2 3 4 5 6 7\n -------------")
for(i=0;i<16;i++){write("\n"+"0123456789ABCDEF"[i]+":")
for(j=2;j<8;j++){write("",i*j<105?String.fromCharCode(j*16+i):"DEL")}}
