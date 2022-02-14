#include<stdlib.h>
#include<stdio.h>
#include<time.h>
#include<string.h>

// attempting to cheese the niven numbers code.golf challenge, to see whether it's possible/feasible
int main()
{
	int target[33] = {1,2,3,4,5,6,7,8,9,10,12,18,20,21,24,27,30,36,40,42,45,48,50,54,60,63,70,72,80,81,84,90,100};
	int a[33];
	int ai,i;

	int seed;
	srand(time(NULL));
	for(;;) {
		seed = rand();
		srand(seed);
		for (i=1,ai=0; i < 101 && ai < 33; i++)
		{
			rand()&3 ? a[ai++]=i : 0;
		}
		if(memcmp(target, a, 48) == 0) {
			break;
		}
	}

	printf("seed found! %d\n%d", seed, a[0]);
	for(int j = 1; j < 33; j++) {
		printf(" %d", a[j]);
	}
	puts("");
}