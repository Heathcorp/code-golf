main(i,j,n){
for(;i<101;i++){
for(j=i,n=0;j;j/=10)n+=j%10;
i%n?0:printf("%d\n",i);
}
}
