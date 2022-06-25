for i in range(1,1001):
 s=''
 if i%2==0:s='Foo'
 if i%3==0:s+='Fizz'
 if i%5==0:s+='Buzz'
 if i%7==0:s+='Bar'
 if len(s)<1:s=str(i)
 print(s)
