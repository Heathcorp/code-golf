#include<stdlib.h>
#include<stdio.h>
#include<time.h>
#include<string.h>

// attempting to cheese the prime numbers code.golf challenge, to see whether it's possible/feasible
int main()
{
	// 				 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
	int target[25] = {1,2,2,4, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8};
	int a[25];
	a[0] = 1;
	int ai,i,mi;

	int seed = 100000000; // best known seed so far: 58794005
	for(mi = 0;;seed++) {
		srand(seed);
		for (i = 1; i < 25; i++)
		{
			if (target[i] != (a[i] = (rand() & 0b110)))
			{
				if (--i > mi)
				{
					mi = i;
					printf("new most digits: %d with seed: %d\n", mi, seed);
				}
				break;
			}
		}		
	}

	printf("seed found! %d\n%d", seed, a[0]);
	for(i = 1; i < 25; i++) {
		printf(" %d", a[i]);
	}
	puts("");
}