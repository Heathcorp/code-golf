#include<stdio.h>
int main(){for(int a,b,i=0;i++<100;printf(a*b?"%s%s%d\n":"%s%s\n",a?"":"Fizz",b?"":"Buzz",i)){a=i%3;b=i%5;}}