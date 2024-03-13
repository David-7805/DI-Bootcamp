from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = self.radius * 2

    def area(self):
        return pi * (self.radius ** 2)

    def __str__(self):
        return f'Circle object with radius {self.radius} and diameter {self.diameter}.'

    def __add__(self, another_circle):
        area_new_circle = self.area() + another_circle.area()
        radius_new_circle = (area_new_circle / pi) ** 0.5
        return Circle(radius_new_circle)

    def __gt__(self, another_circle):
        return self.radius > another_circle.radius

    def __eq__(self, another_circle):
        return self.radius == another_circle.radius

    def sort_circles(self, *circles):
        list_of_circles_by_radius = [(self.radius, str(self))]
        for circle in circles:
            list_of_circles_by_radius.append((circle.radius, str(circle)))
        list_of_circles_by_radius.sort()
        sorted_list_of_circles = []
        for circle in list_of_circles_by_radius:
            sorted_list_of_circles.append(circle[1])
        return sorted_list_of_circles


circle_1 = Circle(4)
print(circle_1)
circle_2 = Circle(3)
print(circle_2)
circle_3 = circle_1 + circle_2
print(circle_3)
print(circle_1 > circle_2)
print(circle_1 == circle_2)
circle_4 = Circle(4)
print(circle_1.sort_circles(circle_2, circle_3, circle_4))








