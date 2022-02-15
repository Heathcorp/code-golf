import sys
for e in sys.argv[1:]:
 s=[0]*99
 i=0
 for t in e.split(" "):exec(["i+=1;s[i]=int(t)",f"s[i-1]{t}=s[i];i-=1"][t[0]<'0'])
 print(int(s[i]))