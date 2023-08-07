int main(int argc, char** argv){
for(;--argc;){
char* s = *++argv;
int l = strlen(s);
 for(int i=0;i<l;i+=16,s+=16){
  printf("%08x: ",i);
  for(int j=0,k=0;j<16;j++,s[k]?k++:0){
   printf(s[k]?"%02x":"  ",s[k]);
   j&1?printf(" "):0;
  }
  putchar(' ');
  for(int j=0;j<16&&s[j];j++)
   putchar(s[j]-10?s[j]:'.');
  puts("");
 }
puts("");
}
}
