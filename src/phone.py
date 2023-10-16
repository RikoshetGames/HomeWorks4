from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__name = name
        self._number_of_sim = number_of_sim

    def __repr__(self):
        return ' '.join([f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self._number_of_sim})"])

    def __str__(self):
        return f"{self.__name}"

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if isinstance(value, int):
            self._number_of_sim = value
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")


