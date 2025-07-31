from main import PointType, Square, Rectangle, Circle

def test_square():
    square = Square(0, 0, 1, PointType.BOTTOM_LEFT)
    assert square.side == 1
    assert square.perimeter() == 4
    assert square.area() == 1

