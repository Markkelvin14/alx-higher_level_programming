#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int m = 0, size, dre;
	PyObject *obj;

	size = Py_SIZE(p);
	dre = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", dre);
	for (m = 0; m < size; m++)
	{
		printf("Element %d: ", m);
		obj = PyList_GetItem(p, m);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
