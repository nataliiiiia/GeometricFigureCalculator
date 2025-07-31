import main
from main import PointType, Square, Rectangle, Circle, process_line

def test_square():
    square = Square(0, 0, 1, PointType.BOTTOM_LEFT)
    assert square.side == 1
    assert square.perimeter() == 4
    assert square.area() == 1

def test_square2():
    square = Square(0, 0, 1, PointType.TOP_RIGHT)
    assert square.side == 1
    assert square.perimeter() == 4
    assert square.area() == 1

def test_square3():
    square = Square(0, 0, 1, PointType.BOTTOM_RIGHT)
    assert square.side == 1
    assert square.perimeter() == 4
    assert square.area() == 1

def test_process_line():
    input = "Square TopRight 1 1 Side 2"
    result = process_line(input)
    assert isinstance(result, Square)
    assert result.point_x == 1
    assert result.point_y == 1
    assert result.side == 2


def test_parse_square():
    input_parts = ["Square", "TopRight", "1", "1", "Side", "2"]
    result = Square.parse(input_parts)
    assert isinstance(result, Square)
    assert result.point_x == 1
    assert result.point_y == 1
    assert result.side == 2

