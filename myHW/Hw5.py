import random

class Human:
    def __init__(self, name, sex, birthday, hair_length, nail_length, nail_color = "бесцветные"):
        self.name = name
        self.sex = sex
        self.birthday = birthday
        self.hair_length = hair_length
        self.nail_length = nail_length
        self.nail_color = nail_color

    def __str__(self):
        return f'Я {self.name}, у меня волосы длины {self.hair_length} см. и {self.nail_color} ногти длины {self.nail_length} мм.'

class Worker:
    def __init__(self, name, sex, birthday):
        self.name = name
        self.sex = sex
        self.birthday = birthday

class Manicurist(Worker):
    def do_job(self, other) :
        if other.nail_length > 1 :
            other.nail_length -= 1
        other.nail_color = random.choice(['красные', 'фиолетовые', 'зелёные'])

class Hairdresser(Worker):
    def do_job(self, other) :
        if other.hair_length > 1 :
            other.hair_length -= 1

class Barber(Worker):
    def do_job(self, other) :
        if other.sex == "M" :
            if other.hair_length > 1 :
                other.hair_length -= 1
        else: 
            raise ValueError

neo = Human(name="Neo", sex="M", birthday=1964, hair_length=10, nail_length=2)
trinity = Human(name="Trinity", sex="F", birthday=1967, hair_length=30, nail_length=5)

manicurist = Manicurist(name="Samara", sex="F", birthday=1992)
hairdresser = Hairdresser(name = "Kate", sex="F", birthday=1999)
barber = Barber(name="Bob", sex="M", birthday=1987)

manicurist.do_job(trinity)
barber.do_job(neo)

print(neo)
print(trinity)