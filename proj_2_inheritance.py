#наследие

my_animal = ''

class Animal:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def sit(self):
        print(self.name.title() + ', sit, fantastic!')

    def voice(self):
            print('How loud!')

    def old_check(self):
        if self.age < 5:
            print ('Hello, ' + self.name + ' the ' + self.breed + ', my young friend')
        else :
            print ('Hello, ' + self.name + ' the ' + self.breed + ', my old friend')

class Cat(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name, breed, age)

    def old_check(self):
        super().old_check()

    def voice(self):
        if self.breed == 'cat':
            print('Nice meow!')
        else:
            pass
        super().voice()

my_animal = Cat ('Murka', 'cat', 5)
my_animal2= Cat ('Rex', 'dog', 1)

my_animal.sit()
my_animal.old_check()
my_animal.voice()
print ('\n')
my_animal2.sit()
my_animal2.old_check()
my_animal2.voice()
