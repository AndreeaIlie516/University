#include <stdio.h>
#include <string.h>

void asmInterclasare(int length, char sir[], char sir2[], char *strRez);


void citireSirC(char sir[]);


int main()
{
    char str1[] = "acegi";
    char str2[] = "bdfhj";
    //char str1[101];
   // char str2[101];
    char strRez[31] = "";
    int length = strlen(str1);

    //printf("Sirul 1: ");
    //citireSirC(str1);

    //printf("Sirul 2: ");
    //citireSirC(str2);

    asmInterclasare(length, str1, str2, strRez);
    printf("\nSirul rezultat este :%s", strRez);
    return 0;
}

void citireSirC(char sir[])
{
    scanf("%s", sir);
}