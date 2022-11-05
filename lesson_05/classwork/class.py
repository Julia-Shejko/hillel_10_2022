class Comp:
    name = "lenovo"

    def __init__(self, cpu, memory, ssd):
        self.cpu = cpu
        self._memory = memory
        self.__ssd = ssd

    def get_cpu(self):
        return self.cpu

    def memory(self):
        return self._memory

    def get_ssd(self):
        return self.__ssd

    @staticmethod
    def some_method(num):
        return num

    @classmethod
    def name_pc(cls, name):
        cls.name = name
        return cls.name


comp_1 = Comp(12, 15, 20)

print(comp_1.some_method(3))
