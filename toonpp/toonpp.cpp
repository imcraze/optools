#include "toonpp.h"
#include "ida.h"

#include <iostream>

PyMODINIT_FUNC PyInit_toonpp(void) {
    return PyModule_Create(&toonppModule);
}

static void print_bytes(const void *object, size_t size)
{
#ifdef __cplusplus
    const unsigned char * const bytes = static_cast<const unsigned char *>(object);
#else // __cplusplus
    const unsigned char * const bytes = object;
#endif // __cplusplus

    size_t i;

    PySys_WriteStdout("[ ");
    for(i = 0; i < size; i++)
    {
        PySys_WriteStdout("%02x ", bytes[i]);
    }
    PySys_WriteStdout("]\n");
}

extern "C" PyObject* toonDecryptByte(PyObject* self, PyObject* args) {
    unsigned char byte;
    int depth;
    unsigned long long key;
    if(!PyArg_ParseTuple(args, "BiK", &byte, &depth, &key))
        return NULL;

    //PySys_WriteStdout("%d", depth);

    //print_bytes(&key, 8);


    uint8 r1 = __ROL1__(byte, 5);
    //printf("r1: %hhX\n", r1);
    uint8 r2 = __ROL1__(((depth >> 6) | 1) * (r1 ^ (key >> (r1 & 0x38))), 5);
    //printf("r2: %hhX\n", r2);
    uint8 r3 = __ROL1__(((2 * depth) | 1) * ((key >> (r2 & 0x38)) ^ r2), 5);

    char ret = ((key >> (r3 & 0x38)) & 0xff) ^ r3;
    if(depth % 2)
        ret = (ret * 0x8f89) - 1;

    PySys_WriteStdout("%hhX ", ret);
    return PyLong_FromDouble((double)ret);

}