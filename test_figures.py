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

def test_process_line_square():
    input = "Square TopRight 1 1 Side 2"
    result = process_line(input)
    assert isinstance(result, Square)
    assert result.point_x == 1
    assert result.point_y == 1
    assert result.side == 2


def test_process_line_circle():
    input = "Circle Center 1 1 Radius 1"
    result = process_line(input)
    assert isinstance(result, Circle)
    assert result.center_x == 1
    assert result.center_y == 1
    assert result.radius == 1


def test_process_line_rectangle():
    input = "Rectangle TopRight 2 2 BottomLeft 1 1"
    result = process_line(input)
    assert isinstance(result, Rectangle)
    assert result.point1_x == 2
    assert result.point1_y == 2
    assert result.point2_x == 1
    assert result.point2_y == 1
    assert result.width == 1
    assert result.height == 1

def test_parse_square():
    input_parts = ["Square", "TopRight", "1", "1", "Side", "2"]
    result = Square.parse(input_parts)
    assert isinstance(result, Square)
    assert result.point_x == 1
    assert result.point_y == 1
    assert result.side == 2

