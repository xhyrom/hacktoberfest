#include <stdio.h>

void main()
{
  int ch = 33;
  printf("\n\n\n");
  while (ch <= 124)
  {
    if (ch < 100)
    {
      printf("%4d--> %4c | %4d--> %4c | %4d--> %4c | %4d--> %4c \n",
             ch, ch, ch + 1, ch + 1,
             ch + 2, ch + 2, ch + 3, ch + 3);
    }
    else
    {
      printf("%4d--> %4c| %4d--> %4c| %4d--> %4c| %4d--> %4c\n",
             ch, ch, ch + 1, ch + 1,
             ch + 2, ch + 2, ch + 3, ch + 3);
    }
    ch = ch + 4;
  }
  printf("%4d--> %4c| %4d--> %4c|\n", ch, ch, ch + 1, ch + 1);
  printf("\n\n\n");
}