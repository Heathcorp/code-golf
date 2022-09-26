main(int argv, char**argc){
for(;*++argc;){
// execute each program
char* prog = *argc;
int i = 0;
int p = 0;
char tape[999] = {0};
int loops[99] = {0};
int li = 0;
int skip = -1;
char c;
for(;c=prog[i];i++){
if(skip<0){
// execute each brainfuck op
if(c=='+')tape[p]++;
if(c=='-')tape[p]--;
if(c=='>')p++;
if(c=='<')p--;
if(c=='.')putchar(tape[p]);
}
// loop logic
if(c=='['){
 loops[li++]=i;
 if(tape[p]==0 && skip<0){
  skip=i;
 }
}
if(c==']'){
 int ls=loops[--li];
 if(skip==ls){
  skip=-1;
 }else if(skip<0 && tape[p]!=0){
  i=ls-1;
 }
}
}
}
}
