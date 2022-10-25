#include <stdio.h>
#include <unistd.h>

int main()
{
    printf("the process ID is %d\n", getpid());
    printf("the parent process ID is %d\n", getppid());
    return 0;
}