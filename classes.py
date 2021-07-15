import random


class Person:

    def __init__(self, firstname, lastname, health, status):
        " initialize attributes used in/available for all class methods\
        in this clas, and for class objects created by this class. "
        self.firstname=firstname
        self.lastname=lastname
        self.health=health
        self.status =status

    def introduce(self):
        "All people will introduce themselves"
        print('Hello, my name is {} {}'.format(self.firstname, self.lastname))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion ==1:
            print("{} is happy today".format(self.firstname))
        elif emotion ==3:
            print("{} is sad right now".format(self.firstname))


    def status_change(self):
        if self.health==100:
            print("{} is at full health".format(self.firstname))
        elif self.health >= 76:
            print("{} is a little tired".format(self.firstname))
        elif self.health >= 51:
            print("{} is feeling unwell".format(self.firstname))
        elif self.health >= 25:
            print("{} needs a doctor".format(self.firstname))
        else:
            print("{} is unconscious".format(self.firstname))

Maria = Person("Maria", "La del Barrio", 95, status=True)
Nick = Person("Nick", "Fury", 60, status=True)
Lee = Person('Lee', "Adama", 52, status=False)

print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Lee.lastname, Lee.status))

Nick.introduce()
Lee.introduce()
Maria.introduce()

Nick.status_change()
Lee.status_change()
Maria.status_change()



class Enemy(Person):

    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname,lastname,health,status)
        self.weapon = weapon

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.firstname))
        elif other.health <= 50:
            print("{}, I'm going to take you down".format(other.firstname))

    def introduce(self):
        print('You are my sworn enemy and I will kill you')


Alex = Enemy('rock', 'Aleksei', 'Andreiko', 75, status=False)
Alex.introduce()

Alex.hurt(Maria)
Alex.insult(Nick)