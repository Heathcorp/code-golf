import sys
s=[]
for l in sys.argv[1:]:
 for o in l.split():exec(["s+=[int(o)]",f"s+=[s.pop(-2){o}s.pop()]"][o<'0'])
 print(int(s[-1]))
