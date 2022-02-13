#include <stdio.h>
int main(){for(int i=0;i++<100;){if(i%3){if(i%5){printf("%d\n",i);}else{puts("Buzz");}}else{puts("Fizz");}}}