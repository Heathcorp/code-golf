int i,li,j,c,loops[9];
main(p,a)char**a;{
for(;*++a;p=i=li=j=0){
for(char tape[99]={0};c=*(*a+i);i++){
if(!j){if(c=='+')tape[p]++;if(c=='-')tape[p]--;if(c=='>')p++;if(c=='<')p--;if(c=='.')putchar(tape[p]);}
if(c=='['){
loops[li++]=i;
if(tape[p]==0 && !j){
j=i;
}
}
if(c==']'){
int ls=loops[--li];
if(j==ls){
j=0;
}else if(!j && tape[p]!=0){
i=ls-1;
}
}}}}
