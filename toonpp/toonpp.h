#ifndef TOONPP_TOONPP_H
#define TOONPP_TOONPP_H

#include <Python.h>



extern "C" PyObject* toonDecryptByte(PyObject* self, PyObject* args);

static PyMethodDef toonppMethods[] = {
        {"decryptByte", toonDecryptByte, METH_VARARGS, "Decrypts bytes from a code object."},
        {NULL, NULL, 0, NULL}
};

static struct PyModuleDef toonppModule = {
        PyModuleDef_HEAD_INIT,
        "toonpp",
        NULL,
        -1,
        toonppMethods
};

#endif //TOONPP_TOONPP_H
