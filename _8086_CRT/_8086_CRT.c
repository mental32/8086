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
    PyObject *module = PyModule_Create(&_8086_module);

    if (module == NULL) {
        return NULL;
    }

    if (PyType_Ready(&CShellType) < 0) {
        return NULL
    };

    Py_INCREF(&CShellType);
    PyModule_AddObject(module, "CShell", (PyObject *) &CShellType);

    return module;
}
