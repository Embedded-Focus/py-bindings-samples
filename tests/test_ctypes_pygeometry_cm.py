from pygeometry import rectangle_new


def test_ctypes_pygeometry_scoped() -> None:
    with rectangle_new(2, 3) as r:
        assert r.area() == 6
