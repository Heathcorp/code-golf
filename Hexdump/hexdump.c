main(i,v,l,j,I)char**v;{for(char*s,*t;s=t=*++v;puts(""))for(l=i=j=I=0;l<strlen(*v);puts("")){for(printf("%08x:",l),l+=16;i<l;printf(*s?"%02x":"  ",*s?*s++:0))printf(" "+i++%2);for(printf("  ");j<l&&*t;j++,t++)putchar(*t-10?*t:46);}}