for i in range(1,1001):s='Foo'[i%2*9:]+'Fizz'[i%3*9:]+'Buzz'[i%5*9:]+'Bar'[i%7*9:];print([s,i][not s])
