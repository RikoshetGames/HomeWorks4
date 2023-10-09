import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name[:10]
        self.price = price
        self.quantity = quantity
        self.all.append(self)


    def __repr__(self):
        """
        Возвращает информацию для разрабочика в режиме отладки.
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает пользовательскую информацию о классе.
        """
        return f"{self.__name}"


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        :return: Цена со скидкой.
        """
        self.price = self.price * self.pay_rate
        return self.price


    @classmethod
    def instantiate_from_csv(cls, file_path):
        """
        Инициализируюет экземпляры класса `Item` данными из файла src/items.csv.
        """
        with (open(file_path, "r") as file):
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                price = float(row["price"])
                quantity = int(row["quantity"])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(value: str) -> int:
        """
        Возвращает число из число-строки.
        """
        number = int(float(value))
        return number


    @property
    def name(self) -> str:
        """
        :return: Название товара.
        """
        return self.__name


    @name.setter
    def name(self, name: str) -> None:
        """
        Присваивает новое название для товара и обрезает до 10 символов.
        :return: Новое название товара.
        """
        self.__name = name[:10]


