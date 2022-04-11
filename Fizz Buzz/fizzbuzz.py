for i in range(1,101):print(["Fizz"[i%3*4:]+"Buzz"[i%5*4:],i][i%3*(i%5)>0])
