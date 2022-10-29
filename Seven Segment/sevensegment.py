import sys
s=sys.argv[1]
print(*[[' _','  '][c in'14']for c in s])
print(*[['|',' '][c in'1723']+['_',' '][c in'017']+['|',' '][c in'56']for c in s],sep='')
print(*[[[['|_|',' _|'][c in'359'],'|_ '][c=='2'],'  |'][c in'147']for c in s],sep='')
