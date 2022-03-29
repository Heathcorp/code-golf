import sys
def spell(n):
 words = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
 word2 = [0,0,"twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
 if n>999:return "one thousand"
 if n > 99:
  i = n%100
  return words[n//100] + " hundred" + (" and " + spell(n%100)if i>0else"")
 if n > 19:
  i = n%10
  return word2[n//10] + ("-"+words[i]if i>0else"")
 return words[n]
for n in sys.argv[1:]:print(spell(int(n)))
