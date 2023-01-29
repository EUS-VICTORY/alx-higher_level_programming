#include "factor.h"

/**
 * factorise - function that factorises a number
 * @buffer:pointer to the address of the number
 *Return: int
 */

int factorise(char *buffer)
{
  u_int32_t num;
  u_int32_t i;

  num = atoi(buffer);

  for (i = 2; i < num; i++)
    {
      if (num % i == 0)
	{
	  print("%d=%d*%d\n", num, num/i, i);
	  break;
	}
    }
  return (0);
}
