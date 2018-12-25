#define _8086_DISK
#include "_8086.h"

int _8086_VirtualMachine_Boot(void)
{
    PyObject *rv = PyObject_CallObject(_PyFunction_DetectDisks)

    if (rv == Py_None)
    {
        // We got no bootable disk!
    }

    disk = malloc(sizeof(Disk));
    disk->size = PyByteArray_GET_SIZE(rv);
    disk->body = PyByteArray_AS_STRING(rv);

    /*
    BOOTLOADER {
        KMAIN {
            APPLICATIONS
        }
    }
    */

    return 0;
}
