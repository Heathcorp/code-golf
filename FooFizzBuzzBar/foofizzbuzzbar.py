for i in range(1,1001):
 s=''
 if i%2<1:s='Foo'
 if i%3<1:s+='Fizz'
 if i%5<1:s+='Buzz'
 if i%7<1:s+='Bar'
 if len(s)<1:s=str(i)
 print(s)
