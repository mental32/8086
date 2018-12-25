#include "_8086.h"

typedef struct {
    PyObject_HEAD
} CShell;


static PyMemberDef CShell_members[] = {{NULL}};
static PyMethodDef CShell_methods[] = {{NULL}};

PyTypeObject CShellType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "_8086.CShell",
    .tp_basicsize = sizeof(CShell),
    .tp_itemsize = 0,
    .tp_new = CShell_new,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_dealloc = (destructor) CShell_dealloc,
    .tp_members = CShell_members,
    .tp_methods = CShell_methods,
};

/* ============================================================ */
static void
CShell_dealloc(CShell *self)
{
    // Recipe for deallocation is just
    // Py_XDECREF(self->attribute);
    // for every attribute.

    Py_TYPE(self)->tp_free((PyObject *) self);
}

static PyObject *
CShell_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    return (PyObject *)((CShell *)type->tp_alloc(type, 0));
}
/* ============================================================ */
