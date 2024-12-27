class Bird(ABC):
    """
    Базовий клас для птахів.
    """
    @abstractmethod
    def move(self):
        pass


class FlyingBird(Bird):
    """
    Клас для птахів, які можуть літати.
    """
    @abstractmethod
    def fly(self):
        pass


class NonFlyingBird(Bird):
    """
    Клас для птахів, які не можуть літати.
    """
    def move(self):
        print("This bird walks or swims.")


class Sparrow(FlyingBird):
    """
    Горобець - птах, який може літати.
    """
    def move(self):
        print("Sparrow is flying.")

    def fly(self):
        print("Sparrow is flying high!")


class Penguin(NonFlyingBird):
    """
    Пінгвін - птах, який не може літати.
    """
    def move(self):
        print("Penguin is swimming.")


# Використання
def let_bird_move(bird):
    bird.move()


sparrow = Sparrow()
penguin = Penguin()

# Тепер функція коректно працює з обома типами птахів
let_bird_move(sparrow)
let_bird_move(penguin)
