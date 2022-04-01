for(line of arguments){
l=[]
n=0
for(a of line.split(' ')){
if(a<'0'){
eval(`l[n-2]${a}=l[--n]`)
}else{
l[n++]=~~a
}
}
print(l[0])
}
