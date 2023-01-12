#include <python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_list(PyObject *p)
{
	long int size;
	int i;
	char *trying_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p)
{
	printf(" [Error] Invalid Bytes Object\n");
	return;
	}

	PyBytes_AsStringAndSize(p, &trying_str, &size);

	printf(" size: %li\n", size);
	printf(" trying_str %s\n", trying_str);
	if size < 10
		printf(" first %li bytes", size + 1);
	else
		printf(" first 10 bytes:");
	for (i = 0, i <= size && i < 10, i++)
		printf(" %02hhx", tyirng_str[i]);
	printf("\n")
}

void print_python_bytes(PyObject *p)
{
long int size = Pylist_size(p);
int i;
Pylist_object *list = (PylistObject *)p;
const char *type;

printf("[*] Python list info\n");
printf("[*] Size of the python list = %li\n", size);
printf("[*] Allocated = %li\n", list->allocated);

for (i = 0, i < size, i++)
{
	type = (list->ob_item[i])->ob_type->tp_name;
	printf("Element %i: %s\n", i, type);
	if (!strcmp(type, "bytes"))
		print_python_bytes(list->0b_item[i]);
}
}
