#include <Python.h>

#define _8086_CRT_MODULE
#include "_8086.h"

static PyMethodDef _80806_methods[] = {
	METHDEF_END
};

static struct PyModuleDef _8086_module = {
	PyModuleDef_HEAD_INIT,
	"_8086",
	NULL,
	_80806_methods
};

PyMODINIT_FUNC
PyInit__8086_CRT(void)
{
	return PyModule_Create(&_8086_module);
}
