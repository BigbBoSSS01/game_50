class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__was_born()


    def __was_born(self):
        print(f'Animal {self.__name} was born')

    def set_age(self, age):
        if type(age) != int or age <= 0:
            raise ValueError("age must be greater than zero")
        else:
            self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
        

    def info(self):
        return (f'{self.__name} is {self.__age} years old. '
                f'Birth year: {2025 - self.__age}.')
    

# some_animal = Animal('anim', 2)
# some_animal.set_age(3)

# print(some_animal.info())
# print(some_animal.get_age())
# print(some_animal.get_name())



class Cat(Animal):
    def __init__(self, name, age):
        super(Cat, self).__init__(name, age)




class Dog(Animal):
    def __init__(self, name, age, commands):
        super(Dog, self).__init__(name, age)
        self.__commands = commands


    @property
    def commands(self):
        return self.__commands
    

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super().info() + f' commands: {self.__commands}'

class FightingDog(Dog):
    def __init__(self, name, age, commands, wins):
        super(FightingDog, self).__init__(name, age, commands)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins
    
    @wins.setter
    def wins(self, value):
        self.__wins = value

    def fight(self):
        print(f'Dog {self.get_name()} is fighting')

    def info(self):
        return super().info() + f', wins: {self.__wins}'







cat = Cat('kitty', 3)
# print(Cat.get_name())
cat.set_age(2)
# print(cat.info())



dog = Dog('sharic', 8, 'sit')
dog.commands = 'sit, run'
print(dog.commands)


Fighting_Dog = FightingDog('Borzic', 1, 'fight', 20)



print(cat.info())
print(dog.info())
print(Fighting_Dog.info())