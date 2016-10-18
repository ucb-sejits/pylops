import numpy as np


def element_size(arr):
    return arr.nbytes / arr.size


def strides(arr):
    stride = arr.strides
    el_size = element_size(arr)
    return [s/el_size for s in stride]


def get_base(arr):
    if arr.base is not None:
        return arr.base
    return arr


def get_start(arr):
    return arr.__array_interface__['data'][0]


def get_array_offset(arr):
    """returns the start of the array as an num-element offset from arr.base"""
    base = get_base(arr)
    base_start = get_start(base)
    arr_start = get_start(arr)
    byte_difference = arr_start - base_start
    return byte_difference / element_size(arr)


# Instead of using flatten, use arr.base for pointer access
def get_pointer(arr):
    base = get_base(arr)
    return np.ctypeslib.ndpointer(base.dtype, base.ndim, base.shape)


# Generic indexing algorithm with offset
def generate_encode_with_offset(strides, offset):
    pass
