import doctest


class Wireless_headphones:
    def __init__(self, current_battery_percentage: int, connection_status: bool):
        """
        Создание и подготовка к работе объекта "Беспроводные наушники"

        :param current_battery_percentage: Текущий заряд батареи в процентах
        :param connection_status: Статус подключения

        Примеры:
        >>> tws_headphones = Wireless_headphones(100, True)  # инициализация экземпляра класса
        """
        if not isinstance(current_battery_percentage, int):
            raise TypeError("Текущий заряд батареи должен быть типа int")
        if current_battery_percentage < 0 or current_battery_percentage > 100:
            raise ValueError("Текущий заряд батареи должен быть от 0 до 100")
        self.current_battery_percentage = current_battery_percentage

        if not isinstance(connection_status, bool):
            raise TypeError("Статус подключения должен быть bool")
        self.connection_status = connection_status

    def are_headphones_connected(self) -> bool:
        """
        Функция которая проверяет подключены ли наушники

        :return: Подключены ли наушники

        Примеры:
        >>> tws_headphones = Wireless_headphones(100, True)
        >>> tws_headphones.are_headphones_connected()
        """
        ...

    def charge_battery(self, extra_percents: int) -> None:
        """
        Функция которая заряжает наушники

        :param extra_percents: Дополнительные проценты зарядки

        :raise ValueError: Если после зарядки заряд превысит 100 вызовем ошибку

        Примеры:
        >>> tws_headphones = Wireless_headphones(60, True)
        >>> tws_headphones.charge_battery(40)
        """
        if not isinstance(extra_percents, int):
            raise TypeError("Добавочный заряд батареи должен быть типа int")
        if extra_percents < 0:
            raise ValueError("Добавочный заряд должен быть положительным числом")
        ...


class Person:
    def __init__(self, age: int, name: str):
        """
        Создание и подготовка к работе объекта "Человек"

        :param age: Возраст человека
        :param name: Имя человека

        Примеры:
        >>> human = Person(22, "Vladimir")  # инициализация экземпляра класса
        """
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age < 0:
            raise ValueError("Возраст должен быть больше 0")
        self.age = age

        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        self.name = name

    def is_person_name(self, suggested_name: str) -> bool:
        """
        Функция проверяет зовут ли человека так, как думает пользователь

        :return: Совпадают ли имена

        Примеры:
        >>> human = Person(22, "Vladimir")
        >>> human.is_person_name("Alexey")
        """
        if not isinstance(suggested_name, str):
            raise TypeError("Предполагаемое имя должно быть типа str")
        ...

    def get_age(self) -> int:
        """
        Функция возвращает возраст человека

        :return: Возраст человека

        Примеры:
        >>> human = Person(22, "Vladimir")
        >>> human.get_age()
        """


class Ball:
    def __init__(self, weight: int, color: str):
        """
        Создание и подготовка к работе объекта "Мячик"

        :param weight: Вес мячика в ньютонах
        :param color: Цвет мячика

        Примеры:
        >>> ball = Ball(100, "Red")  # инициализация экземпляра класса
        """
        if not isinstance(weight, int):
            raise TypeError("Вес должен быть типа int")
        if weight < 0:
            raise ValueError("Вес должен быть больше 0")
        self.weight = weight

        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        self.color = color

    def change_color(self, new_color: str) -> None:
        """
        Функция меняет цвет мячика

        Примеры:
        >>> ball = Ball(100, "Red")
        >>> ball.change_color("Blue")
        """
        if not isinstance(new_color, str):
            raise TypeError("Новый цвет должен быть типа str")
        ...

    def play_with_ball(self) -> None:
        """
        Функция позволяет поиграть с мячиком

        Примеры:
        >>> ball = Ball(100, "Red")
        >>> ball.play_with_ball()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
