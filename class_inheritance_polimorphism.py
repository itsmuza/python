# inheritance

# parent class can only provide public and protected properties to its child class
class Animal:
    _description = "This is animal class"

    def __init__(self, voice):
        self.voice = voice
        self._status = "animal is alive"

    def make_voice(self):
        print(f"animal can make voice: {self.voice}")


class Dog(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}")

    def protect(self):
        print("I can protect you")


class Cat(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}")

    def play(self):
        print("I can play with you")


class Fish(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}")

    def swim(self):
        print("I can swim ")


dog = Dog("Baris", "wow", True)
cat = Cat("Tom", "myow", True)
fish = Fish("Nemo", "zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

dog.make_voice()
cat.make_voice()
fish.make_voice()

print(dog._status)
