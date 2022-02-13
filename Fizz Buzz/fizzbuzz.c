#include <stdio.h>
int main(){
	int a,b;
	for(int i=0;i++<100;puts("")){
		if((a=i%3)==0)printf("Fizz");
		if((b=i%5)==0)printf("Buzz");
		if(a&&b)printf("%d",i);
	}
}