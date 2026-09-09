class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color
    
    def draw(self):
        print("Рисуется фигура")

class Line(Figure):
    def draw(self):
        print("Рисуется линия")

class Rect(Figure):
    def draw(self):
        print("Рисуется прямоугольник")

class Ellipse(Figure):
    def draw(self):
        print("Рисуется эллипс")

class Triangle(Figure):
    def draw(self):
        print("Рисуется треугольник")

figures = [
    Line((0, 0, 10, 10), 2, 'red'),
    Rect((0, 0, 50, 30), 1, 'blue'),
    Ellipse((20, 20), 3, 'green')
]

for fig in figures:
    fig.draw()

figures.append(Triangle((0, 0, 10, 10, 20, 0), 2, 'yellow'))

print("\nПосле добавления треугольника:")
for fig in figures:
    fig.draw()