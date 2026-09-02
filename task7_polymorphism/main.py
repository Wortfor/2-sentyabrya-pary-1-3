# Задача 7: Полиморфизм - единый интерфейс для разных типов
class Figure:
    """
    Базовый класс Figure с общими свойствами и методом draw().
    """
    
    def __init__(self, coords, width, color):
        """
        Конструктор базового класса Figure.
        """
        self.coords = coords
        self.width = width
        self.color = color
    
    def draw(self):
        """
        Метод draw() в базовом классе.
        Будет переопределен в дочерних классах.
        """
        print("Рисуется фигура")


class Line(Figure):
    """
    Дочерний класс Line (линия).
    """
    
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length
    
    def draw(self):
        """
        ПЕРЕОПРЕДЕЛЯЕМ метод draw() для Line.
        Теперь при вызове draw() у Line будет своё сообщение.
        """
        print(f"Рисуется линия: длина {self.length}, цвет {self.color}")


class Rect(Figure):
    """
    Дочерний класс Rect (прямоугольник).
    """
    
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height
    
    def draw(self):
        """
        ПЕРЕОПРЕДЕЛЯЕМ метод draw() для Rect.
        Теперь при вызове draw() у Rect будет своё сообщение.
        """
        print(f"Рисуется прямоугольник: ширина {self.width}, высота {self.height}, цвет {self.color}")


class Ellipse(Figure):
    """
    Дочерний класс Ellipse (эллипс).
    """
    
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius
    
    def draw(self):
        """
        ПЕРЕОПРЕДЕЛЯЕМ метод draw() для Ellipse.
        Теперь при вызове draw() у Ellipse будет своё сообщение.
        """
        print(f"Рисуется эллипс: радиус {self.radius}, цвет {self.color}")


print("="*60)
print("ПОЛИМОРФИЗМ - ЕДИНЫЙ ИНТЕРФЕЙС ДЛЯ РАЗНЫХ ТИПОВ")
print("="*60)
print("Согласно теории:")
print("Мы можем оперировать разными типами объектов")
print("через их единый базовый класс Figure.")
print("="*60)

# Создаем объекты всех трех типов
print("\n1. СОЗДАНИЕ ОБЪЕКТОВ РАЗНЫХ ТИПОВ:")
print("-" * 40)

line = Line((0, 0), 2, "синий", 10)
rect = Rect((5, 5), 4, "красный", 3)
ellipse = Ellipse((10, 10), 3, "зеленый", 5)

print("✅ Созданы объекты разных типов:")
print(f"   - line  (тип: {type(line).__name__})")
print(f"   - rect  (тип: {type(rect).__name__})")
print(f"   - ellipse (тип: {type(ellipse).__name__})")

# СОЗДАЕМ ОДИН ОБЩИЙ СПИСОК
print("\n" + "="*60)
print("2. СОЗДАНИЕ ОДНОГО ОБЩЕГО СПИСКА:")
print("="*60)

figures = [line, rect, ellipse]  # ← ОДИН список для всех типов!
print("✅ Создан список figures, содержащий объекты разных типов")
print("   Список: [Line, Rect, Ellipse]")

print("\n" + "="*60)
print("3. МАГИЯ ПОЛИМОРФИЗМА - ОДИН ЦИКЛ ДЛЯ ВСЕХ:")
print("="*60)
print("Мы НЕ ЗНАЕМ точный тип каждого объекта в списке.")
print("Мы просто вызываем метод draw() для каждого.")
print("Автоматически выполняется код нужного дочернего класса!")
print("-" * 40)

# ОДИН ЦИКЛ для всех типов объектов!
for figure in figures:
    figure.draw()  # ← Вызывается метод нужного класса!

print("\n" + "="*60)
print("4. ДЕМОНСТРАЦИЯ: МЫ НЕ ЗНАЕМ ТИПЫ:")
print("="*60)

print("Типы объектов в списке:")
for i, figure in enumerate(figures, 1):
    print(f"  Элемент {i}: {type(figure).__name__}")

print("\n" + "="*60)
print("5. А ЧТО БЫЛО БЫ БЕЗ ПОЛИМОРФИЗМА?")
print("="*60)

print("""
❌ БЕЗ ПОЛИМОРФИЗМА (плохо):
----------------------------------------
# Нужно знать тип каждого объекта!
for obj in line_list:
    obj.draw_line()
for obj in rect_list:
    obj.draw_rect()
for obj in ellipse_list:
    obj.draw_ellipse()

# При добавлении новых фигур - нужно писать новые циклы!
""")

print("""
✅ С ПОЛИМОРФИЗМОМ (хорошо):
----------------------------------------
# Не нужно знать тип объекта!
for figure in figures:
    figure.draw()  # Всегда работает!

# При добавлении новых фигур - цикл НЕ МЕНЯЕТСЯ!
""")

print("="*60)
print("ВЫВОД:")
print("="*60)
print("✅ Полиморфизм позволяет использовать ЕДИНЫЙ ИНТЕРФЕЙС")
print("✅ Мы НЕ ЗНАЕМ точный тип объекта в списке")
print("✅ Автоматически вызывается метод нужного класса")
print("✅ Код становится ГИБКИМ и РАСШИРЯЕМЫМ")
print("✅ При добавлении новых фигур цикл НЕ МЕНЯЕТСЯ!")