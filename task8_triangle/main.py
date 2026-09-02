# Задача 8: Полиморфизм - расширение без изменения кода
class Figure:
    """
    Базовый класс Figure с общими свойствами и методом draw().
    """
    
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color
    
    def draw(self):
        print("Рисуется фигура")


class Line(Figure):
    """Дочерний класс Line (линия)."""
    
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length
    
    def draw(self):
        print(f"Рисуется линия: длина {self.length}, цвет {self.color}")


class Rect(Figure):
    """Дочерний класс Rect (прямоугольник)."""
    
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height
    
    def draw(self):
        print(f"Рисуется прямоугольник: ширина {self.width}, высота {self.height}, цвет {self.color}")


class Ellipse(Figure):
    """Дочерний класс Ellipse (эллипс)."""
    
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius
    
    def draw(self):
        print(f"Рисуется эллипс: радиус {self.radius}, цвет {self.color}")


# =============================================
# НОВЫЙ КЛАСС - ДОБАВЛЕН БЕЗ ИЗМЕНЕНИЯ СТАРОГО КОДА!
# =============================================
class Triangle(Figure):
    """
    НОВЫЙ дочерний класс Triangle (треугольник).
    Добавлен без изменения существующего кода!
    """
    
    def __init__(self, coords, width, color, sides):
        """
        Конструктор класса Triangle.
        
        Параметры:
        coords (tuple): координаты (x, y)
        width (float): ширина треугольника
        color (str): цвет треугольника
        sides (tuple): длины сторон треугольника (a, b, c) - уникальное свойство
        """
        super().__init__(coords, width, color)
        self.sides = sides  # уникальное свойство для треугольника
    
    def draw(self):
        """
        ПЕРЕОПРЕДЕЛЯЕМ метод draw() для Triangle.
        Теперь при вызове draw() у Triangle будет своё сообщение.
        """
        print(f"Рисуется треугольник: стороны {self.sides}, цвет {self.color}")


print("="*60)
print("ПОЛИМОРФИЗМ - РАСШИРЕНИЕ БЕЗ ИЗМЕНЕНИЯ КОДА")
print("="*60)
print("Согласно теории:")
print("В будущем в программу можно добавлять новые классы,")
print("просто унаследовав их от Figure.")
print("Они автоматически будут встраиваться в общую логику.")
print("="*60)

# Создаем объекты всех типов (включая новый Triangle)
print("\n1. СОЗДАНИЕ ОБЪЕКТОВ (ВКЛЮЧАЯ НОВЫЙ ТРЕУГОЛЬНИК):")
print("-" * 40)

line = Line((0, 0), 2, "синий", 10)
rect = Rect((5, 5), 4, "красный", 3)
ellipse = Ellipse((10, 10), 3, "зеленый", 5)
triangle = Triangle((20, 20), 5, "фиолетовый", (3, 4, 5))  # ← НОВЫЙ ОБЪЕКТ!

print("✅ Созданы объекты разных типов:")
print(f"   - line     (тип: {type(line).__name__})")
print(f"   - rect     (тип: {type(rect).__name__})")
print(f"   - ellipse  (тип: {type(ellipse).__name__})")
print(f"   - triangle (тип: {type(triangle).__name__}) ← НОВЫЙ!")

# СОЗДАЕМ ОДИН ОБЩИЙ СПИСОК (с новым объектом)
print("\n" + "="*60)
print("2. СОЗДАНИЕ ОДНОГО ОБЩЕГО СПИСКА (С НОВЫМ ТИПОМ):")
print("="*60)

figures = [line, rect, ellipse, triangle]  # ← Добавили треугольник!
print("✅ Создан список figures с новым объектом Triangle")
print("   Список: [Line, Rect, Ellipse, Triangle]")
print("   ⚠️ ЦИКЛ НЕ МЕНЯЛСЯ! Мы просто добавили новый объект в список")

print("\n" + "="*60)
print("3. ТОТ ЖЕ САМЫЙ ЦИКЛ (НЕ ИЗМЕНЯЛСЯ!):")
print("="*60)
print("⚠️ ВНИМАНИЕ! Цикл остался ТОЧНО ТАКИМ ЖЕ, как в задаче 7!")
print("Мы НЕ добавляли новые if/else, НЕ писали новые циклы.")
print("Просто добавили новый объект в список.")
print("-" * 40)

# =============================================
# ЭТОТ ЦИКЛ НЕ ИЗМЕНИЛСЯ НИ НА ОДНУ СТРОЧКУ!
# Он точно такой же, как в задаче 7!
# =============================================
for figure in figures:
    figure.draw()  # ← Цикл НЕ ИЗМЕНЯЛСЯ!

print("\n" + "="*60)
print("4. ДЕМОНСТРАЦИЯ: МЫ НЕ ЗНАЕМ ТИПЫ:")
print("="*60)

print("Типы объектов в списке:")
for i, figure in enumerate(figures, 1):
    print(f"  Элемент {i}: {type(figure).__name__}")

print("\n" + "="*60)
print("5. ПРЕИМУЩЕСТВА ПОЛИМОРФИЗМА:")
print("="*60)

print("""
✅ Без изменения цикла мы добавили новый класс!
✅ Программа легко расширяется новыми типами
✅ Не нужно переписывать старую логику
✅ Нет новых if/else или циклов
✅ Добавление новой фигуры - просто создание нового класса

💡 Главное преимущество:
   Программа расширяется без изменения существующего кода!
""")

print("="*60)
print("ВЫВОД:")
print("="*60)
print("✅ Полиморфизм позволяет легко РАСШИРЯТЬ программу")
print("✅ Новый класс Triangle добавлен БЕЗ ИЗМЕНЕНИЯ цикла")
print("✅ Цикл из задачи 7 остался ТОЧНО ТАКИМ ЖЕ")
print("✅ Добавление новых типов НЕ ТРЕБУЕТ переписывания старого кода")
print("✅ Это главное преимущество полиморфизма!")