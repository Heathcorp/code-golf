h=(n,d)=>{
s=n.toString().split('').reduce((a,b)=>+b*(+b)+a,0)
 return d<9?h(s,d+1):(s==1)
}
for(i=0;i<201;i++){
if(h(i,0))print(i)
}
