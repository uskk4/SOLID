from abc import ABC, abstractmethod

class Workable(ABC):
    """
    Інтерфейс для роботи.
    """
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    """
    Інтерфейс для їжі.
    """
    @abstractmethod
    def eat(self):
        pass


class OfficeWorker(Workable, Eatable):
    """
    Офісний працівник може працювати та їсти.
    """
    def work(self):
        print("Office worker is working.")

    def eat(self):
        print("Office worker is eating lunch.")


class Robot(Workable):
    """
    Робот може тільки працювати.
    """
    def work(self):
        print("Robot is working.")


# Використання
def manage_work(worker: Workable):
    worker.work()

def manage_lunch(worker: Eatable):
    worker.eat()


# Тестування
office_worker = OfficeWorker()
robot = Robot()

manage_work(office_worker)
manage_lunch(office_worker)

manage_work(robot)
# manage_lunch(robot)  # Помилка: Robot не реалізує Eatable
