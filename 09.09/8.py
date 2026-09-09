class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu, *mem_slots):
        self.name = name
        self.cpu = cpu
        self.mem_slots = list(mem_slots)
        while len(self.mem_slots) < 4:
            self.mem_slots.append(None)
    
    def get_config(self):
        config = []
        config.append(f"Материнская плата: {self.name}")
        config.append(f"Процессор: {self.cpu.name}, {self.cpu.fr}")
        config.append("Слоты памяти:")
        for i, mem in enumerate(self.mem_slots):
            if mem:
                config.append(f"  Слот {i+1}: {mem.name} - {mem.volume}")
            else:
                config.append(f"  Слот {i+1}: пусто")
        return config