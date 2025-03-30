import ctypes
from collections.abc import Generator
from contextlib import contextmanager
from ctypes import c_int, c_void_p

lib = ctypes.CDLL("libgeometry.so")

lib.rectangle_new.argtypes = [c_int, c_int]
lib.rectangle_new.restype = c_void_p

lib.rectangle_delete.argtypes = [c_void_p]
lib.rectangle_delete.restype = None

lib.rectangle_area.argtypes = [c_void_p]
lib.rectangle_area.restype = c_int


class ManagedRectangle:
    def __init__(self, a: int, b: int) -> None:
        self._obj = lib.rectangle_new(a, b)
        if not self._obj:
            raise MemoryError("Failed to allocate Rectangle")

    def __del__(self):
        if self._obj:
            lib.rectangle_delete(self._obj)
            self._obj = None

    def area(self) -> int:
        return lib.rectangle_area(self._obj)


# different approach, similar result:


class ScopedRectangle:
    def __init__(self, handle: c_void_p) -> None:
        self._handle = handle

    def area(self) -> int:
        return lib.rectangle_area(self._handle)


@contextmanager
def rectangle_new(a: int, b: int) -> Generator[ScopedRectangle, None, None]:
    h: c_void_p | None = None
    try:
        h = lib.rectangle_new(a, b)
        if not h:
            raise MemoryError("Could not allocate memory for new rectangle.")
        yield ScopedRectangle(h)
    finally:
        if h:
            lib.rectangle_delete(h)
