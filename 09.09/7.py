class Graph:
    def __init__(self, data):
        self.data = data[:]
        self.is_show = True
    
    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            print("Отображение данных закрыто")
    
    def set_show(self, fl_show):
        self.is_show = fl_show