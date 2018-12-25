#ifndef _8086_CRT_H
#define _8086_CRT_H

#include <Python.h>

#define METHDEF_END {NULL, NULL, 0, NULL}

#ifdef _8086_CRT_MODULE

int _8086_VirtualMachine_Boot(void);
PyTypeObject CShellType;

#endif

#ifdef _8086_DISK

#include <stddef.h>
#include <stdint.h>

typedef struct {
    size_t size;
    uint8_t *body;
} Disk;

#endif

#endif
