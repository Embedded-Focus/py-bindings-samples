from ctypes import CDLL, CFUNCTYPE, POINTER, c_int, c_size_t, c_void_p, sizeof
from typing import Generic, Protocol, TypeVar, runtime_checkable

CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))

T = TypeVar("T", covariant=True)


@runtime_checkable
class PtrType(Generic[T], Protocol):
    def __getitem__(self, index: int) -> T: ...


def test_ctypes_qsort() -> None:
    @CMPFUNC
    def py_cmp_func(a: PtrType[int], b: PtrType[int]) -> int:
        return a[0] - b[0]
        # return a.contents.value - b.contents.value

    libc = CDLL("libc.so.6")
    qsort = libc.qsort
    qsort.argtypes = [c_void_p, c_size_t, c_size_t, CMPFUNC]
    qsort.restype = None

    IntArray5 = c_int * 5
    ia = IntArray5(5, 1, 7, 33, 99)

    qsort(ia, len(ia), sizeof(c_int), py_cmp_func)

    assert IntArray5(1, 5, 7, 33, 99) != ia, "references must not be equal"
    assert [1, 5, 7, 33, 99] == [elem for elem in ia], "array elements must be equal"
