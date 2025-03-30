from pygeometry import Rectangle, rectangle_new


def test_ctypes_pygeometry_rectangle() -> None:
    r = Rectangle(2, 3)
    assert r.area() == 6


def test_ctypes_pygeometry_rectangle_context() -> None:
    with rectangle_new(2, 3) as r:
        assert r.area() == 6
