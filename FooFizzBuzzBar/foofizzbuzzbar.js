for(i=0;i++<1000;){
s=i%2?'':'Foo'
s+=i%3?'':'Fizz'
s+=i%5?'':'Buzz'
s+=i%7?'':'Bar'
print(s?s:i)
}
