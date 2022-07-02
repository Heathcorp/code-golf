for i in range(1,1001):
 s=['','Foo'][i%2<1]
 s+='Fizz'[i%3*9:]
 s+='Buzz'[i%5*9:]
 s+='Bar'[i%7*9:]
 print([s,i][not s])
