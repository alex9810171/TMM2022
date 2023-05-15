#include <stdio.h>

void for_function(){
	int x = 0;
	for (int i = 1; i <= 5; i++){
		x += i;		
	}
	printf("%d\n", x);
}

void qq_function(){
	int x = 100;
	for (x; x>0; x-=10){
		printf("QQ\n");
	}
}

int main(){
	int count;
	scanf("%d", &count);
	printf("%d", count);
}
