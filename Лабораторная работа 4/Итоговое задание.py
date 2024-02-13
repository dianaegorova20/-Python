class Vehicle:
    """Базовый класс для транспортных средств."""

    def __init__(self, brand: str, color: str):
        """
        Конструктор класса Vehicle.

        Args:
            brand (str): Марка транспортного средства.
            color (str): Цвет транспортного средства.
        """
        self.brand = brand
        self.color = color

    def __str__(self) -> str:
        """
        Магический метод, возвращающий строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return f"{self.color} {self.brand}"

    def __repr__(self) -> str:
        """
        Магический метод, возвращающий представление объекта для отладки.

        Returns:
            str: Представление объекта для отладки.
        """
        return f"Vehicle(brand={self.brand}, color={self.color})"


class Car(Vehicle):
    """Дочерний класс для легковых автомобилей."""

    def __init__(self, brand: str, color: str, num_doors: int):
        """
        Конструктор класса Car.

        Args:
            brand (str): Марка автомобиля.
            color (str): Цвет автомобиля.
            num_doors (int): Количество дверей.
        """
        super().__init__(brand, color)
        self.num_doors = num_doors

    def __str__(self) -> str:
        """
        Магический метод, возвращающий строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return f"{super().__str__()}, {self.num_doors} doors"

    def open_door(self, door_num: int) -> str:
        """
        Открыть указанную дверь автомобиля.

        Args:
            door_num (int): Номер двери.

        Returns:
            str: Сообщение о том, что дверь открыта.
        """
        return f"The door {door_num} is now open."

    def start_engine(self) -> str:
        """
        Перегруженный метод для запуска двигателя автомобиля.

        Returns:
            str: Сообщение о запуске двигателя.
        """
        return "The car's engine is now running."


# Пример использования классов
vehicle = Vehicle("Toyota", "Red")
print(vehicle)  # Вывод: Red Toyota

car = Car("Honda", "Blue", 4)
print(car)  # Вывод: Blue Honda, 4 doors

print(car.open_door(2))  # Вывод: The door 2 is now open.
print(car.start_engine())  # Вывод: The car's engine is now running.