from pygeometry import ManagedRectangle


def test_ctypes_pygeometry_managed() -> None:
    r = ManagedRectangle(2, 3)
    assert r.area() == 6
