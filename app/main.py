class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{" \
               f"Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}" \
               f"}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore_instance: Herbivore) -> None:
        is_carnivore = isinstance(herbivore_instance, Carnivore)
        if not herbivore_instance.hidden and not is_carnivore:
            herbivore_instance.health -= 50
        if herbivore_instance.health <= 0:
            Animal.alive.remove(herbivore_instance)
