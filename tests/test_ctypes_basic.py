from ctypes import CDLL, c_char_p, c_int


def test_ctypes_puts_c_str() -> None:
    libc = CDLL("libc.so.6")

    puts = libc.puts
    puts.argtypes = [c_char_p]
    puts.restype = c_int  # default; also set implicitly

    puts("Hello, Wörld!\n".encode())


def test_ctypes_printf_int() -> None:
    libc = CDLL("libc.so.6")

    printf = libc.printf
    # printf is variadic, so no argtypes specified

    printf("The value is: %d\n".encode(), c_int(-42))
