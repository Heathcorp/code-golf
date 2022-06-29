for i in range(1,1001):
 s=['','Foo'][i%2<1]
 s+='Fizz'[i%3*9:]
 if i%5<1:s+='Buzz'
 if i%7<1:s+='Bar'
 print([s,i][not s])
