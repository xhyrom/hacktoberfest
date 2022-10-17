#include<stdio.h>

void main(){
    int sticks = 21;
    int temp;
    printf("*****************The 21 Matchstick game******************\n");
    printf("You can pick 1-4 sticks at once.\n");
    printf("One who have to pick the last stick will loose.\n");
    while (1)
    {
        if (sticks <= 1)
        {
            printf("\t\t\tYou loose\n");
            break;
        }
        printf("Choose : ");
        scanf("%d",&temp);
        if (temp>4 || temp<1)
        {
            printf("Wrong choice!!, Voilation of rules!!\n");
            break;
        }
        
        printf("My choice : %d\n",5-temp);
        sticks = sticks -  5;
        printf("\t\t\tNo. of sticks left : %d\n",sticks);
    }
    
}