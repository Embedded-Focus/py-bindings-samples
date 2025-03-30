from ctypes import CDLL, c_int


def test_ctypes_printf_c_str() -> None:
    libc = CDLL("libc.so.6")

    printf = libc.printf
    # printf is variadic, so no argtypes specified

    printf("Hello, Wörld!\n".encode())


def test_ctypes_printf_int() -> None:
    libc = CDLL("libc.so.6")

    printf = libc.printf
    # printf is variadic, so no argtypes specified

    printf("The value is: %d\n".encode(), c_int(-42))
