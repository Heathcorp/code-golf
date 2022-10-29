import sys
s=sys.argv[1]
print(*[[' _','  '][c in'14']for c in s])
print(*[[[[['|_|','| |'][c=='0'],'|_ '][c in'56'],' _|'][c in'23'],'  |'][c in'17']for c in s],sep='')
print(*[[[['|_|',' _|'][c in'359'],'|_ '][c=='2'],'  |'][c in'147']for c in s],sep='')
