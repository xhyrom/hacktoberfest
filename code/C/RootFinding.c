#include <stdio.h>

float Sqroot(float num)
{
    float i;
    int max = 5;
    i = num / 2;
    int temp = 1;
    while (temp <= max)
    {
        i = (i * i * i + 3 * i * num) / (3 * i * i + num);
        temp++;
    }
    return i;
}

void main()
{
    int number = 1;
    printf("Square Roots of first 20 naturals number :\n");
    while (number<=25)
    {
        printf("%5d ---->   %5f\n",number,Sqroot(number));
        number++;
    }
    
}