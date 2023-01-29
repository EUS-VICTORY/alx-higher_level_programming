#include "factors.h"

/**
 * main - main function
 *Return: void
 */

int main(int argc, char *arg[v])
{
  FILE *fptr;
  size_t count;
  ssize_t line;
  char *buffer = NULL;


  if (argc != 2)
    {
      fprintf(stderr, "usage: factor <file name>\n");
      exit(EXIT_FAILURE);
    }
  fptr = fopen(argv[1], "r");
  if (fptr == NULL)
    {
      fprintf(stderr, "Error: can't open file %s\n", argv[1]);
      exit(EXIT_FAILURE);
    }
  while((line = getline(&buffer, &count, fptr != 1)
    {
      factorise(buffer);
    }
  return(0);
}
    
