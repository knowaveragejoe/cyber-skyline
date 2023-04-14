#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <err.h>

void init(){
    setvbuf(stdout, NULL , _IONBF , 0);
    setvbuf(stderr, NULL , _IONBF , 0);
    setvbuf(stdin, NULL , _IONBF , 0);
}

int main(void){
    init();
    char buf[64];
    puts("Enter string to be encrypted: ");
    ssize_t bytes = read(0, buf, 0x100);
    if(bytes < 0){
        errx(1, "read error");
    }
    memfrob(buf,bytes);
    printf("Frobnicated Data: %s\n",buf);
    return 0;
}
