# Задача 5: Базовый класс Figure (наследование)
class Figure:
    """
    Базовый класс Figure с общими свойствами для всех фигур.
    Это пример НАСЛЕДОВАНИЯ из теории ООП.
    
    Согласно принципу DRY (Don't Repeat Yourself):
    - Общие свойства выносятся в базовый класс
    - Дочерние классы наследуют их и добавляют свои уникальные свойства
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
        Будет использоваться дочерними классами.
        """
        return f"координаты {self.coords}, ширина {self.width}, цвет {self.color}"


print("="*60)
print("ПРИНЦИП DRY - НЕ ПОВТОРЯЙСЯ")
print("="*60)
print("Вместо того чтобы в каждом классе писать:")
print("  self.coords = coords")
print("  self.width = width")
print("  self.color = color")
print("Мы выносим это в БАЗОВЫЙ КЛАСС Figure")
print("="*60)

# Демонстрация работы базового класса
print("\n1. СОЗДАНИЕ БАЗОВОГО КЛАССА Figure:")
print("-" * 40)

# Создаем базовую фигуру (как пример)
figure = Figure((0, 0), 10, "красный")
print(f"Базовая фигура: {figure.get_info()}")

print("\n" + "="*60)
print("2. ПОЧЕМУ ЭТО ВАЖНО (DRY):")
print("="*60)

print("""
❌ ПЛОХО (дублирование кода):
----------------------------------------
class Line:
    def __init__(self, coords, width, color, length):
        self.coords = coords    # дублируется
        self.width = width      # дублируется
        self.color = color      # дублируется
        self.length = length    # уникальное

class Rect:
    def __init__(self, coords, width, color, height):
        self.coords = coords    # дублируется
        self.width = width      # дублируется
        self.color = color      # дублируется
        self.height = height    # уникальное

✅ ХОРОШО (наследование):
----------------------------------------
class Figure:                   # БАЗОВЫЙ КЛАСС
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

class Line(Figure):             # НАСЛЕДУЕТ Figure
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)  # вызывает родительский конструктор
        self.length = length    # только уникальное!

class Rect(Figure):             # НАСЛЕДУЕТ Figure
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)  # вызывает родительский конструктор
        self.height = height    # только уникальное!
""")

print("="*60)
print("ВЫВОД:")
print("="*60)
print("✅ Базовый класс Figure содержит ОБЩИЕ свойства")
print("✅ Дочерние классы будут НАСЛЕДОВАТЬ эти свойства")
print("✅ Код не дублируется - соблюдается принцип DRY")
print("✅ При изменении общих свойств, меняется только в одном месте")
