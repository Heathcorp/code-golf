a,b,c,d,e,f,g,h;main(u,v)char**v;{for(;*++v;printf("%d
",a+c<e|e+g<a|b+d<f|f+h<b?0:abs((a+c<e+g?a+c:e+g)-(a>e?a:e))*abs((b+d<f+h?b+d:f+h)-(b>f?b:f))))sscanf(*v,"%d%d%d%d%d%d%d%d",&a,&b,&c,&d,&e,&f,&g,&h);}
