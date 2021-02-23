# cython: language_level=3

from libcpp.string cimport string


cdef extern from "quadopt.h":
    string cpp_optimize "optimize" (const string& segment, double penalty)


cpdef str optimize(str segment, double penalty=1.0):
    cdef bytes result = cpp_optimize(segment.encode("utf-8"), penalty)
    return result.decode("utf-8")
