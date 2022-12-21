from dataclasses import dataclass


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


@dataclass
class Training:
    """Базовый класс тренировки."""

    action: int
    duration: float
    weight: float

    M_IN_KM = 1000
    LEN_STEP = 0.65
    MIN_IN_H = 60

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return (self.action * self.LEN_STEP / self.M_IN_KM)

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return (self.get_distance() / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


@dataclass
class Running(Training):
    """Тренировка: бег."""

    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # (18 * средняя_скорость + 1.79) * вес_спортсмена
        # / M_IN_KM * время_тренировки_в_минутах
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed()
                + self.CALORIES_MEAN_SPEED_SHIFT) * self.weight
                / self.M_IN_KM * (self.duration * self.MIN_IN_H))


@dataclass
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    height: float

    CALORIES_WEIGHT_MULTIPLIER = 0.035
    CALORIES_SPEED_HEIGHT_MULTIPLIER = 0.029
    KMH_IN_MSEC = 0.278
    CM_IN_M = 100

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий при спортивной ходьбе."""
        # (0.035 * вес + (средняя_скорость_в_метрах_в_секунду**2
        # / рост_в_метрах) * 0.029 * вес) * время_тренировки_в_минутах
        return ((self.CALORIES_WEIGHT_MULTIPLIER * self.weight
                + (((self.get_mean_speed() * self.KMH_IN_MSEC) ** 2)
                 / (self.height / self.CM_IN_M))
                * self.CALORIES_SPEED_HEIGHT_MULTIPLIER * self.weight)
                * self.duration * self.MIN_IN_H)


@dataclass
class Swimming(Training):
    """Тренировка: плавание."""

    length_pool: float
    count_pool: int

    LEN_STEP = 1.38
    CALORIES_MULTIPLIER = 1.1
    CALORIES_SHIFT = 2

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость при плавании."""
        # длина_бассейна * count_pool / M_IN_KM / время_тренировки
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий при плавании."""
        # (средняя_скорость + 1.1) * 2 * вес * время_тренировки
        return ((self.get_mean_speed() + self.CALORIES_MULTIPLIER)
                * self.CALORIES_SHIFT * self.weight * self.duration)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    workout_dict: dict[str, Training] = {'SWM': Swimming,
                                         'RUN': Running,
                                         'WLK': SportsWalking}
    return workout_dict[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
