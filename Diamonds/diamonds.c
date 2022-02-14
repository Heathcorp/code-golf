main(){
    char* charset="12345678987654321";
    char* end = charset + 18;
    
    for(int j = 1; j < 18; j++,j++,puts("")){
    	for(int i = 0, e = 1; i < j; i++, i < 1 + j / 2 ? e++ : e--){
    		printf("%10.*s%s\n", e, charset, end - e);
    	}
    }
}