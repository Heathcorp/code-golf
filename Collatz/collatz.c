i;j;main(n){
for(;i++<1e3;j=0){
for(n=i;n>1;j++)n=n%2?1+n*3:n/2;
printf("%d\n",j);
}
}
