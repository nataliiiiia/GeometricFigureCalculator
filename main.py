from abc import ABC, abstractmethod
import math
from enum import Enum


class PointType(Enum):
    CENTER = "Center"
    BOTTOM_RIGHT = "BottomRight"
    TOP_LEFT = "TopLeft"
    BOTTOM_LEFT = "BottomLeft"
    TOP_RIGHT = "TopRight"


def parse_point_type(s):
    try:
        return PointType(s)
    except ValueError:
        raise ValueError(f"Unknown point type: {s}")


class Figure(ABC):
    allowed_points = set()

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @classmethod
    def validate_point(cls, point_type):
        if not isinstance(point_type, PointType):
            raise ValueError(f"Point type must be a PointType enum, got {point_type}")
        if point_type not in cls.allowed_points:
            raise ValueError(f"{cls.__name__} does not support point type {point_type.name}")

    def __str__(self):
        return f"{self.__class__.__name__} Perimeter {self.perimeter()} Area {self.area()}"


class Square(Figure):
    allowed_points = {
        PointType.BOTTOM_RIGHT,
        PointType.TOP_LEFT,
        PointType.BOTTOM_LEFT,
        PointType.TOP_RIGHT
    }

    def __init__(self, point_x, point_y, side, point_type):
        if side <= 0:
            raise ValueError("The side must be greater than 0.")
        self.validate_point(point_type)
        self.point_x = point_x
        self.point_y = point_y
        self.side = side
        self.point_type = point_type

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2


class Rectangle(Figure):
    allowed_points = {
        PointType.TOP_RIGHT,
        PointType.TOP_LEFT,
        PointType.BOTTOM_RIGHT,
        PointType.BOTTOM_LEFT
    }

    def __init__(self, point1_type, point1_x, point1_y, point2_type, point2_x, point2_y):
        self.validate_point(point1_type)
        self.validate_point(point2_type)

        if point1_x == point2_x or point1_y == point2_y:
            raise ValueError("Invalid points coordinates")

        self.point1_x = point1_x
        self.point1_y = point1_y
        self.point2_x = point2_x
        self.point2_y = point2_y
        self.width = abs(point1_x - point2_x)
        self.height = abs(point1_y - point2_y)

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height


class Circle(Figure):
    allowed_points = {PointType.CENTER}

    def __init__(self, point_type, center_x, center_y, radius):
        if radius <= 0:
            raise ValueError("The radius must be greater than 0.")
        self.validate_point(point_type)
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2


def process_line(line):
    figure_types = {
        "square": Square,
        "rectangle": Rectangle,
        "circle": Circle
    }
    input_parts = line.strip().split()
    fig_type_key = input_parts[0].casefold()

    if fig_type_key not in figure_types:
        raise ValueError(f"{fig_type_key} is not supported.")

    fig_type = figure_types[fig_type_key]

    try:
        if fig_type == Square:
            point_type = parse_point_type(input_parts[1])
            x = float(input_parts[2])
            y = float(input_parts[3])
            side = float(input_parts[5])
            return fig_type(x, y, side, point_type)

        elif fig_type == Rectangle:
            point1_type = parse_point_type(input_parts[1])
            x1 = float(input_parts[2])
            y1 = float(input_parts[3])
            point2_type = parse_point_type(input_parts[4])
            x2 = float(input_parts[5])
            y2 = float(input_parts[6])
            return fig_type(point1_type, x1, y1, point2_type, x2, y2)

        elif fig_type == Circle:
            point_type = parse_point_type(input_parts[1])
            x = float(input_parts[2])
            y = float(input_parts[3])
            radius = float(input_parts[5])
            return fig_type(point_type, x, y, radius)
        else:
            raise ValueError("Unsupported figure.")

    except IndexError:
        raise IndexError("Input is missing required parameters.")
    except ValueError:
        raise ValueError("Invalid numeric input.")


def read_input(from_file, source):
    figures = []
    try:
        if from_file:
            with open(source, 'r') as file:
                for line in file:
                    if line.strip():
                        fig = process_line(line)
                        figures.append(fig)
        else:
            for line in source:
                if line.strip():
                    fig = process_line(line)
                    figures.append(fig)
        for figure in figures:
            shape_name = figure.__class__.__name__
            print(f"{shape_name} Perimeter {figure.perimeter():.0f} Area {figure.area():.0f}")
    except FileNotFoundError:
        print(f"Error: File {source} not found.")


if __name__ == "__main__":
    test_input = [
        "Square TopRight 1 1 Side 2",
        "Rectangle TopRight 2 2 BottomLeft 1 1",
        "Circle Center 1 1 Radius 1",
    ]
    read_input(0, test_input)
    file_path = "input.txt"
    read_input(1, file_path)
