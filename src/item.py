import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = f'Файл {kwargs.get("filename")} поврежден'
        super().__init__(self.message)



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
        self.__name = name
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


    def __add__(self, other):
        """
        Сложение экземпляров класса "Phone" и "Item".
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise ValueError("Складывать можно только объекты Item и дочерние от них.")


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
    def instantiate_from_csv(cls, filename: str) -> None:
        """
        Инициализируюет экземпляры класса `Item` данными из файла src/items.csv.
        """
        file_path = f"../{filename}"
        cls.all = []
        try:
            with open(file_path, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if "name" not in row or "price" not in row or "quantity" not in row:
                        raise InstantiateCSVError
                    name = row["name"]
                    price = float(row["price"])
                    quantity = int(row["quantity"])
                    cls(name, price, quantity)
        except InstantiateCSVError:
            print(f"Файл {filename} поврежден")
            raise

        except FileNotFoundError:
            print(f"Отсутствует файл {filename}")
            raise


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






