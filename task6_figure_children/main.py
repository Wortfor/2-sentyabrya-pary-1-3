# Задача 6: Дочерние классы Line, Rect, Ellipse (наследование)
class Figure:
    """
    Базовый класс Figure с общими свойствами для всех фигур.
    """
    
    def __init__(self, coords, width, color):
        """
        Конструктор базового класса Figure.
        
        Параметры:
        coords (tuple): координаты фигуры (x, y)
        width (float): ширина фигуры
        color (str): цвет фигуры
        """
        self.coords = coords      # координаты (x, y)
        self.width = width        # ширина
        self.color = color        # цвет
    
    def get_info(self):
        """
        Метод для получения информации о фигуре.
        """
        return f"координаты {self.coords}, ширина {self.width}, цвет {self.color}"


class Line(Figure):
    """
    Дочерний класс Line (линия).
    Наследует все свойства от Figure и добавляет length (длина).
    """
    
    def __init__(self, coords, width, color, length):
        """
        Конструктор класса Line.
        Вызывает конструктор родительского класса Figure через super().
        
        Параметры:
        coords (tuple): координаты (x, y)
        width (float): ширина линии
        color (str): цвет линии
        length (float): длина линии (уникальное свойство)
        """
        # Вызываем конструктор родительского класса
        super().__init__(coords, width, color)
        # Добавляем уникальное свойство
        self.length = length
    
    def get_info(self):
        """
        Переопределяем метод get_info() для Line.
        Добавляем информацию о длине.
        """
        base_info = super().get_info()
        return f"Линия: {base_info}, длина {self.length}"


class Rect(Figure):
    """
    Дочерний класс Rect (прямоугольник).
    Наследует все свойства от Figure и добавляет height (высота).
    """
    
    def __init__(self, coords, width, color, height):
        """
        Конструктор класса Rect.
        Вызывает конструктор родительского класса Figure через super().
        
        Параметры:
        coords (tuple): координаты (x, y)
        width (float): ширина прямоугольника
        color (str): цвет прямоугольника
        height (float): высота прямоугольника (уникальное свойство)
        """
        # Вызываем конструктор родительского класса
        super().__init__(coords, width, color)
        # Добавляем уникальное свойство
        self.height = height
    
    def get_info(self):
        """
        Переопределяем метод get_info() для Rect.
        Добавляем информацию о высоте.
        """
        base_info = super().get_info()
        return f"Прямоугольник: {base_info}, высота {self.height}"


class Ellipse(Figure):
    """
    Дочерний класс Ellipse (эллипс).
    Наследует все свойства от Figure и добавляет radius (радиус).
    """
    
    def __init__(self, coords, width, color, radius):
        """
        Конструктор класса Ellipse.
        Вызывает конструктор родительского класса Figure через super().
        
        Параметры:
        coords (tuple): координаты (x, y)
        width (float): ширина эллипса
        color (str): цвет эллипса
        radius (float): радиус эллипса (уникальное свойство)
        """
        # Вызываем конструктор родительского класса
        super().__init__(coords, width, color)
        # Добавляем уникальное свойство
        self.radius = radius
    
    def get_info(self):
        """
        Переопределяем метод get_info() для Ellipse.
        Добавляем информацию о радиусе.
        """
        base_info = super().get_info()
        return f"Эллипс: {base_info}, радиус {self.radius}"


print("="*60)
print("НАСЛЕДОВАНИЕ КЛАССОВ: РАСШИРЯЕМ ФУНКЦИОНАЛЬНОСТЬ")
print("="*60)
print("Согласно теории:")
print("Благодаря механизму наследования классов,")
print("мы можем использовать ранее созданные классы")
print("и расширять их функциональность.")
print("="*60)

# Создаем объекты дочерних классов
print("\n1. СОЗДАНИЕ ОБЪЕКТОВ ДОЧЕРНИХ КЛАССОВ:")
print("-" * 40)

line = Line((0, 0), 2, "синий", 10)
rect = Rect((5, 5), 4, "красный", 3)
ellipse = Ellipse((10, 10), 3, "зеленый", 5)

print("✅ Линия создана")
print("✅ Прямоугольник создан")
print("✅ Эллипс создан")

print("\n" + "="*60)
print("2. ВЫВОД ИНФОРМАЦИИ О КАЖДОЙ ФИГУРЕ:")
print("="*60)

print(f"\n{line.get_info()}")
print(f"\n{rect.get_info()}")
print(f"\n{ellipse.get_info()}")

print("\n" + "="*60)
print("3. ДОСТУП КО ВСЕМ СВОЙСТВАМ:")
print("="*60)

print(f"\nLine: координаты {line.coords}, ширина {line.width}, цвет {line.color}, длина {line.length}")
print(f"Rect: координаты {rect.coords}, ширина {rect.width}, цвет {rect.color}, высота {rect.height}")
print(f"Ellipse: координаты {ellipse.coords}, ширина {ellipse.width}, цвет {ellipse.color}, радиус {ellipse.radius}")

print("\n" + "="*60)
print("4. ИЕРАРХИЯ НАСЛЕДОВАНИЯ:")
print("="*60)

print("""
        ┌─────────────────┐
        │    Figure       │  ← БАЗОВЫЙ КЛАСС
        │  - coords       │
        │  - width        │
        │  - color        │
        └────────┬────────┘
                 │
    ┌────────────┼────────────┐
    │            │            │
    ▼            ▼            ▼
┌─────────┐ ┌─────────┐ ┌─────────┐
│  Line   │ │  Rect   │ │ Ellipse │  ← ДОЧЕРНИЕ КЛАССЫ
│ - length│ │ - height│ │ - radius│
└─────────┘ └─────────┘ └─────────┘
""")

print("="*60)
print("ВЫВОД:")
print("="*60)
print("✅ Дочерние классы наследуют все свойства Figure")
print("✅ Каждый дочерний класс добавляет УНИКАЛЬНОЕ свойство")
print("✅ Код не дублируется (принцип DRY)")
print("✅ super() вызывает конструктор родительского класса")
