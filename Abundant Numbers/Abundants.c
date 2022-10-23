main(n,i,t){
for(;n++<200;t>n?printf("%d\n",n):0){
for(t=0,i=1;i<n;i++)t+=n%i?0:i;
}
}
