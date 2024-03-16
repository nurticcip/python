class Animal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    def sound(self):
        pass


class Mammal(Animal):
    def __init__(self, name, age, gender, is_domestic):
        super().__init__(name, age, gender)
        self.is_domestic = is_domestic

    def sound(self):
        return "Mammal sound"


class Bird(Animal):
    def __init__(self, name, age, gender, is_flying):
        super().__init__(name, age, gender)
        self.is_flying = is_flying

    def sound(self):
        return "Bird sound"


class Reptile(Animal):
    def __init__(self, name, age, gender, is_poisonous):
        super().__init__(name, age, gender)
        self.is_poisonous = is_poisonous

    def sound(self):
        return "Reptile sound"


class Lion(Mammal):
    def __init__(self, name, age, gender, is_domestic):
        super().__init__(name, age, gender, is_domestic)

    def sound(self):
        return "Roar"


class Eagle(Bird):
    def __init__(self, name, age, gender, is_flying):
        super().__init__(name, age, gender, is_flying)

    def sound(self):
        return "Screech"


class Snake(Reptile):
    def __init__(self, name, age, gender, is_poisonous):
        super().__init__(name, age, gender, is_poisonous)

    def sound(self):
        return "Hiss"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_animals_info(self):
        for animal in self.animals:
            print(animal)

    def make_sounds(self):
        for animal in self.animals:
            print(f"{animal.name} makes {animal.sound()} sound")


# Тестирование системы
zoo = Zoo()
lion = Lion("Simba", 5, "Male", False)
eagle = Eagle("Eddy", 3, "Female", True)
snake = Snake("Slytherin", 2, "Male", True)

zoo.add_animal(lion)
zoo.add_animal(eagle)
zoo.add_animal(snake)

print("Zoo Animals:")
zoo.show_animals_info()

print("\nAnimal Sounds:")
zoo.make_sounds()

