#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main ()
{
    int child_status;
    char* arg_list[] = {
    "ls", 
    "-l",
    "/",
    NULL
    }; 
spawn ("ls", arg_list);
wait (&child_status);
if (WIFEXITED (child_status))
    printf ("the child process exited normally, with exit code %d\n",
    WEXITSTATUS (child_status));
else
    printf ("the child process exited abnormally\n");
    return 0;
}