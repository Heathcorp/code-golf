main(i,j,n) {
for(;i<51;i++)
{
for(n=0,j=i;j;j/=2)
{
n+=j&1;
}
n>1&&n^4?printf("%d\n",i):0;
}
}
