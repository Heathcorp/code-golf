for i in range(2, 9999):
 if not 0 in [i%b for b in range(2, i)]:print(i)
