fn main(){
for i in 1..1001{
let mut n = 0;
let mut j = i;
while j>1{n+=1;if j%2>0{j=j*3+1}else{j/=2}}
println!("{n}");
}
}
